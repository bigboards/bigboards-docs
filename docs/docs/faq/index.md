# Networking
## How do I change the internal network address?
Have a look at the ```bb switch network``` command. By running that on the first node of your hex you can change the internal address of all nodes inside the hex.

# Tints
## Why don't you just use plain ansible playbooks?
We want to make it as easy as possible for people to create their own tints. We started out with plain ansible playbooks but we saw we were doing the same things over and over again. We decided to simplify the process by taking out the repetitive work, ending up with some sort of descriptive model of what a tint should be.