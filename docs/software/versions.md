Different versions of the on-device firmware can be found in the wild. The list underneath is chronologically ordered, oldest versions first. 

To check the firmware version of your device, you can run this command on the first node of your Hex: 

`grep bigboards /etc/apt/sources.list | cut -d' ' -f3`

## Genesis
Version `genesis` is the first version of the software on top of the BigBoards Hexes. It provides a web-based management console and uses [Serf](http://serfdom.io) to communicate between the nodes. Apps are running inside an [LXC container](https://linuxcontainers.org/) as a whole operating system. This setup proved not to be the most stable of solutions. 

## Feniks
So, we build the app system on [Docker](https://www.docker.com/) instead of [LXC](https://linuxcontainers.org/). It was quite a struggle to get docker running on top of [ARM chip architecture](http://www.arm.com/) and [the Wandboard platform](http://wandboard.org/)! Docker proved to be much more stable then LXC.

## Ember
Version `ember` is an intermediate release, building further upon [Docker](https://www.docker.com/) as application virtualisation technology for our Apps. Ember has numerous bug fixes to stabilize your Hex!

## Gemini
This is our twins release: finally officializing **nHex** as our new model of your personal cluster! nHex is the same type of 6-node personal cluster but centered around [Intel NUC](http://www.intel.com/nuc/) as platform. We have [models available](http://bigboards.io/orderprototype) with Intel i3, i5 and i7 processors with 8GB or 16GB or RAM per node!!!

## v1.3
From version `v1.3` onward, your devices and the **Library** with its **Apps** are managed from the central **Hive**. You can find it at <http://hive.bigboards.io>.   

Also note that we are moving away from naming our releases with code names in favor of **semantic versioning** our releases. This allows for easier integration with the infrastructure tooling that we use and embed in the Hexes.
