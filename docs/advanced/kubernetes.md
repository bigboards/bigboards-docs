# Kubernetes

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) is 
an open-source system for automating deployment, scaling, and management of 
containerized applications.

It groups containers that make up an application into logical units for easy 
management and discovery. Kubernetes builds upon [15 years of experience of 
running production workloads at Google](http://queue.acm.org/detail.cfm?id=2898444), 
combined with best-of-breed ideas and practices from the community.

This tutorial will turn your BigBoards Hex or Cube into a Kubernetes cluster 
using the Kubernetes [custom installation guide](https://kubernetes.io/docs/getting-started-guides/scratch/). 

## Ubuntu 16.04 LTS
Unfortunately Kubernetes is not supported to run on 
[Ubuntu 14.04 LTS (Trusty Tahr)](http://releases.ubuntu.com/14.04/) that is 
originally installed on your BigBoards device. 

So, to install Kubernetes You have to upgrade or install 
[Ubuntu 16.04 LTS (Xenial Xerus)](http://releases.ubuntu.com/16.04/) on all nodes
of your BigBoards device.

> **WARNING** 
>
> The BigBoards firmware is only supported to run on Ubuntu 14.04 LTS. To reinstall
> the BigBoards firmware, you have to reflash your OS disks with the BigBoards 
> firmware. 

### do-release-upgrade
The easiest way to upgrade your BigBoards device is to run [the server-grade release 
upgrade](https://help.ubuntu.com/lts/serverguide/installing-upgrading.html) on all 
the nodes of your device.

### install from USB drive
*To be documented*   

## Installing kubeadm
To install kubeadm, we follow the [install procedure](https://kubernetes.io/docs/setup/independent/install-kubeadm/) 
at [kubernetes.io](https://kubernetes.io).

We however run all commands through `ansible host -s -m shell -a "<CMD>"` command to run on all nodes 
simultaneously. 

1. `ansible host -s -m shell -a "apt-get update && apt-get upgrade -y"`
1. `ansible host -s -m shell -a "apt-get install -y ebtables ethtool"`
1. `ansible host -s -m shell -a "apt-get install -y curl apt-transport-https"`
1. `ansible host -s -m shell -a "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -"`
1. Add [docker.com](https://docker.com) as new apt repo to the sources list by running this command on all nodes
```
sudo su -
cat <<EOF >/etc/apt/sources.list.d/docker.list
deb https://download.docker.com/linux/$(lsb_release -si | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable
EOF
```
6. `ansible host -s -m shell -a "apt-get update && apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')"`
1. `ansible host -s -m shell -a "curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -"`
1. Add [kubernetes.io](https://kubernetes.io) as new apt repo to the sources list by running this command on all nodes
```
sudo su -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-$(lsb_release -cs) main
EOF
```
9. `ansible host -s -m shell -a "apt-get update && apt-get install -y binutils ebtables socat"`
1. `ansible host -s -m shell -a "apt-get update && apt-get install -y kubernetes-cni kubectl"`
1. `ansible host -s -m shell -a "apt-get update && apt-get install -y autopoint autoconf libtool automake"`
1. `ansible host -s -m shell -a "curl https://gist.githubusercontent.com/lenartj/0b264cb70e6cb50dfdef37084f892554/raw/6ebc9ea54b31e726ed66d68874817d113d218b86/trusty-kubernetes.sh >> /tmp/trusty-kubernetes.sh"`
1. `ansible host -s -m shell -a "chmod a+wx /tmp/trusty-kubernetes.sh"`
1. `ansible host -s -m shell -a "/tmp/trusty-kubernetes.sh | tee /tmp/trusty-kubernetes.log"`
