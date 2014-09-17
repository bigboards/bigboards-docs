Configure the internal network
##############################

The Hex is a device you can take with you and as such we need a flexible network configuration. Most distributed technologies don't handle network changes very well. We called the internal network to live to be able to cope with this. The ip addresses of the internal network will always stay the same, unless you change them yourselves offcourse. 
When you first get your hex the internal network is configured in the 172.20.40.0/28 network. Unless you have multiple hexes on your network there is really no reason to change the internal ip address.

We tried to make it as easy as possible for you to change the internal network ip range if you need to do so. These are the steps to take:

#. Go to the management console and open the tasks screen
#. click on the play button behind the 'network_internal' task.
#. enter the new range in the ip_prefix field. 

.. warning:: Make sure the ip_prefix is structured correctly. It should look like xxx.xxx.xxx so three numbers between 0 and 255 separated by dots.

.. note:: Have we told you you could access the tasks console directly by surfing to http://<your-hex-name>-n1.local/#/tasks ?