# Getting Started 

To get you up and going as fast as possible, here are the steps you need to take:

 1. Plug in power and network
 2. Connect your browser to `http://<hex-name>.hex.bigboards.io:7000/`
 3. Install a tint from the library 

There are two versions of the hardware device so the installation procedure differs a bit depending on the version you have.
 
## Getting started with a cube
The power connector for the cube is a round DIN4 connector and you will have to press it in 
firmly for the device to start. The supplied power supply can be used for any AC voltage 
between 110V and 230V, so you will be able to use it close to anywhere on the planet.

## Getting started with a hex

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