Getting started
###############
You Hex is delivered to you as a fully assembled and completely installed device! Normally, there is nothing additional you have to do, but to unbox it and start to use it!

Power
=======================================================================================================================
Since the Hex is an electronic device, it benefits from having power. This means you will have to make a connection from your Hex to your wall outlet. An **external power supply** is provided to make this connection.

#. Plug the **round power plug** into the Hex. You can find the power jack next to the wireless antenna at the bottom of the device

#. Attach the separate **power cord** to the power supply. The delivered cord is a regular computer power cord.

#. Plug the power cord into a **wall outlet**.

Once a connection has been made, the **6 white LEDs** at the bottom of the Hex light up and the Hex boots.

Network
=======================================================================================================================
The Hex contains an **internal 8-ports ethernet switch** which you can use at any time to make wired connections, either directly with your computer, either with your LAN.

.. warning:: The master node contains WiFi (with antenna) but is unused for now.

The networking within you Hex is setup to be able to run 2 separate LANs:

#. The **internal LAN** interconnects all nodes across the internal switch and is setup with static IP adresses.

#. The **external LAN** interconnects all nodes with your home or office LAN when you hook your Hex's internal switch to you LAN by an ethernet cable.

Making a wired network connection with your LAN
-----------------------------------------------------------------------------------------------------------------------
Using the internal switch, you can hook your Hex to your LAN.

#. Plug a regular CAT5e (or higher) ethernet cable into one of the two **free ports at the bottom of the Hex**.

#. Plug the other end of the ethernet cable into an RJ45 **port of your LAN or local/desktop switch**.

Your Hex will be assigned **12 ip addresses** from your network's DHCP server (LAN server or home router) in the range your LAN is setup. Each node and each container will receive its own ip address.

If your network allows **multicast DNS**, your Hex will be visible on the network using his **personal name**, e.g. Alice. All nodes and containers receive an identifiable network name: ::

    <name>-[n|v]x
    where name is the Hex's personal name
      and n for nodes
      and v for containers
      and x = 1..6 for the number of the node

E.g. ``Alice-n1`` for Alice's master node and ``Alice-v6` for the last node's container.

.. note:: For container names to appear, a Tint has to be installed on your Hex, otherwise containers are not created on your Hex.

Making a wired network connection directly with your computer
-----------------------------------------------------------------------------------------------------------------------
You can directly connect your laptop to the internal switch of your Hex. However, as the internal network is static, you have to reconfigure your personal computer's network settings.

#. On your laptop or desktop, attach an **ethernet cable**, at least CAT5e.

#. Plug the other side of the ethernet cable into 1 of the **2 free ethernet ports at the bottom of your Hex**.

#. **Change the network configuration** on your computer to use a static ip address. You will need the following parameters to do this: ::

	ip address: 172.20.40.200
	netmask: 255.255.255.0
	gateway: <none>

 .. note:: Any ip address above ``172.20.40.16`` should do, because ``172.20.40.[1-6]`` are used for the physical nodes and ``172.20.40.[11-16]`` for the Tints containers.

What ip address does my Hex's master node effectively use?
-----------------------------------------------------------------------------------------------------------------------
The ``<ip address>`` that the master node of your Hex effectively uses, depends on how you have set up your networking:

#. If you have connected your Hex to the **LAN**, your LAN will have dispatched an ip address using DHCP.

    #. if your LAN supports **multicast DNS**, you are able to target your Hex's master node as ``<name>-n1``, where ``<name>`` is your Hex's personal name.

    #. but if your LAN does **NOT** support **multicast DNS**, you will have to figure out what ip address was assigned to your Hex's master node. Either ask your infrastructure team, check your home router or temporarily make a wired connection directly between your Hex and your computer. In the former case, you can SSH into your Hex and run ``ìfconfig`` to list available networks.

#. If you have connected your Hex **directly to your computer**, you can address your Hex's master node at ``172.20.40.1``

Browsing to your Hex's management console
=======================================================================================================================
Point your web browser to ``http://<ip address>/`` once you know the ip address of your Hex's master node.

The master node will serve the BigBoards management console that allows you to monitor the resource usage of your Hex, as well as to perform management operations like updating your Hex's firmware or installing tints.
