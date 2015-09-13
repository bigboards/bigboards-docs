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
http://<hex-name>.hex.bigboards.io:7000/
```
will present you with a view on your hex. It allows you to install tints and even open a shell to a specific node to enter commands. How is that for power at your fingertips!

## Connecting using SSH

Every node can be addressed using SSH using the **bb** user.

```
my-laptop:> ssh bb@<hex-name>.hex.bigboards.io
```

The password for this user is ```Swh^bdl```.

## Installing a tint from the library
The library is prefilled with available Tints for your Hex. Just go to 

````
http://<hex-name>.hex.bigboards.io:7000/#/library
````

to choose the Tint you want to install. Click on it, to get to the details. Click ont he Install button to install it on your Hex.