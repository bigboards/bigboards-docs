# Bootstrapping your device

**Boostrapping** is actually initialising your Hex from scratch. It encompasses 3 steps: 

1. Burning bootable images on all 6 SD cards of your device
2. Bringing the system to the latest level of the firmware
3. Verifying proper functioning of your device

## Burning SD cards/Users/wvl
We have build a project to generate the SD cards on a laptop. Our supported environment is a laptop running Ubuntu (14.4) with an integrated SD card reader. 

> All our tests to burn SD cards with an USB dongle failed miserably. We have no clue why. However, this could allow us to generate 6 SD cards fully in parallel!

1. Clone the bigboards-bootstrap project at `http://bitbucket.org/bigboards/bigboards-bootstrap.git`
2. Adjust the file `groupvars/all` to 
	1. suit your environment regarding SD card reader which is defined under the `disk` section, specifically `dev` and `'part`
	2. configure the script to generate SD cards for a specific Hex under the `hex` section, specifically `name` and `id`
3. Run the `./setup.sh [1..6]` script for each SD card 
4. Insert the generated SD cards in order in your Hex. 
	1. The 1st card is for the master node, i.e. the node where the power supply is connected.
	2. The 2nd until 6th card are inserted in clockwise order when looking at the hex from the top

![Hex and order of nodes](hex-nodes.svg)

## Update your Hex to the latest firmware level
After you generated your SD cards for your Hex, it is initialised at firmware v1.0. So we need to bring it to the latest level of the firmware before we can start installing e.g. the `bb CLI` or anything else.

1. Login to your master node
	1. Connect it to your LAN
	1. Connect it to power
	1. `ssh bb@<hex>-n1.local`
1. Check your current firmware version
    1. `grep bigboards /etc/apt/sources.list | cut -d' ' -f3`
    1. `sudo vim /etc/apt/sources.list`
    1. `deb http://apt.bigboards.io/ gemini main` as last line
1. Run these commands to install the updater and MMC into the latest version
    1. `sudo apt-get update`
	1. `sudo apt-get install bigboards-cli`
	1. `bb system purge-legacy`
	1. `bb system bootstrap`
	1. `bb firmware upgrade gemini`
	1. `bb firmware update`
1. Switch IP range for the internal network
   1. `bb network switch 10.20.xyz` where xyz is the Hex's number in Podio

## Verify proper functioning of your Hex
After the initialisation in the previous step, your Hex should be at the required firmware and fully operational. 

Verify your Hex by 

1. browse to the management console `http://<hex>-n1.local:7000`
1. check that all your nodes are visible in the dashboard
1. can you access all your nodes via SSH?
