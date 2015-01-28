# Networking
All nodes of the hex can be reached using SSH but for that to work you will need to know a few things about the hex. 

First thing to know is that while there only is one physical network interface per node, each node has actually two different ip addresses. One ip address configured on eth0 and  initially set in the range of 172.20.40.x is the internal network. We use this internal network to pass commands around the hex and to make sure all nodes can talk to each other, even when the other address is unavailable.

The other ip address is configured on eth0:0 and set using DHCP by your DHCP server. This one is considered to be the external network connection and is used by the node to retrieve data from the internet.

 