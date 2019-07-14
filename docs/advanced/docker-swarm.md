# Docker Swarm
Current versions of the [Docker Engine] include swarm mode for natively 
managing a cluster of Docker Engines, called a **Docker swarm**.  
You can use cse the Docker CLI to create a swarm, deploy application services to a swarm, and manage swarm 
behavior.

This tutorial outlines how to turn your BigBoards device in a [Docker Swarm] and **manage it from your workstation** 
with the Docker CLI.

## Prerequisites
To complete the tutorial, there are some prerequisites:

1. Do a [factory reset](../hardware/factory-reset.md) of your device.
1. [Install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) on all nodes 
    1. `bb run 'apt-get remove docker docker-engine docker.io'`
    1. `bb run 'apt-get update'`
    1. `bb run 'apt-get -y upgrade'`
    1. `bb run 'apt-get -y autoremove'`
    1. `bb run 'apt-get -y install linux-image-extra-$(uname -r) linux-image-extra-virtual'`
    1. `bb run 'apt-get -y install apt-transport-https ca-certificates curl software-properties-common'`
    1. `bb run 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'`
    1. `bb run 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'`
    1. `bb run 'apt-get -y update'`
    1. `bb run 'apt-get -y install docker-ce'`
    1. `bb run 'docker run hello-world'`
    
## Build a swarm
The next step is to turn your BigBoards device in a [Docker Swarm]. 

How to do this is explained in Docker's [Swarm tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/), 
but here is the rundown:

1. Log in to your device's master node, i.e. **node-1**
1. Initialize the master node as the **swarm manager**
    1. Note the IP address of the manager node; you can use the internal IP
    1. `docker swarm init --advertise-addr <MANAGER-IP>`
    1. Copy the `COMMAND-TO-JOIN` the swarm as it is printed by the init command
1. Join the **other nodes to the swarm**
    1. `ansible host-workers --sudo -m shell -a '<COMMAND-TO-JOIN>'`
1. Check the status of the swarm
    1. `docker info` gives you an overview of the swarm
    1. `docker node ls` lists all nodes in the swarm, e.g. 
    
```
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
pjtfg2sxm914w616bufmh9tqq *   jill-n1             Ready               Active              Leader
jgqr12mnpxf91lk1fj4eihudf     jill-n2             Ready               Active
c8tqqhjhrr0ng4bwbx8joxf3o     jill-n3             Ready               Active
``` 

## Wrap up
So, that's it! In this tutorial you learned how to turn your BigBards device into a [Docker Swarm] cluster by:

1. Doing a **factory reset** of all the nodes of your BigBoards device
1. **Install docker** on all nodes
1. Initialize the master node as your **swarm manager**
1. and finally join all additional nodes to **form the swarm**  

With this setup, you have a 3 -or 6-node **docker swarm**, which you can 
completely manage from the [Docker Engine] running on your workstation.

## Unswarm
To undo the swarming of you BigBoards device, follow these steps:

1. Remove all running services
    1. List running services `docker service ls`
    1. Remove running services `docker service rm <SERVICE>` 
1. Disconnect your local [Docker Engine] from your swarm
    1. `unset DOCKER_HOST`
1. Remove your swarm from [Docker Cloud]
    1. Go to [Docker Cloud]
    1. Log in
    1. Go to *Swarms (Beta)*
    1. Find the target swarm in the list
    1. Use the ⠇ drop down menu 
    1. *Unregister* the swarm
1. Log in to the devices 1st node
1. End running services
    1. `docker service ls`
    1. `docker service rm 'dockercloud-server-proxy'`
1. Unswarm the nodes of your BigBoards device
    1. List the nodes in the swarm `docker node ls`
    1. Remove the workers `ansible host-workers --sudo -m shell -a 'docker swarm leave'`
    1. Verify workers have left `docker node ls` should indicate status `Down`
    1. Have the master node leave the swarm `docker swarm leave -f` which will also erase all cluster state!

**Done!**

[Docker Cloud]: https://cloud.docker.com
[Docker Engine]: https://docs.docker.com/engine/
[Docker Swarm]: https://docs.docker.com/engine/swarm/
