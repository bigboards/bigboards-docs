# Create a docker container

Apps are not directly installed onto the host operating system. Doing that would make it really hard to keep the OS clean and lean. It would also make it a real horror to make sure all component versions match up.

For making this easier, we rely on docker. Docker is a very popular application containerization technology that allows us to run our applications inside a sandbox environment called a container. This container can be added or removed from a host without leaving traces. For more details about docker, make sure to check out their website.

Docker also has a whole library of already existing docker containers called [the docker hub](https://hub.docker.com/). The bigboards containers are also hosted [there](https://hub.docker.com/u/bigboards). You can choose one of these docker containers to use inside your app, or you can continue reading on how to create your own.

The best way to create new docker containers is to create a Dockerfile. The Dockerfile contains the definition of what is to be included inside your docker container. We will
create a docker directory with a new directory for each container we want to build. In our case that will be elasticsearch:

```
 $> mkdir $WORK/docker
 $> mkdir $WORK/docker/elasticsearch
 $> touch $WORK/docker/elasticsearch/Dockerfile

```

Once you invoked those commands, you should have a docker directory containing an elasticsearch directory containing the Dockerfile. The next steps will all happen inside the Dockerfile, so fire up you favourite text editor (**not** Word) and open that Dockerfile file so we can add some content to it.

## FROM
A docker containers always relies on another container to use as a base. Usually the base would be something like 'ubuntu', but we at bigboards already created some base images to make things easier:

 - **base-x86_64** - The absolute base image for X86_64 architectures. It is based on the ubuntu baseimage
 - **base-armv7l** - The absolute base image for ARM v7 architectures. It is based on mazzolino/armhf-ubuntu

 - **nodejs-x86_64** - The base image + nodejs 0.10.25 for x86_64 architectures.
 - **nodejs-armv7l** - The base image + nodejs 0.10.25 for ARM v7 architectures.

 - **java-7-x86_64** and **java-8-x86_64** - The base image + java 7 or 8 for X86_64 architectures.
 - **java-7-armv7l** and **java-8-armv7l** - The base image + java 7 or 8 for ARM v7 architectures.

Now, to define this in our docker file we can add the following line:

```
FROM bigboards/base-x86_64
```

This will use the bigboards base image as the foundation to build your app on. But there is a gotcha there. This will only create an image for x86_64, so not for ARM v7. If you would like to create a single Dockerfile for both architectures, you could use the \_\_arch\_\_ placeholder. 

```
FROM bigboards/base-__arch__
```

When building with the bigboards build environment, this will be replaced with the architectures you configured. However, the build environment is not open to the public yet, so you need to use the static alternative for now. You can always reach out to us to add it to the build system though.

Since elasticsearch is using java, we benefit from using one of the java base images for our container:

```
FROM bigboards/java-8-__arch__
```

## MAINTAINER
Usually you also want to indicate that you are the maintainer of this docker container, so you can add some maintainer information with this tag:

```
MAINTAINER Daan Gerits (daan@bigboards.io)
```

## ADD
During the construction of the container, you might want to use some files or binaries. These binaries can be packed together with your Dockerfile, if you are unable to retrieve them online.

Let's add a test.txt file holding "Hello Resource" as means of an example. Switch to the commandline to create folder to hold both files:
```
 $> mkdir $WORK/docker/elasticsearch/docker_files
 $> echo "Hello Resource" > $WORK/docker/elasticsearch/docker_files/test.txt
```

Once that is done, we will have a nice test.txt file in our docker_files directory. Now it is time to let the docker build process know that this file needs to be included in the build. For that, switch back to the editor holding the Dockerfile and enter the following:

```
ADD docker_files/test.txt /test.txt
```

So as a result of that line, our test.txt file will be available at the root of our filesystem.

## Installing Software
With the RUN statement we can run applications inside the container during the build process. Usually you will want to do this to get the binaries for your application from a website using wget, or install a package using apt. I'll show you how to do both.

Beware that each run statement will create a new layer in docker's layered filesystem. Having a lot of images can cause the installation of an app to take a very long time. There are some tricks you can do to join multiple commandline statements into one single RUN statement. Since that is a more advanced topic, we will not handle that here right now, but do reach out if you have questions about it.

### Downloading and unpacking an archive
One of the most common cases you will encounter is downloading and unpacking a tarbal or zipfile. For that you can use the following statements:

```
RUN wget -O /tmp/my-archive.tar.gz http://... .tar.gz
RUN tar -xzf /tmp/my-archive.tar.gz -C /my/target/directory
```

As you can see, we first download the archive using wget and store it as /tmp/my-archive.tar.gz. Next we unpack it using the tar command and we use /my/target/directory as the folder to unpack to.

If your unpacked folder contains a version number (elasticsearch-2.3.4), you can make a symlink to a more simple name (elasticsearch):

```
RUN ln -s elasticsearch-2.3.4 elasticsearch
```

### Using APT to install a package
Since most of the bigboards images are running on top of ubuntu, you can also use apt to install a package.

```
RUN apt-get update && apt-get install -y vim
```

The command above will install vim inside the container. It uses two commands inside a single RUN statement; first do _apt-get update_ then do _apt-get install -y vim_. Make sure you notice that **-y** flag when installing, it makes sure apt will not ask you to confirm anything when installing.

### Using APT to install a package with a new sources.list entry
In case you would need to add a new sources.list entry, there are a few more steps to take, so let's start with creating a file holding the sources.list entry:

```
 $> mkdir $WORK/docker/elasticsearch/docker_files
 $> echo "deb https://packages.elastic.co/elasticsearch/2.x/debian stable main" > $WORK/docker/elasticsearch/docker_files/elasticsearch.list
```

We will also do that for the archive file:

```
 $> wget -O $WORK/docker/elasticsearch/docker_files/archive.key https://packages.elastic.co/GPG-KEY-elasticsearch
```

Once both have been done, we can add the ADD and RUN commands to our docker file:

```
ADD docker_files/archive.key /tmp/archive.key
ADD docker_files/elasticsearch.list /etc/apt/sources.list.d/elasticsearch.list

RUN apt-key add /tmp/archive.key
RUN apt-get update && apt-get install -y elasticsearch
```

## Adding Volumes
Volumes are a way to hook data that exists on the host system into the docker container. Volumes mounts have to be defined in the docker file as well as in the app configuration later on in order to work. The simplest version of a volume is shown below, where we create the /data folder and indicate it is ready to be link to a volume.

```
RUN mkdir /data
VOLUME /data
```

A more complex example is the use in combination with alternatives. The use of alternatives is quite common in the bigdata world since it allows you to switch between multiple configuration sets in an easy way. In the example below, we create a new directory and register it as an alternative. After all that is done, we indicate the folder can be used to link a volume.

```
RUN mkdir -p /etc/kafka/conf && \
    update-alternatives --install /etc/kafka/conf kafka-conf /etc/kafka/conf.bb 1 && \
    update-alternatives --set kafka-conf /etc/kafka/conf.bb
VOLUME /etc/kafka/conf.bb
```

For our elasticsearch app, we will need to register a data folder as well as a configuration folder as a volume:
```
RUN mkdir /data
VOLUME /data
VOLUME /elasticsearch/conf
```

## Expose Ports
Usually when running some kind of service in a container, you will want to make a connection to it from the outside. This is where the EXPOSE statement comes in. With EXPOSE, you can register which ports should be available to the outside world.

```
EXPOSE 9200 9300
```

## Command to run
Docker containers are meant for application virtualization, which means that only a single application can run inside a container. Using the CMD statement, we can tell docker which command that should be.

```
CMD ["/elasticsearch/bin/elasticsearch"]
```

## Summary
When all this is done, you should end up with a Dockerfile that looks like this:

```
FROM bigboards/java-8-__arch__

MAINTAINER Daan Gerits (daan@bigboards.io)

ADD docker_files/archive.key /tmp/archive.key
ADD docker_files/elasticsearch.list /etc/apt/sources.list.d/elasticsearch.list

RUN apt-key add /tmp/archive.key
RUN apt-get update && apt-get install -y elasticsearch

RUN mkdir /data
VOLUME /data
VOLUME /etc/elasticsearch

EXPOSE 9200 9300

CMD ["elasticsearch"]
```