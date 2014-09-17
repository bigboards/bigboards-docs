Hardware
#######################################################################################################################
You might have seen terms like 'Hex' or 'Tint' on our website or even in the documentation you are reading right now. Allow us to place them into context for you.

Hex
=======================================================================================================================
A Hex points to the hardware device we are offering as a part of BigBoards. Actually calling it a device does not do it justice since it is a combination of 6 individual nodes each with their own CPU, memory and storage. So a Hex is a cluster of 6 nodes (hence the name 'Hex').

We got a lot of feedback from people saying that there was something wrong with our design. There was a really big hole in the middle. Surely there would be better ways to place these nodes so they would not take up that much space. Well, we actually did that on purpose. All though we are using low-power ARM based computing units which produce a significant less amount of heat then their intel based counterparts, there still is some heat we need to get rid of. The hole in the middle of the Hex serves as a chimney, making use of natural air convection to evacuate hot air out of the Hex from the top and sucking in cool air from the bottom. Pretty neat, right?

You can find more details about the Hex in its own documentation section.

Node
=======================================================================================================================
Each of the nodes has their own CPU, memory, network and storage.

+-----------+----------------------------------------------+
| CPU       |  Cortex-A9 Quad core Freescale i.MX6 at 1Ghz |
+-----------+----------------------------------------------+
| Memory    |  2Gb DDR3                                    |
+-----------+----------------------------------------------+
| Network   |  Gigabit Ethernet                            |
+-----------+----------------------------------------------+
| Storage   |  1Tb 7200RPM 2.5" HDD + 16Gb MicroSD (OS)    |
+-----------+----------------------------------------------+

Master node
=======================================================================================================================
One of the nodes within the hex will be dubbed the Master Node. The master node will host the management console; the web console you can use to manage your hex. The WiFi antenna you are seeing at the outside of the hex is also connected to this master node. In the future however we would like to put the management console as well as the antenna to a separate controller instead of making one node more valueable then another.

Container
=======================================================================================================================
We wanted to be sure the nodes of your hex keep as clean as possible. By using linux containers to run the software stacks (stack tints) we can keep the main node clean and lean. Linux Containers, or LXC for short, creates virtual environments through the linux kernel. It will not use any kind of hypervisor like Xen or VMWare to do so, resulting in close to no performance loss. This becomes offcourse even more important when you run it on limited devices.

Containers are being created when you install a stack tint. For example, when you install the hadoop tint a container will be created and hadoop will be installed inside this container.

Integrated switch
=======================================================================================================================
We have used an gigabit ethernet switch to interconnect all nodes. The switch has a large enough back plane to support all six nodes sending data continuously.

Internal LAN
=======================================================================================================================
The Hex is a device you can take with you and as such we need a flexible network configuration. Most distributed technologies don't handle network changes very well. We called the internal network to live to be able to cope with this. The ip addresses of the internal network will always stay the same, unless you change them yourselves offcourse. 
When you first get your hex the internal network is configured in the 172.20.40.0/28 network. Unless you have multiple hexes on your network there is really no reason to change the internal ip address.

External LAN
=======================================================================================================================
Having an immutable internal network comes in handy, but you probably also want to reach the hex from other devices like your laptop. The moment you connect a cable between the hex and your company or home network all nodes of the hex will become first class members of your network. Relying on DHCP for delivering IP addresses, each node will receive an address. This external connection will also be used the moment a node needs to reach out to the internet.

Power
=======================================================================================================================
When you apply power to the Hex you will do so by using an external AC to DC adapter. This adapter will transform the electricity from your wall outlet to 12VDC. Once fed into the Hex, the integrated power module will bring the power down to 5VDC and distribute that to the different nodes and hard disks. Depending on your model the internal switch will take 12VDC or 5VDC.

Due to the use of low energy consuming parts we are able to keep the power consumption as low as 48W during continuous high load. Your Hex idles around 28W.
