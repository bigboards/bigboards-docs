# Generating and burning SD cards

## Generating
```
sudo mount /dev/sdb1 /media/bbfs
sudo mount --rbind /sys /media/bbfs/sys
sudo mount --rbind /dev /media/bbfs/dev
sudo mount --rbind /proc /media/bbfs/proc
sudo chroot /media/bbfs /bin/bash
```

Next install all the packages you like and change the files you need to be changed. Make sure you install a bootloader (in case of the x86 version)

```
sudo apt-get install ...
```

CTRL-D out of the chroot jail and generate the image
```
$ <CTRL-D>
$ umount -l /media/bbfs/sys
$ umount -l /media/bbfs/dev
$ umount -l /media/bbfs/proc
$ sudo rm -rf bbfs/var/cache/apt/archives/*.deb
$ sudo rm -rf bbfs/var/cache/apt/archives/partials/*.deb
$ sudo rm -rf bbfs/var/cache/apt/archives/partial/*.deb

$ sudo tar --numeric-owner -C bbfs -cz -f ~/bigboards-core-14.04.2-core-amd64.tar.gz . 
```
