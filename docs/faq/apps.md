## Why don't you just use plain ansible playbooks?
We want to make it as easy as possible for people to create their own tints. We started out with plain ansible playbooks but we saw we were doing the same things over and over again. We decided to simplify the process by taking out the repetitive work, ending up with some sort of descriptive model of what a tint should be.

## My app isn't installing, I'm not even getting any task output!
This is one we ran into ourselfs quite frequently. It is probably caused by some step in the tint installation process asking for user input. 

One of the usual suspects is the git checkout task. If the git repository defined in the tint metadata is private, cloning it means you'll have to enter a password. For now there is no other way around it than to make the repository public.