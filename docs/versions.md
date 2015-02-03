#Versions

Following versions can be found in the wild (oldest first):

 * Genesis
 * Feniks

## BigBoards Genesis
**Genesis** is the *1st version* of the software on top of the BigBoards Hex. It provides 

1. a **web-based management console** (*MMC*) and 
1. uses [**Serf**](http://serfdom.io) to communicate between the nodes. 

In this version, Tints run inside an [LXC container](https://linuxcontainers.org/) as a complete operating system. 

Problems with the stability of **Genesis**, forced us to move away from this setup. Sometimes containers wouldn't start; other times the LXC containers simply were not available over the network. Most of the time, under IO stress, the network would simply crash. 

## BigBoards Feniks
**Feniks** is the *2nd version* of the software on the BigBoards Hex.

In this version, we implemented the Tint system using [Docker](https://docker.com/) as soon  as we heard that some guys got Docker running on ARM. We started experimenting with Docker on ARM a few months before. The first tests we did already proved Docker to be a more stable solution then LXC, however the full port of such a complex product would require too much of our time.