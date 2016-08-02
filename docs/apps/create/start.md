# Create an App
While there are already quite some apps available, chances are that you want to create your own app based on different technologies. App Development is not that difficult, but you benefit from having experience with docker and ansible. In any case, if you are running into trouble, let us know and we'll help out.

As you might have read in the anatomy section, an app exists out of 3 parts:

	- docker containers
	- configuration settings
	- definition

As an example here, we will build an app for elasticsearch, so by the end of this section, you will have an app that runs elasticsearch on a cluster.

Let's create a directory in which to do our work. I will refer to this directory as $WORK from now on just to make it easier.

```
 $> mkdir /home/daan/tutorial
 $> export WORK=/home/daan/tutorial

```

By invoking the two statements above, your $WORK should also point to your directory. You can use any path you like. For me it made sense to put it in /home/daan/tutorial.