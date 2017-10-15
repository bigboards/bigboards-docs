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

## Preparing your desktop
As you will be commandeerig your Kubernetes cluster from your desktop, you have to
[install and configure the Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

## Preparing the cluster layout
In this guide we will keep the cluster simple: 

1. Each node of your BigBoards device will be a Kubernetes node, incl. the master 
   node.  
1. We will be running the Ubuntu 14.04 LTS version as flashed by BigBoards.
1. Kubernetes has a distinctive [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
   which is, on the 1 hand, conceptually simple from deployment perspective (everything has 
   its own IP address), but, on the other hand, complex from the operations perspective
   to ensure every address is routable. To keep installation simple, we'll be deploying 
   [Flannel](https://github.com/coreos/flannel#flannel) which is a simple overlay network. 
   We get software defined networking at the cost of slight loss in performance.
   > Ideally we would have networking handled as cloase to the hardware and OS level 
   > as possible. This should be feasible via [SR-IOV](https://en.wikipedia.org/wiki/Single-root_input/output_virtualization) 
   > on the NIC, the [Kubernetes CNI plugin](https://kubernetes.io/docs/concepts/cluster-administration/network-plugins/#cni)
   > and the [sriov-cni implementation](https://github.com/hustcat/sriov-cni).  
   
   
  
 