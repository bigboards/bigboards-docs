# Update

Once you are the proud owner of a Hex, you will need to know how you can work with it. This section will explain how you make sure your Hex is up and running with the **latest firmware**.

## For the impatient

 - Go to the management console.
 - Click on the 'update' button 

Or

 - Login to the Hex as user `bb``
 - execute `sudo apt-get update`
 - execute `sudo apt-get install bigboards-updater`
 - execute `/opt/bb/runtimes/bigboards-updater/update.sh`

## Updating your Hex

Before we get started, let's go into a bit of context.

A single node inside a Hex is actually a full-blown Linux system. It is provisioned with Ubuntu Trusty Tahr (14.04 LTS).

Because we don't want the installation of Tints to obfuscate the core Linux system, a **Tint runs inside a Linux container** (LXC). This way we can just throw away the container on uninstalling the Tint. The core Linux system will remain intact. Moreover, as Tints are self-contained, their respective container will be maintained by the Tint itself!

Therefor, The BigBoards **updater** will only **update the core linux system**. It will a.o. update the management console ()which you see when browsing to the Hex) or it will modify some core system settings to make sure your Hex is running smoothly.

Currently **you are in charge of executing updates**, however we are investigating how to automate this. The idea would be to push changes to all the Hexes so you are always running the most stable version. This would allow us to have everyone running the same version, thus limiting overhead. However, if you think this would be a bad idea, we are very open to have a discussion about it.

So up to the updating process itself. 

There are two ways to update your Hex: 

* The easiest by far is making use of the **update button** on the management console. Open the management console of your Hex, navigate to the Version page and you will see a button with two arrows on it. Click it and it will start the update process.
* The other option is to use **update script** via the command-line by making an SSH connection to your Hex. You need to perform the following operations:

	`bb1 #> sudo apt-get update`
	`bb1 #> sudo apt-get install bigboards-updater`
	`bb1 #> /opt/bb/runtimes/bigboards-updater/update.sh`

If all commands complete successfully, you will have the latest firmware running on your Hex.

# Patching your Hex

As the requirements for our `bigboards-updater` became more complex, we had to implement the updating process by applying a **series of patches**. 

Each patch is defined by the date it was created, e.g. 20140505 and 20140717.

You apply a specific patch to your Hex by executing:::

	bb1 #> sudo apt-get update
	bb1 #> sudo apt-get install bigboards-updater
	bb1 #> /opt/bb/runtimes/bigboards-updater/patch.sh <patch-id>

where <patch-id> is the ID of the patch you want to apply.

Please note that applying patches in the correct order is crucial. Normally, you should execute them chronologically! So, simply in the order of the patch IDs.

**Warning:** For the time being we have disable the updater because we need to automate the chronological application of patches. For the time being, we'll have to manually apply the various patches to your Hex!
