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

## Preparing kubectl
We will be commandeering the Kubernetes cluster from the master node of your BigBoards device. Therefor, we need to install ``kubectl`` as described at [install and configure the Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

1. `curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`
1. `chmod +x ./kubectl`
1. `sudo mv ./kubectl /usr/local/bin/kubectl`
1. `kubectl version` 
1. `kubectl config set-cluster <hex-name> --server=http://<hex-name>-n1.local --insecure-skip-tls-verify=true`
1. `kubectl config set-context <hex-name> --cluster=<hex-name> --user=admin`
1. `kubectl config set-credentials admin --username=bb`
1. `kubectl config use-context <hex-name>`
1. `kubectl config view`
1. `ansible host -s -m file -a "path=/etc/kubernetes state=directory mode=0755"`
1. `ansible host -s -m file -a "path=/var/lib/kube-proxy state=directory mode=0755"`
1. `ansible host -s -m file -a "path=/var/lib/kubelet state=directory mode=0755"`
1. `ansible host -s -m copy -a "src=~/.kube/config dest=/var/lib/kube-proxy/kubeconfig mode=0644"`
1. `ansible host -s -m copy -a "src=~/.kube/config dest=/var/lib/kubelet/kubeconfig mode=0644"`

## Install docker

To [Install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) on all nodes 

1. `ansible host -s -m shell -a "apt-get remove docker docker-engine docker.io"`
1. `ansible host -s -m shell -a "apt-get update"`
1. `ansible host -s -m shell -a "apt-get -y upgrade"`
1. `ansible host -s -m shell -a "apt-get -y autoremove"`
1. `ansible host -s -m shell -a "apt-get -y install linux-image-extra-$(uname -r) linux-image-extra-virtual"`
1. `ansible host -s -m shell -a "apt-get -y install apt-transport-https ca-certificates curl software-properties-common"`
1. `ansible host -s -m shell -a "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"`
1. `ansible host -s -m shell -a "add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'"`
1. `ansible host -s -m shell -a "apt-get -y update"`
1. `ansible host -s -m shell -a "apt-get -y install docker-ce"`
1. `ansible host -s -m shell -a "docker run hello-world"`

## Install Kubernetes binaries 
A Kubernetes binary release includes all the Kubernetes binaries as well as the supported release of etcd. 

To [Install Kubernetes binaries](https://kubernetes.io/docs/getting-started-guides/scratch/#downloading-and-extracting-kubernetes-binaries)

1. `URL=$(curl -w "%{url_effective}\n" -I -L -s -S https://github.com/kubernetes/kubernetes/releases/latest -o /dev/null)`
1. `K8S_VERSION=$(basename $URL)`
1. `curl -L https://github.com/kubernetes/kubernetes/releases/download/${K8S_VERSION}/kubernetes.tar.gz > /tmp/kubernetes.tar.gz`
1. `tar -xvzf /tmp/kubernetes.tar.gz -C /tmp/`
1. `export KUBERNETES_SKIP_CONFIRM=true`
1. `/tmp/kubernetes/cluster/get-kube-binaries.sh`
1. `tar -xvzf /tmp/kubernetes/server/kubernetes-server-linux-amd64.tar.gz -C /tmp/`
1. `ansible host -s -m file -a "path=/opt/k8s/${K8S_VERSION} state=directory mode=0755"`
1. `ansible host -s -m copy -a "src=/tmp/kubernetes dest=/opt/k8s/${K8S_VERSION} mode=0644"`
1. `ansible host -s -m file -a "path=/opt/k8s/kubernetes src=/opt/k8s//${K8S_VERSION} state=link mode=0644"`

## Activate Kubernetes services
Now that we have installed the Kubernetes binaries, we have to run the necessary daemons as system services. 

The approash was inspired by [trusty-kubernetes.sh](https://gist.github.com/lenartj/0b264cb70e6cb50dfdef37084f892554) 

1. generate the /etc/kubernetes/.conf files
```bash
cat >/tmp/kube.conf <<EOF
KUBE_LOGTOSTDERR="--logtostderr=false"
KUBE_LOG_LEVEL="--v=4"
KUBE_MASTER="--master={{ ansible_hostname }}-n1:8080"
KUBE_ALLOW_PRIV="--allow-privileged=false"
EOF
``` 

```bash
cat >/tmp/kubelet.conf <<EOF
KUBELET_ADDRESS="--address=0.0.0.0"
KUBELET_PORT="--port=10250"
KUBELET_HOSTNAME="--hostname-override={{ inventory_hostname }}"
KUBELET_API_SERVER="--api-servers=http://{{ ansible_local.bb.hex.id }}-n1:8080"

KUBELET_KUBECONFIG_ARGS="--kubeconfig=/var/lib/kubelet/kubeconfig --require-kubeconfig=true"
KUBELET_SYSTEM_PODS_ARGS="--pod-manifest-path=/etc/kubernetes/manifests"
KUBELET_NETWORK_ARGS="--register-node --configure-cbr0=true --node-ip={{ hostvars[ansible_hostname]['ansible_' + ansible_local.bb.node.nic_ext].ipv4.address }}"
KUBELET_DNS_ARGS="--cluster-dns={{ ansible_local.bb.hex.id }}-n1 --cluster-domain={{ ansible_local.bb.hex.id }}.k8s.local"
KUBELET_AUTHZ_ARGS="--authorization-mode=AlwaysAllow"
EOF
``` 

```bash
cat >/tmp/kube-proxy.conf <<EOF
KUBE_PROXY_ARGS=""
EOF
``` 

2. generate the /etc/init/.conf files
```bash
cat >/tmp/kubelet.init.conf <<EOF
description "Kubelet"

start on (docker)
stop on runlevel [!2345]

limit nproc unlimited unlimited

respawn
kill timeout 30

script
    if [ -f /etc/kubernetes/kube.config ]; then
        . /etc/kubernetes/kube.config
    fi

    if [ -f /etc/kubernetes/kubelet.conf ]; then
            . /etc/kubernetes/kubelet.conf
    fi
        
    exec /usr/bin/kubelet \
        $KUBE_LOGTOSTDERR \
        $KUBE_LOG_LEVEL \
        $KUBELET_API_SERVER \
        $KUBELET_ADDRESS \
        $KUBELET_PORT \
        $KUBELET_HOSTNAME \
        $KUBE_ALLOW_PRIV \
        $KUBELET_KUBECONFIG_ARGS 
        $KUBELET_SYSTEM_PODS_ARGS \
        $KUBELET_NETWORK_ARGS \
        $KUBELET_DNS_ARGS \
        $KUBELET_AUTHZ_ARGS \
        $KUBELET_EXTRA_ARGS
end script
EOF
``` 

```bash
cat >/tmp/kube-proxy.init.conf <<EOF
description "KubeProxy"

start on (filesystem and net-device-up IFACE!=lo)
stop on runlevel [!2345]

limit nofile 65536 65536

respawn
kill timeout 30

script
    if [ -f /etc/kubernetes/kube.config ]; then
        . /etc/kubernetes/kube.config
    fi

    if [ -f /etc/kubernetes/kube-proxy.conf ]; then
            . /etc/kubernetes/kube-proxy.conf
    fi
        
 exec /usr/bin/kube-proxy \
    $KUBE_LOGTOSTDERR \
    $KUBE_LOG_LEVEL \
    $KUBE_MASTER \
    $KUBE_PROXY_ARGS
end script
EOF
``` 

3. Copy init.conf files
    1. `ansible host -s -m template -a "src=/tmp/kube.conf dest=/etc/kubernetes/kube.conf mode=0644"`
 