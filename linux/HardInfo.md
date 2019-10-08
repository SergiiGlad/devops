
http://opensource.com/article/19/9/linux-commands-hardware-information

## Hardware overview

```
$ hwinfo --short
```
or

```
$ lshw -short
```

The long full froms but hard to read output 

```hwinfo``` or ```lshw```

## CPU details

```
$ lscpu
```
or
```
# lshw -C cpu

# lshw -C cpu | grep -i mhz

```

## Memory

```
# dmidecode -t memory | grep -i size
```

For more specifics

```
# lshw -short -C memory
```

Video device

```
# lspci | grep -i vga
```

Finally, to show current memory use in megabytes, issue
```
$ free -m
```
or

```
$ top
``` 

## Disks, filesystems, and devices

A single line each disk device
```
# lshw -short -C disk
```

Get specific STA disk, such as model and serial number
```
# hdparm -i /dev/sda
```

List all disks with all their defined partitions
```
lsblk
```
For more detail such as number of sector, size, filesystem ID and type
```
# fdisk -l
````

Print block device attribute like UUID
```
$ blkid
```

To list the mounted filesystem, points and space used

```
$ df -m

```

Finally list details __USB__ and __PCI__
```
$ lspci
$ lsusb
```





