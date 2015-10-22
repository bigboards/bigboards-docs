#Versions

Following versions can be found in the wild (oldest first):

 * Genesis
 * Feniks
 * Ember

## BigBoards Genesis
 Genesis is the first version of the software on top of the BigBoards hex. It provides a web-based management console and uses serf to communicate between the nodes. Tints are running inside an LXC container as a whole operating system. Problems with the stability of Genesis led to the creation of Feniks.

## BigBoards Feniks
Starting with Feniks, we changed the tint system to use docker instead of LXC. The main reason for this were the strange things we were seeing when working with LXC containers. Sometimes containers wouldn't start, or were started but not available to connect to. In short, a lot of issues we tried to solve.

And then it happened. News started pouring in that some guys had managed to get docker running on ARM. For us this was quite big news since we started experimenting with docker on ARM a few months before. The first tests we did already proved docker to be a more stable solution then LXC.

## BigBoards Ember
Ember is our intermediate release, building further upon Docker as application virtualisation technology for our Tints. Ember has numerous bug fixes to render you Hex more stable as before!

## BigBoards Gemini
Gemini is twins release, finally officializing **nHex** as our new model of your personal cluster! nHex is the same type of 6-node personal cluster but centered around **Intel NUC** as platform for compute nodes. We have models available with Intel i3, i5 and i7 processors with 8GB or 16GB or RAM per node!!!

## BigBoards v1.3
From version `v1.3`onward, your devices and the **Library** with it **Tints** are managed from the central **Hive**. You can find it at <http://hive.bigboards.io>.   
