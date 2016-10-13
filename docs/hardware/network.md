# Networking
All nodes of the hex can be reached using SSH but for that to work you will need to know a few things about networking on your micro-cluster. 

First thing to know is that while there only is one physical network interface per node, each node has actually **two different IP addresses**. 

One IP address is configured on ``eth0`` and is initially set in the range of ```172.20.<hex-number>.[1-6]```. This is the **internal network**. We use this internal network to pass commands around the cluster and to make sure all nodes can talk to each other, even when the other address is unavailable.

The other IP address is configured on ``eth1``. It gets its address from the DHCP server on your LAN. This address is considered to be the **external network** connection. It is used by the node to retrieve data from the internet and it used by you to connect to the cluster. The IP addresses of the external network are also automatically registered in our DNS sytem as ``<cluster-name>.hex.bigboards.io`` for the 1st node and ``<cluster-name>-n[1-6].<cluster-name>.hex.bigboards.io`` for all nodes 1 to 6.

 