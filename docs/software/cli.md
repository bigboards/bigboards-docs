# BigBoards command-line utility

To make it easier to administer your hex, we also created a little program you can run from the command prompt. It is called ```bb``` and in general you will invoke it with a set of options. This part of the documentation will explain all available options.

## network
### switch
Change the internal network prefix. If you want to combine multiple hexes in the same network, you will have to make sure each of your hexes is running on a different ip range. By default the internal network is configured to use addresses in the ```172.20.40``` range, but you can easily change this (to 172.20.30 for example) by invoking the following command:

```
> bb network switch 172.20.30
```

## version
### switch
BigBoards uses different releases and will only give you updates in a specific release. However, if you want to upgrade the version of the release you can do so by invoking 

```
> bb version switch <new-release-name>
```

### update
To make sure you are running the latest version of your release, you can invoke the ```bb update``` command. This will update the BigBoards software, but will also invoke any patches that have not been installed yet.

## run
Running a single command on a multitude of nodes can be a bit of a hassle. Therefor we created a little wrapper around ansible to allow you to invoke any command on all nodes at the same time.

```
> bb run "<your command in quotes>"
```

Remember to put the quotes, otherwise only a part of your command will be invoked on the remote nodes.

## mmc
### start
Start the web interface and API server on the master node.

```
> bb mmc start
```
### stop
Stop the web interface and API server on the master node.

```
> bb mmc stop
```

### restart
Restart the web interface and API server on the master node.

```
> bb mmc restart
```

### status
Check if the web interface and API server are running on the master node.

```
> bb mmc status
```

## containers
### list
List all containers running on the master node.

```
> bb containers list
```

### attach
Attach to the container with the given name on the master node.

```
> bb containers attach <container-name>
```

### tail
Follow the contents of a stdout of a container. The container should be running on the master node.

```
> bb containers tail <container-name>
```