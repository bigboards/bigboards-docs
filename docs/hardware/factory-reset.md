# Factory reset
This page describes how to uninstall the BigBoards firmware by doing a factory reset. 

> **Warning** 
>
> A factory reset brings your system back to its initial state. To reinstall 
> the BigBoards firmware, your must [boostrap](../software/bootstrap.md) and [link](../software/link.md) 
> your device again.

## Why?
A factory reset might be useful if you want to run a different operating environment 
to manage your installed services, e.g. in case you want to 

* run a commercial Hadoop distributions like 
  [Cloudera](https://cloudera.com), [MapR](https://mapr.com) or 
  [Hortonworks](https://hortonworks.com)
* turn your device in micro-cloud by installing 
  [OpenStack](https://openstack.org)
* run all your apps on a container 
  service like [Docker Swarm](https://docs.docker.com/engine/swarm/) 
  or [Kubernetes](https://kubernetes.io/) 

> **Warning** 
>
> Installing an alternative operating environment is a great way to learn 
> commercial software solutions, but can obviously not be supported by BigBoards! 
>
> If you have issues with such installations, you have to seek help via the 
> solution provider's own support channels. 

## Preflight checks
Before you perform the factory reset, verify that 

1. You have uninstalled any app from your device, preferably via the MMC, if necessary via the CLI `bb system purge`
1. Make sure your device in on the latest firmware version by running `bb firmware update` 

## Procedure

To uninstall the BigBoards firmware, simply run 

```
bb hardware reset
```