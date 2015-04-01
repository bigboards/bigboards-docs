# Bootstrapping your device

**Boostrapping** is actually initialising your Hex from scratch. It encompasses 3 steps: 

1. Burning bootable images on all 6 SD cards of your device
2. Bringing the system to the latest level of the firmware
3. Verifying proper functioning of your device

## Burning SD cards
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

## Update your Hex to the latest level of Genesis
After you generated your SD cards for your Hex, it is initialised at firmware v1.0. So we need to bring it to the latest level of the `genesis` release before we can start installing e.g. the `bb CLI` or anything else.

1. Start your Hex
	1. Connect it to your LAN
	1. Connect it to power
1. Login to the master node via SSH 
2. Run these commands
	1. `sudo apt-get update`
	2. `sudo apt-get install bigboards-updater`
	3. `cd`
	4. `./runtimes/bigboards-updater/update.sh`

## Verify proper functioning of your Hex
After the initialisation in the previous step, your Hex should be at firmware v1.0 and ready for first operations. 

Simply verify your Hex by 

1. browse to the management console `http://<hex>--n1.local:7000`
1. check that all your nodes are visible in the dashboard
1. can you access all your nodes via SSH?
