#Creating a stack tint
Starting with Feniks, the tint system got an overhaul. Previously tints were ansible playbooks and it involved quite some technical knowledge to create a tint. With the introduction of Docker we had an opportunity to do things better. The result is a cleaner and easier to use tint environment.

Let's have a look on how to create your own tint. As an example, we will take ElasticSearch as an example.

Creating a tint requires you to:

 1. create a docker image
 2. create a repository on bitbucket.org
 3. create a tint.yml file describing the tint
 4. create a configuration directory holding configuration files
 5. commit everything to the bitbucket.org repo 

We will go through all these steps and explain what you should do to make it work.

## 1. Create a docker image
It may scare you of when you read this the first time, but I promise you it isn't that daunting. Docker requires an image to serve as some sort of template when creating a docker container. This means we need to create that image and make it available through the [docker hub](http://hub.docker.com).

There are several ways to create a new image, but the one we like most is through the use of a DockerFile. A DockerFile describes which actions have to take place to go from one image to another one. You can read more about how DockerFiles work over [here](https://docs.docker.com/reference/builder/)

We already created a set of images which you can use as a base image for your own endeavours. Have a look at our [docker hub page](https://hub.docker.com/u/bigboards/)

For ElasticSearch we started of from the java-7 image we had laying around. So here is the DockerFile we use for that:

```
#
# ElasticSearch Dockerfile
#
# Modified from https://github.com/dockerfile/elasticsearch for the BigBoards Hex.
#

# Pull base image.
FROM bigboards/java-7-armv7l

MAINTAINER bigboards
USER root
ENV ES_PKG_NAME elasticsearch-1.4.2

# install curl
RUN apt-get update && apt-get install -y wget

# Install ElasticSearch.
RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /elasticsearch

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300
```

Once you have created that docker file, copy it to one of the nodes on the hex and build it. (we will provide a command for that in a later version, just to make things easier for you.) And last but not least, don't forget to push it to the repository.
 
**NOTE** - *We will need to do something with this. It is way to difficult to build it and push it unless you have previous docker knowledge*

## 2. Create a repository on bitbucket.org
Right now, a tint can only be installed from bitbucket.org. Before you ask, no we don't have shares there, but all though we like github very much, we like the ability to have free private repositories on bitbucket even more.

That being said, expect github to be integrated really soon.

If you have no account yet, go to [BitBucket](https://bitbucket.org/account/signup/) and create one.

## 3. Create a tint.yml file describing the tint
The tint.yml file holds all information the hex needs to know about the tint to be able to work with it. The tint.yml file will be converted into a set of ansible playbooks used for installing and uninstalling the tint. You can always have a look inside the ```/opt/bb/tints.d/<tint-type>/<tint-owner>/<tint-id>/work``` to see what has actually been generated.

```
stack:
  views:
    - label: "Marvel"
      url: "http:<< nodes[hex.name + '-n1'].ip >>-n1:9200/_plugin/marvel"
      description: "Marvel’s overview dashboard provides full details on the health of your cluster, including cluster-wide metrics, overview of all nodes and indices and events such as master election or the addition of new nodes."
  containers:
    elasticsearch:
      image: "bigboards/elasticsearch-marvel-armv7l"
      command: "/elasticsearch/bin/elasticsearch"
      ports:
        - 9200
        - 9300
      config: "/elasticsearch/config"
  groups:
    es_node:
      runs_on: "all"
      containers:
        - "elasticsearch"
```

Let's go through the sections in this file:
### ```stack```
The root element of the file indicates which kind of tint is being described. For now only stack tints are being supported, but we are in the progress of creating new types as well.

### ```views```
Views are addressable web interfaces that are available after a tint has been installed. This can for example be a web interface for managing the technologies that came with the tint.

Each view should hold a ```label```, used in the web interface to allow you to navigate to the view. Next to that we need the ```url``` where you will be redirected to when navigating to the view. You may use expressions like ```nodes[hex.name + 'n1'].ip``` to get the ip address of the first node, as long as you put them between ```<< >>```. Last but not least, you are encouraged to add a ```description``` to explain what the view is actually meant for.

### ```containers```
Containers refer to docker containers and include all things needed to create the docker containers. To keep thing at a minimum, only the required parameters are listed in the tint.yml example above.

The key of the container object (*elasticsearch* in this case) will be used as the name for the new container. ```image``` denotes the image that is being used to bootstrap the container and should be accessible on the [docker hub](http://hub.docker.io). ```command``` is the command that is being invoked inside the container while ```ports``` enumerate the port mappings being used. The last item, ```config```, indicates where the configuration directory should be mounted, but more on that later.

### ```groups```
While we already know which containers are available for use, we still don't know where each of these containers have to be installed. This is where a ```group``` fits in. A group declares which containers should be running on which hosts. Each group has a unique name (*es_node* in this case) and uses the ```runs_on``` property to define where the containers should be running. You can use any [Ansible pattern](http://docs.ansible.com/intro_patterns.html) to define where the containers should run. Last thing to declare are the actual ```containers``` that should be running. This is a simple list of names of the containers we declared earlier.

## 4. create a configuration directory holding configuration files
Chances are you will have to adept the configuration files that come with the technology you want to install. If you ran through the previous sections you will have noticed there was a property in the container section of the tint.yml file dealing with configuration resources used for the process running inside the container.

A tint can have a ```conf``` directory at its root, holding a sub directory for each container it will create. Files placed in that directory will be considered [jinja2 templates](http://jinja.pocoo.org/docs/dev/templates/), so you can create some pretty advanced structures in there.

You will have to declare where the contents of the conf directory have to be mounted inside the container. In our tint.yml example the directory will be mounted at ```/elasticsearch/config```.
