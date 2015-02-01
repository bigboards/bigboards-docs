# Configure the internal network

The Hex is a device you can take with you and as such we need a flexible network configuration. Most distributed technologies don't handle network changes very well. We called the internal network to live to be able to cope with this. 

The **IP addresses of the internal network will always stay the same**, unless you change them yourselves of course. 

When you first get your hex the internal network is configured in the **172.20.40.0/28** IP range. Unless you have multiple hexes on your network there is really no reason to change the internal ip address.

We tried to make it as easy as possible for you to change the internal network IP range if you need to do so. These are the steps to take:

1. Go to the management console and open the **Tasks screen**
1. Click on the **Play button** behind the `network_internal` task.
1. Enter the **new IP range** in the `ip_prefix` field. 

**Warning:** Make sure the `ip_prefix` is structured correctly. It should look like `xxx.xxx.xxx` so three numbers between 0 and 255 separated by dots.

**Note:** Have we told you you could access the tasks console directly by surfing to `http://<your-hex-name>-n1.local/#/tasks` ?