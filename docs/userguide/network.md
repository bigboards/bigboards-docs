# Networking
All nodes of the hex can be reached using SSH but for that to work you will need to know a few things about networking on the hex. 

First thing to know is that while there only is one physical network interface per node, each node has actually **two different IP addresses**. 

One IP address is configured on eth0 and is initially set in the range of ```10.20.<hex-number>.[1-6]```. This is the **internal network**. We use this internal network to pass commands around the hex and to make sure all nodes can talk to each other, even when the other address is unavailable.

The other IP address is configured on eth1. It gets its address from the DHCP server on your LAN. This address one is considered to be the **external network** connection. It is used by the node to retrieve data from the internet.

 