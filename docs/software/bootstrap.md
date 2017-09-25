# Bootstrapping your device

**Boostrapping** is actually initialising your device from scratch. It encompasses 3 steps: 

1. Burning bootable images on all 6 SSDs if your have an Intel device, or SD cards if you have an ARM device
1. Bringing the system to the latest level of the firmware
1. Verifying proper functioning of your device

> **WARNING**
> 
> We bootstrap your device for you in our labs!!! 
>
> So, unless you have been **explicitly asked by us** to re-bootstrap your device,  you should NEVER execute this procedure yourself!!!


## Burning SD cards
We have build a project to generate the SSDs and SD cards on a laptop. The supported environment is a 
computer running Ubuntu (14.4) with an integrated SD card reader for the micro SDHC cards, or a USB to 
M.2 SATA converter for the NUC SSDs. 

You can also [generate SD card images on a Wandboard](generate_SD_wandboard.md), if e.g. you have a ARM device at your disposal. 

> All our tests to burn SD cards with an USB dongle failed miserably. We have no clue why. However, this would allow us to generate 6 SD cards fully in parallel!

1. Clone the bigboards-bootstrap project at `https://github.com/bigboards/bigboards-bootstrap.git`
1. Check if the profile for your device is present under `./profiles; if not: 
    1. run `./addprofile` and answer the questions to provide:
        1. `<NAME>` of your device
        1. `<ARCH>` of your device, either `armv7l` or `x86_64` 
        1. `<SEQ>` of your device, is the number of your device in our back-office application; ask us if you require it. The sequence number of your device also becomes visible as your device's internal IP address `172.17.<SEQ>`
1. Adjust the disk image environment to suit your needs:
    1. Depending on the host system on which you are generating the disk images, you'll run `burn` on Intel en `burn-arm` on ARM
    1. Run `sudo fdisk -l` with an SSD or SD card inserted to validate device and partition numbering on your host
    1. Verify the shell script if the default `DEVICE` is in line with the output of `fdisk`  
    1. Check the file `<MY_ARCH>/vars/environment` if the partition number is in line with the output of `fdisk`    
1. Run `./burn <device-name>` or `./burn-arm <device-name>` for all the SSDs or SD cards you have to generate. On a Wandboard you might have to reboot the host for each card, because if fails to unmount the SD card properly  

## Booting your device

Insert the generated SSDs or SD cards in the correct sequence in your device: 

1. The **1st disk or card** is for the **master node**, i.e. the node at the side where the network uplink is connected to your Hex.
1. The **2nd until 6th disk or card** are inserted in **clockwise** order when looking at your device from the top

![Hex and order of nodes](../images/hex-nodes.svg)

Power up your device! 
After booting your device for the 1st time, verify that you can connect to all nodes via SSH. 

`ssh bb@<device-ip>` using either the internal network or the external IP address. To find the external address you can: 

* use an **mDNS browser** like Bonjour
* run an **`arp -a`** command for discovery
* check your **router** or **DHCP server** for handed out IP addresses  


## Update your device to the latest firmware level
After you generated the SSDs or SD cards for your device, it is initialised at firmware v1.0. 
So we need to bring it to the latest level of the firmware before we can start installing 
e.g. the `bb CLI` or anything else.

1. Login to your 1st/master node
1. Check your current firmware version on the [versions](./versions.md) page. Currently, `v1.3` is the latest.
	1. `grep bigboards /etc/apt/sources.list | cut -d' ' -f3`
	1. `sudo vim /etc/apt/sources.list`
	1. `deb http://apt.bigboards.io/ <version> main` as last line
1. Run these commands to install the updater and MMC into the latest version
	1. `sudo apt-get update`
	1. `sudo apt-get install bigboards-cli`
	1. `bb system init` which asks for your device's name and number of nodes
	1. `bb system bootstrap`
	1. `bb firmware upgrade <version>`
	1. `bb firmware update`
1. If your internal network is on a conflichting range, you can switch the IP range
	1. `bb network switch xxx.yyy.zzz` to choose the network subnet you like to use.
	1. Normally your device is initialized to `172.17.<SEQ>` where `<SEQ>` is the device's number in our backoffice application

## Verify proper functioning of your device
After the initialisation in the previous step, your device should be at the required firmware and fully operational. 

Verify your device by 

1. browse to the management console `http://<device-ip>:7000` using either the internal or the external IP. Normally your device
1. check that all your nodes are visible in the dashboard
1. can you access all your nodes via SSH?

The next step is to [link your device](link.md) to the [BigBoards Hive](hive.md).
