# Apps
While having hardware is one thing, data processing today is mostly defined by the used technologies. 
The software layer is meant to work with *apps*, collections of technologies brought together for
a specific purpose. Popular apps are *Spark on Yarn* or *ElasticSearch with Kibana*.

It is really simple to install an app onto a device. Just go to the device web interface,
select the one you want from the library, grab a coffee and when you get back your environment will
be waiting for you.

**Only one app can be installed at any moment in time.**
If you want to use an other app, first remove the installed one if there is one, then install the new one.

If the stack you want to use is not in the library yet, you can create your own using our central platform.

## App Scope
An app can be declared public or private. Public apps are visible to anyone using the bigboards platform
while private apps can only be installed, modified or used by the owner. You can add collaborators to a
private app so you can share even a private app between a limited number of people.

The app scope is only used for the definition of the tint. The configuration part of the tint has to
reside inside a *public* git repo. A private docker registry can be used but has to be configured on
each device on which the app is installed.

