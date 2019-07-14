# Kubernetes

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) is an open-source system for automating deployment, scaling, and management of containerized applications.

Kubernetes is often abbreviated to **k8s**.

Kubernetes groups containers that make up an application into logical units for easy management and discovery. It builds upon [15 years of experience of running production workloads at Google](http://queue.acm.org/detail.cfm?id=2898444), combined with best-of-breed ideas and practices from the community.

This tutorial will turn your BigBoards Hex or Cube into a Kubernetes cluster [using kubeadm to create a cluster](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/).

We will be doing this tutorial from the commandline of the master node of your BigBoards device. All commands have to be run from a shell via `ssh bb@<hex>-n1.local`!



## Objectives
1. Install a **secure Kubernetes cluster** on your BigBoards device
1. Install a **pod networking** on the cluster so that application components (pods) can talk to each other
1. Install a **sample application** on the cluster



## Prerequisites
To complete the tutorial, there are some prerequisites:

1. Since the BigBoards firmware runs on top of Ubuntu 14.04 which is not supported by Kubernetes, you have to [install an alternative Linux operating system](../hardware/install-alt-os.md). We prefer [Ubuntu LTS](https://wiki.ubuntu.com/LTS) releases.
1. Make a short list of the host names of your BigBoards device, with the network MAC addresses and product_uuids `cat /sys/class/dmi/id/product_uuid`. Here's an example for 1 of our Cubes Jill.   

|host   |MAC              |product_uuid                        |
|-------|-----------------|------------------------------------|
|jill-n1|b8:ae:ed:78:dc:7b|DB780F00-7277-11E3-BE96-B8AEED78DC7B|
|jill-n2|b8:ae:ed:78:dc:62|DB780F00-7277-11E3-BFF1-B8AEED78DC62|
|jill-n3|b8:ae:ed:78:d9:aa|D5822E00-7277-11E3-B10F-B8AEED78D9AA|



## Designing the cluster layout
In this guide we will keep the cluster simple: 

1. We will be running the Ubuntu 16.04 LTS version.
1. Kubernetes has a distinctive [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/) which is, on the 1 hand, conceptually simple from deployment perspective (everything has its own IP address), but, on the other hand, complex from the operations perspective to ensure every address is routable. To keep installation simple, we'll be deploying [Flannel](https://github.com/coreos/flannel#flannel) which is a simple overlay network. We get the ease of software defined networking at the cost of slight loss in performance.
1. Each node of your BigBoards device will be a Kubernetes node, incl. the master node.
1. The 1st node of you BigBoards device will be the master of the Kubernetes cluster.   



## Installing kubernetes and initializing the master node
We have automated the installation of Kubernetes on your BigBoards device using [Ansible](https://ansible.com). 

Check the [installation instructions](http://docs.ansible.com/ansible/latest/intro_installation.html) to get the latest version installed on your personal computer. 

You can also install Ansible on the master node of you cluster and run all the playbooks underneath from the shell there.

1. Checkout the [GitHub repository](https://github.com/bigboards/bb-kubernetes)
1. Change directory to the folder with the local repository
1. Add an inventory `./inventories/<hex-name>.yml` with the layout of your BigBoards device. Look at `jill.yml` as an example.
1. `$ ansible-playbook -vv -i inventories/<hex-name>.yml install.yml`

Check that all deployed system pods start properly, especially `kube-system/kube-dns`

```bash
$ kubectl get pods --all-namespaces
```



## Join worker nodes

The final output of the playbook will be the command to join the worker nodes to the Kubernetes cluster. 

```bash
$ ansible host-workers -s -i inventories/<hex-name>.yml -m shell -a 'kubeadm join --token <token> <master-ip>:<master-port> --discovery-token-ca-cert-hash sha256:<hash>'
```



## Install dashboard
Kubernetes Dashboard is a general purpose, web-based UI for Kubernetes clusters. It allows users to manage applications running in the cluster and troubleshoot them, as well as manage the cluster itself.

![Kubernetes dashboard](k8s-dashboard-ui.png)

To install

```bash
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
```



## Deploy sample application
Now it is time to take your new cluster for a test drive. 

Sock Shop is a sample microservices application that shows how to run and connect a set of services on Kubernetes. 

To learn more about the sample microservices app, see the [GitHub README](https://github.com/microservices-demo/microservices-demo).

Note that the Sock Shop demo only works on `amd64`.

```bash
$ kubectl create namespace sock-shop
$ kubectl apply -n sock-shop -f "https://github.com/microservices-demo/microservices-demo/blob/master/deploy/kubernetes/complete-demo.yaml?raw=true"
```
You can then find out the port for the front-end service by running:

```bash
$ kubectl -n sock-shop get svc front-end
NAME        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
front-end   10.110.250.153   <none>       80:30001/TCP   59s
```

It takes several minutes to download and start all the containers. 

Watch the output of `kubectl get pods -n sock-shop` to see when they’re all up and running.

Then go to the IP address of your cluster’s master node in your browser, and specify the given port. 

So for example, `http://<master_ip>:<port>`. In the example above, this was `http://10.110.250.153:30001`, but it may be a different port for you.



## Uninstall sampe application
To uninstall the socks shop, run this on the master.

```bash
$ kubectl delete namespace sock-shop
```


## Tear down
To undo what kubeadm did, you should first [drain the node](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#drain) and make sure that the node is empty before shutting it down.
Talking to the master with the appropriate credentials, run:

```
$ kubectl drain <node name> --delete-local-data --force --ignore-daemonsets
$ kubectl delete node <node name>
```

Then, on the node being removed, reset all kubeadm installed state:
```
$ kubeadm reset
```

If you wish to start over simply run `kubeadm init` or `kubeadm join` with the appropriate arguments.
