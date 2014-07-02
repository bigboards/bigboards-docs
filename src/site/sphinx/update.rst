Update
######
Once you are the proud owner of a hex, you will need to know how you can work with it. This section will explain how you make sure your hex is up and running with the latest firmware.

For the impatient
=================
 - Go to the management console.
 - Click on the 'update' button 

Or

 - Login to the hex
 - execute 'apt-get update'
 - execute 'apt-get install bigboards-updater'
 - execute '/opt/bb/runtimes/bigboards-updater/update.sh'

Updating your hex
=================
Before we get started, let's go into a bit of context.
A single node inside a hex is actually a running linux system. It is provisioned with Ubuntu Raring (13.10), but this will probably change in the near future. Because we don't want the installation of tints to obfuscate the core linux system, we run all our tint related stuff inside a linux container. This way we can just throw away the container once we don't want anything to do with the tint anymore. The core linux system will remain intact.

The BigBoards Updater will actually only update the core linux system. It will update the management console you see when surfing to the hex or modify some core system settings to make sure your hex is running smoothly.

Currently you are in charge of executing updates but we are thinking of changing this. The idea would be to push changes to all the hexes so you are always running the most stable version out there. This would allow us to have everyone running the same version, limiting overhead. However, if you think this would be a bad idea, we are very open to have a discussion about it.

So up to the updating process itself. There are two ways to update your hex. The easiest by far is making use of the update button on the management console. Surf to the ip address of your hex and you will see a button with two arrows on it. Click it and it will start the update process.

The other option is to use the commandline by making an SSH connection to your hex. In order to update you need to perform the following operations:::

	bb1 #> sudo apt-get update
	bb1 #> sudo apt-get install bigboards-updater
	bb1 #> /opt/bb/runtimes/bigboards-updater/update.sh

If all commands complete succesfully you will have a new firmware running on your hex.