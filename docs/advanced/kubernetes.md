# Kubernetes

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) is an open-source system for automating deployment, scaling, and management of containerized applications.

It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon [15 years of experience of running production workloads at Google](http://queue.acm.org/detail.cfm?id=2898444), combined with best-of-breed ideas and practices from the community.

This tutorial will turn your BigBoards Hex or Cube into a Kubernetes cluster using the Kubernetes [custom installation guide](https://kubernetes.io/docs/getting-started-guides/scratch/).

We will be doing this tutorial from the commandline of the master node of your BigBoards device. All commands have to be run from a shell via `ssh bb@<hex>-n1.local`!

## Prerequisites
To complete the tutorial, there are some prerequisites:

1. Do a [factory reset](../hardware/factory-reset.md) of your device.

## Designing the cluster layout
In this guide we will keep the cluster simple: 

1. Each node of your BigBoards device will be a Kubernetes node, incl. the master node.  
1. We will be running the Ubuntu 14.04 LTS version as flashed by BigBoards.
1. Kubernetes has a distinctive [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/) which is, on the 1 hand, conceptually simple from deployment perspective (everything has its own IP address), but, on the other hand, complex from the operations perspective to ensure every address is routable. To keep installation simple, we'll be deploying [Flannel](https://github.com/coreos/flannel#flannel) which is a simple overlay network. We get the ease of software defined networking at the cost of slight loss in performance.
1. We will run docker, kubelet, and kube-proxy outside of a container, the same way we would run any system daemon, so we just need the bare binaries. For etcd, kube-apiserver, kube-controller-manager, and kube-scheduler, we will run these as containers, so will need container images. We will load the images from [Google Container Registry (GCR)](https://gcr.io) such as `gcr.io/google_containers/etcd:2.2.1`.
1. Kubernetes allows you to deploy a fully secured cluster using HTTPS and user credentials to access all resources. To keep it simple, we'll however keep security outside of this installation and use our famous `bb` user to access all services.

## Run the ansible playbook
To automate the installation of Kubernetes on the BigBoards devices, we have wrapped all steps in an ansible playbook.

You can run the ansible playbook either from the master node of you BigBoards device, either from your personal computer if you have [ansible](http://docs.ansible.com/ansible/latest/intro_installation.html) installed.

### From your personal computer
1. Do a GIT checkout from `https://github.com/bigboads/bb-kubernetes.git`
1. Add an inventory for you BigBoards device similar to `./inventories/jill.yml`
1. Run `ansible-playbook -vv -i inventories/<your-inventory>.yml install.yml`

### From your BigBaords device
1. Do a GIT checkout from `https://github.com/bigboads/bb-kubernetes.git`
1. Verify a correct ansible inventory at `/etc/ansible/hosts`; it should be similar to `./inventories/jill.yml`
1. Run `ansible-playbook -vv install.yml`
