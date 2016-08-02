# Anatomy of an app
Apps are built out of two main parts. At one side, there are docker containers. The other side holds the
 configuration for these docker containers to work together. An app will bring both containers and configuration
 together into one unit which can be installed on a device.
 
## Docker containers
Underneath it all, docker is used to isolate different services from each other and gives us the ability
to easily remove everything and start from a clean slate again. Allthough you can use any kind of docker
container that is out there, you might find some optimized containers in our docker-hub realm.

If no docker container is available for the technology you want to use, you can build your own. Once you
 have done so, you can refer to it from the app definition and you are good to go.
 
**Although it is possible, we strongly discourage the use of so called 'fat' docker containers. Docker
 containers are meant for application virtualization, not for machine virtualization.**
 
## Configuration
Currently the configuration is retrieved from any **public** git repo you have access to. These git repo's
hold the configuration for specific services inside the stack. When an app is installed, the configuration
is mounted inside the docker containers so it can be used by the service inside the container.