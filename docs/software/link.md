# Linking your device to the Hive
Before you can start using your BigBoards micro-cluster properly, you must link your device to your account on the [BigBoards Hive](software/hive) and also register all it's nodes in the Hive and to the cluster.

## Add your cluster to the Hive
Log in to the Hive as described [here](software/hive). 

In the upper right corner of the Hive app, sits the [cluster button](http://hive.bigboards.io/#/clusters) that takes you to list of your clusters. 

If you cluster at hand isn't available in  this list, simply add it by clicking on the ``plus`` button in the bottom right corner and then ``cluster`` button that appears. Give your cluster a ``name`` and ``create`` it.

## Link your device to the Hive cluster
Click on the cluster's card to get to the details of the cluster. 

To link your device to this cluster, open the fan-out menu by clicking the ``hamburger`` icon at the right of the header panel of your cluster and push the ``link`` menu-item.

A dialog appears showing you a long token. You can copy-past that token either by double clicking on the token and hitting ``<ctrl>-c`` or by simply clicking the ``clipboard` icon.

Next, head over to the MMC of your device, click on button at the left that takes you the settings panel. If you Hex is not linked to an account yet, the settings panel will show you a multi-line text field. Paste the cluster token in this field and push the ``link`` button. 

The settings panel will show your name to confirm the linking. 

If your device is already linked to an account, you can unlink it by clicking the ``unlink`` button. The panel will change to the multiline text field.

## Register all your nodes to the Hive
Log in to the Hive as described [here](software/hive). 

In the upper right corner of the Hive app, sits the [devices button](http://hive.bigboards.io/#/devices) that take you to the list of your devices.

If your devices do not show up in this list, we still have to register them. This still is a command-line process. Open a console on your master node by either SSH into the node, or if you have access to the devices MMC, you can simply click the ``terminal`` button behind the first node on the main panel of the console.

From the console run these commands, using your device's name and your profile's short-id from the Hive where required.

1. ``cd ~``
1. ``wget http://apt.bigboards.io/tool.sh``
1. ``chmod a+x tool.sh``
1. ``sudo ./tool.sh init``
1. ``./tool.sh remote <device-name>-n2 init``
1. ``./tool.sh remote <device-name>-n3 init``
1. ``./tool.sh remote <device-name>-n4 init``
1. ``./tool.sh remote <device-name>-n5 init``
1. ``./tool.sh remote <device-name>-n6 init``
1. ``./tool.sh link <short-id>``
1. ``./tool.sh remote <device-name>-n2 link <short-id>``
1. ``./tool.sh remote <device-name>-n3 link <short-id>``
1. ``./tool.sh remote <device-name>-n4 link <short-id>``
1. ``./tool.sh remote <device-name>-n5 link <short-id>``
1. ``./tool.sh remote <device-name>-n6 link <short-id>``