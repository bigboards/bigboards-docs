# Migrating to another release

BigBoards devices running on some older version of the firmware can be upgraded to the latest version through the use of the `bb` command.

## What version am I on?

You can check the version you are running by executing the following command:

```
grep bigboards /etc/apt/sources.list | cut -d' ' -f3
```

This command will return one of `<version>` as found on the [versions](versions) page.

## Installing the `bb` CLI on Genesis

**Remark**: This procedure should only be applied when your BigBoards device is running on the *genesis* version of the firmware.

If you are running *genesis* you will notice the `bb` utility is not available. We only added it since *feniks* but
there is an option to install it by hand. Follow these steps to get the `bb` CLI utility:

1) Make sure that all the latest fixes of the software are installed.

```
/opt/bb/runtimes/bigboards-updater/update.sh
```

2) Open the apt `sources.list` file holding the software repositories.

```
sudo nano /etc/apt/sources.list
```

3) Find the line stating `deb http://apt.bigboards.io/repo snapshots/`. It
should be near the last line in the file.

4) Change the line into `deb http://apt.bigboards.io/ feniks main`.

5) Save the changes using *`ctrl-x`*, *`Y`*, *`enter`*.

6) Run `sudo apt-get update`

7) Run `sudo apt-get install bigboards-cli`

## Changing your version

From *feniks* onwards we have a command line utility `bb` for changing the
version.

**Warning**: Make sure you jot down the IP address of your master node,
`<hex-name>-n1`. During the upgrade process, the network gets restarted and you
might need it to be able to reconnect to your master node.

Switching version becomes as simple as

1) Make sure that all the latest fixes of the software are installed.

```
bb firmware update
```

2) Open the apt `sources.list` file holding the software repositories.

```
sudo nano /etc/apt/sources.list
```

3) Find the line stating `deb http://apt.bigboards.io/ <version> main`. It
should be near the last line in the file.

4) Change the line into `deb http://apt.bigboards.io/ <new-version> main`.

5) Save the changes using *ctrl-x*, *Y*, *enter*.

6) Choose one of `<version>` as found on the [versions](versions) page and run:

```
bb firmware upgrade <new-version>
```

7) Run:

```
bb firmware update
```
