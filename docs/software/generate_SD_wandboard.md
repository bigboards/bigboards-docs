# Prepare a Wandboard to generate SD cards for your device

As a Wandboard is an ARM computer with 2 microSDHc card slots, it can be used to initialize SD cards for ARM based BigBoards clusters.

The process is a bit elaborate, as we have to write a bootable SD card from still another computer.

Also note that in total, you require `n+1` microSD cards for generating images for BigBoards device!

## Generate SD card to boot your wandboard

The whole process to generate the bootstrap SD card is explained on `ARMhf.com` on the page [Wandboard microSD card installation](http://www.armhf.com/boards/wandboard/wand-sd-install/)

Insert the bootstrap SD card in your Wandboard and boot it. 

## Setup bootstrap environment

1. `sudo apt-get update`
1. `sudo apt-get install software-properties-common`
1. `sudo apt-add-repository ppa:ansible/ansible`
1. `sudo apt-get update`
1. `sudo apt-get install git ansible python-apt`
1. `mkdir workspaces`
1. `cd workspaces`
1. `git clone https://github.com/bigboards/bigboards-bootstrap.git`
1. `cd bigboards-bootstrap`
1. `git config user.name 'My Name'`
1. `git config user.email 'my.name@my.domain'`
1. `git branch -r`
1. `git checkout gemini`
1. Check if a profile for your device exists under `./profiles` if not
    1. `./addprofile`
	    1. fill in `<device-name>`
	    1. choose architecture `armv7l` or `x86_64`
	    1. fill in `<seq>`; ask us if do not know your device's sequence
1. `git add .`
1. `git commit -m 'added new profile'`
1. `git push`

## Burn all other SD card images

Continue to burn all other SD card images for your device as explained on the [bootstrap page](bootstrap.md#burning-sd-cards).