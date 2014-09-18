Hardware
#######################################################################################################################
You might have seen terms like *Hex* or *Tint* on our website, or even in the documentation you are reading right now. This chapter explains all these terms for you.

Hex
=======================================================================================================================
A Hex is the name of the hardware device we are offering as the company BigBoards. The name is obviously derived from its typical Hexagonal shape. Just calling a Hex a device does not do it justice, since it is a package of 6 individual but complete computers. Each node has its own CPU, memory, storage and network link. So a Hex effectively is a cluster of 6 nodes.

Node
=======================================================================================================================
Each of the nodes is a computer on its own. We implemented our prototype using ARM SoCs (System on Chip). Each node has its own CPU, memory, storage and network.

+-------------+-----------------------------------------------------+
| **CPU**     |  Cortex-A9 Quad core Freescale i.MX6 at 1Ghz        |
+-------------+-----------------------------------------------------+
| **Memory**  |  2Gb DDR3                                           |
+-------------+-----------------------------------------------------+
| **Storage** |  1Tb 7200RPM 2.5" HDD (data) + 16Gb MicroSD (OS)    |
+-------------+-----------------------------------------------------+
| **Network** |  Gigabit Ethernet                                   |
+-------------+-----------------------------------------------------+

Master node
=======================================================================================================================
One of the nodes within the Hex is the master node, because he plays a leading part in your Hex. The master node a.o. hosts the management console: the web console you can use to manage your Hex.

The WiFi antenna you are seeing at the outside of the Hex is connected to the master node. That's how you can easily identify the master node.

In the future however we would like to move the management console as well as the antenna to a separate controller instead of making one node more valuable then the others.

Container
=======================================================================================================================
To keep the nodes of your Hex as stable as possible, the software stacks (Stack Tints) run on top of a Linux container. The container isolates all programs and configurations of the Tints from the hosting operating system of the node. This way, we keep the actual node clean and lean.

Linux Containers, or LXC for short, creates virtual environments through the linux kernel. The general term is application virtualization. LXC does not use any kind of hypervisor like Xen or VMWare to do create a virtual machine, but encapsulates the applications on the operating system, resulting in close to no performance loss. The latter is off course extremely important when you run on limited devices.

These containers are being created on your Hex when you install a stack tint. For example, when you install the Hadoop Tint a container will be created and hadoop will be installed inside this container. From the outside world, the containers are seen as separate machines because they do received their proper ip address on the network.

Integrated switch
=======================================================================================================================
The Hex comes with is own 8-ports Gigabit ethernet switch to interconnect all nodes. The switch has a large enough backplane to support all six nodes sending data continuously.

Internal LAN
=======================================================================================================================
The Hex is a device you can take with you and as such we need a flexible network configuration. Most distributed technologies don't handle network changes very well. The internal network allows your Hex to be disconnected from the outside world. The ip addresses of the internal network will always stay the same, unless you change them yourselves.

When you first get your Hex the internal network is configured with ip addresses in the 172.20.40.0/28 range. Unless you have multiple Hexes on your network there is really no reason to change the internal ip address. In case you have multiple Hexes on your network, you can change the internal range of ip addresses using the management console.

External LAN
=======================================================================================================================
Having an immutable internal network comes in handy, but you probably also want to reach the Hex from other devices like your laptop. The moment you connect a cable between the Hex and your company or home network all nodes ànd containers of your Hex will become first class members of your network. Relying on DHCP for delivering ip addresses, each node but also each container will receive an address. This external connection will also be used the moment a node needs to reach out to the internet.

The nodes are setup to support multicast DNS. If your networks supports this technology, all your nodes and containers are network addressable using their names instead of ip addresses. Have a look at the :ref:`multicast DNS <mDNS>` section of the :doc:`Getting Started <../gettingstarted>` page to know how the names of nodes and containers are structured.

Power
=======================================================================================================================
When you apply power to the Hex you will do so by using an external AC to DC adapter. This adapter will transform the electricity from your wall outlet to 12VDC. Once fed into the Hex, the integrated power module will bring the power down to 5VDC and distribute that to the different nodes and hard disks. Depending on your model the internal switch will take 12VDC or 5VDC.

Due to the use of low energy consuming parts we are able to keep the power consumption as low as 48W during continuous high load! Your Hex idles around 28W!!
