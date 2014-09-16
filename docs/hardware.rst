Hardware
#######################################################################################################################

A Hex
=======================================================================================================================
A large part of BigBoards is centered around the Hex, an Hexagon shaped cluster of 6 nodes. Each of these nodes have their own CPU, memory and storage. They are all interlinked over an integrated 8-ports 1GB ethernet switch.

A Node
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

Network
=======================================================================================================================
There is a Gigabit Ethernet switch inside with a large enough back plane to support all six nodes sending data continuously.

One node has a WiFi antenna, allowing WiFi connections to be made to the Hex.

.. warning:: The WiFi is not used yet. We are looking into having the WiFi operate as access point or repeater.

Power
=======================================================================================================================
When you apply power to the Hex you will do so by using an external AC to DC adapter. This adapter will transform the electricity from your wall outlet to 12VDC. Once fed into the Hex, the integrated power module will bring the power down to 5VDC and distribute that to the different nodes and hard disks. Depending on your model the internal switch will take 12VDC or 5VDC.

Due to the use of low energy consuming parts we are able to keep the power consumption as low as 48W during continuous high load. Your Hex idles around 28W.
