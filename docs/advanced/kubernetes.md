# Kubernetes

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) is an open-source system for automating deployment, scaling, and management of containerized applications.

It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon [15 years of experience of running production workloads at Google](http://queue.acm.org/detail.cfm?id=2898444), combined with best-of-breed ideas and practices from the community.

This tutorial will turn your BigBoards Hex or Cube into a Kubernetes cluster [using kubeadm to create a cluster](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/).

We will be doing this tutorial from the commandline of the master node of your BigBoards device. All commands have to be run from a shell via `ssh bb@<hex>-n1.local`!

## Prerequisites
To complete the tutorial, there are some prerequisites:

1. Because Kubernetes is not supported on Ubuntu 14.04, i.e. the BigBoards firmware, you have to [install an alternative Linux operating system](../hardware/install-alt-os.md). We prefer [Ubuntu LTS](https://wiki.ubuntu.com/LTS) release.
1. Make a short list of the host names of your BigBoards device, with the network MAC addresses and product_uuids `cat /sys/class/dmi/id/product_uuid`. Here's an example for 1 of our Cubes Jill.   

|host   |MAC              |product_uuid                        |
|-------|-----------------|------------------------------------|
|jill-n1|b8:ae:ed:78:dc:7b|DB780F00-7277-11E3-BE96-B8AEED78DC7B|
|jill-n2|b8:ae:ed:78:dc:62|DB780F00-7277-11E3-BFF1-B8AEED78DC62|
|jill-n3|b8:ae:ed:78:d9:aa|D5822E00-7277-11E3-B10F-B8AEED78D9AA|

## Designing the cluster layout
In this guide we will keep the cluster simple: 

1. Each node of your BigBoards device will be a Kubernetes node, incl. the master node.  
1. We will be running the Ubuntu 16.04 LTS version.
1. Kubernetes has a distinctive [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/) which is, on the 1 hand, conceptually simple from deployment perspective (everything has its own IP address), but, on the other hand, complex from the operations perspective to ensure every address is routable. To keep installation simple, we'll be deploying [Flannel](https://github.com/coreos/flannel#flannel) which is a simple overlay network. We get the ease of software defined networking at the cost of slight loss in performance.

## Installing kubernetes
We have automated the installation of Kubernetes on your BigBoards device using [Ansible](https://ansible.com). 

Check the [installation instructions](http://docs.ansible.com/ansible/latest/intro_installation.html) to get the latest version installed on your personal computer. 

You can also install Ansible on the master node of you cluster and run all the playbooks underneath from the shell there.

1. Checkout the [GitHub repository](https://github.com/bigboards/bb-kubernetes)
1. Change directory to the folder with the local repository
1. Add an inventory `./inventories/<hex-name>.yml` with the layout of your BigBoards device. Look at `jill.yml` as an example.
1. Run `ansible-playbook -vv -i inventories/<hex-name>.yml install.yml`


