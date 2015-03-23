# Migrating to Feniks
Hexes running on Genesis can be upgraded to Feniks through the use of the ```bb``` command.

## What version am I on?
You can check the version you are running by executing the following command:

	⬢ > grep bigboards /etc/apt/sources.list | cut -d' ' -f3

If you are running genesis, the command above will return `snapshots/`. If you are running feniks the command will return `feniks/`

## Installing the `bb` CLI on Genesis
If you are running genesis you will notice the bb utility is not available. We only added it since feniks but there is an option to install it by hand. Follow these steps to get the `bb` CLI utility:

 1. Make sure that all the latest versions of the software are installed: `⬢ > /opt/bb/runtimes/bigboards-updater/update.sh`
 1. Open the apt sources.list file holding the software repositories: `⬢ > sudo nano /etc/apt/sources.list`
 1. Find the line stating `deb http://apt.bigboards.io/repo snapshots/`. It should be near the last line in the file.
 1. Change the line into `deb http://apt.bigboards.io/ feniks main`
 1. Save the changes using *ctrl-x*, *Y*, *enter*.
 1. run `sudo apt-get update`
 1. run `sudo apt-get install bigboards-cli`

## Changing your version
From feniks onwards we have a commandline utility `bb` for changing the version. 

**Warning**
Make sure you jot down the IP adress of your master node, \<hex-name\>-n1. During the upgrade process, the network gets restarted and you might need it to be able to reconnect to your master node. 

Switching version becomes as simple as 

	⬢ > bb version switch <version-name>
	⬢ > bb version update

where version-name can be **genesis** or **feniks**.

Be sure to run `bb version update` afterwards to effectively apply all changes to your hex.

## <a name="patching"></a> Patching your system
There are moments when you want to get to the latest version of the bigboards software. We create patches to make the most profound modifications to your hex. These patches are included inside the bigboards-updater application and they have to be run in a specific order. But don't worry, that isn't something you should be concerned about. If you want to patch the system, simply run the following command:

	⬢ > bb version update

For the ones of you who do want to dive a bit deeper, we use the `.versions` file to determine the current level of the system. Once a patch is installed a log will be written into this versions file.