# Big Data in 1-2-3
To get you up and running as fast as possible, here are the steps you need to take:

 1. Plug in network and power
 2. Ensure your cluster is linked to the Hive
 2. Connect your browser to the MMC `http://<hex-name>.hex.bigboards.io:7000/`
 3. Install an app from the library 

## Network and power
Since your BigBoards micro-cluster is a networked electronic device, it benefits from being connected to your LAN and getting power. This means you will have to make a connection from your device to a free ethernet port and your wall outlet. 

> An external power supply is shipped with your device.

At the back of your micro-cluster you'll find 

* 2 ethernet ports and
* 1 power connector.

### Networking
This is the easiest part. Using a regular ethernet cable, plug it in in either of 2 ethernet ports available. Internally, your micro-cluster simply contains a 1GB ethernet switch. So all ports are equal.

The other free port can be used to: 

* either link your laptop directly to your micro-cluster in case you need direct access to the [internal network](hardware/network);
* either link another micro-cluster to your LAN by daisy-chaining multiple devices together.

### Powering On

To power up your micro-cluster you simply have to use the shipped **external power supply**. The PSU can be used for any **AC voltage between 110V and 230V**, so you will be able to use it close to anywhere on the planet. 

1. Attach the separate power cord to the power supply. The delivered cord is a regular computer power cord. 
1. The other connector of the PSU needs to be plugged into your micro-cluster to power it up. 
    1. You can find the power connect in between the 2 ethernet ports at the back of your device. 
    1. There are two models of the BigBoards hardware: [Hex and Cubes](hardware/#models). Each model has a different type of connector: 
        * The power connector for the **Cube** is a round `DIN4` connector. 
        * The **Hex** powers supply is a `6-pin Molex` connector. 
    1. You might have to press the power supply's connector firmly for the device to start. 
1. Plug the power cord into a wall outlet. Make sure the deliver cord is suitable for your region.

Once the power connection has been made, your micro-cluster boots.

## Is your cluster linked to the Hive?
The first thing to do, is to link your micro-cluster to the Hive using your account.

To verify if your device is linked, login to the hive at [http://hive.bigboards.io](http://hive.bigboards.io) and check your [clusters](http://hive.bigboards.io/#/clusters).

Is your device listed here? Does in contain all it's nodes if you look at the details page? That's perfect!

If not, follow [the guide to link your cluster](software/link). 

## The MMC

Point your browser to [http://&lt;hex-name&gt;.hex.bigboards.io:7000/](http://&lt;hex-name&gt;.hex.bigboards.io:7000/)

What you see is the management console of your micro-cluster. We call it the **MMC**. More info [here](software/mmc). 

The MMC allows you to operate your device: 

* install apps from the library, 
* open a shell to a specific node to run commands,
* look at the ops stats of your device,
* link to this docmentation set,
* directly get support from us via our ticketing system.

How is that for power at your fingertips!

### Alternatively, connect using SSH

Every node can be addressed using SSH using the **bb** user.

```
my-laptop:> ssh bb@<cluster-name>-n[1-6].<cluster-name>.hex.bigboards.io
```

The password for the `bb` user is ```Swh^bdl```.

## Install an app
The BigBoards Library is prefilled with available app for your micro-cluster. You can simply install any of these by the click of a button. 

Go to [http://<hex-name>.hex.bigboards.io:7000/#/library](http://<hex-name>.hex.bigboards.io:7000/#/library)


Choose the app that you want to install. Click on it, to get to the details. Click on the `Install` button to install it on your Hex.

And you are good to go!
