# (Very) Frequently Asked Questions

## There seems to be something wrong with the design of the Hex. There is a big hole in the middle.

Well, we actually did that on purpose. All though we are using low-power ARM based computing units which produce a significant less amount of heat then their intel based counterparts, there still is some heat we need to get rid of. The hole in the middle of the Hex serves as a chimney, making use of natural air convection to evacuate hot air out of the Hex from the top and sucking in cool air from the bottom. Pretty neat, right?

## Why do you use ARM technology?

By using ARM technology, we are able to keep the energy consumption as low as possible. Did you know the Hex only consumes 48 Watts when under load?

## There is only 2GB of RAM on each node. Isn't that too low to work with Big Data technologies?

Currently we are limited to 2GBs of RAM because there aren't any SoC boards readily available with more RAM. Even then, since 64bit ARM CPU's aren't around yet, you are limited to less then 4Gb. Eventually we want to have as much memory as possible, but this is limited to what we can get from the suppliers.

That being said, almost all Big Data technologies can run on a Hex. The only thing you need to keep in mind is the size of the dataset you are processing.

## Doesn't ARM need specific packages?

Indeed, packages built for ARM differ from the ones being build for x86. However, a lot of them are already available.
