# Getting Started 

You Hex is delivered to you as a fully assembled and completely installed device! There is nothing additional you have to do, but to unbox it and start to use it!

## Powering On

Since the Hex is an electronic device, it benefits from having power. This means you will have to make a connection from your Hex to your wall outlet. An external power supply is provided to make this connection.

1. Plug the round power plug into the Hex. You can find the power jack next to the wireless antenna at the bottom of the device
2. Attach the separate power cord to the power supply. The delivered cord is a regular computer power cord.
3. Plug the power cord into a wall outlet.
4. Once a connection has been made, the 6 white LEDs at the bottom of the Hex light up and the Hex boots.

## Connecting to the WebUI

Pointing your browser to 
```
http://alice-n1.local:7000
```
will present you with a view on your hex. It allows you to install tints and even open a shell to a specific node to enter commands. How is that for power at your fingertips!

## Connecting using SSH

Every node can be addressed using SSH using the **bb** user.

```
my-laptop:> ssh bb@alice-n1.local
```

The password for this user is ```Swh^bdl```.

## Adding a tint to the library
Before we can actually install a new tint, we have to add it to the library inside the hex. At this point tints can only be installed from bitbucket.org (no we don't have shares there), but that will change in the near future. 