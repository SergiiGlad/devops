
http://opensource.com/article/19/9/linux-commands-hardware-information

## Hardware overview

```
$ hwinfo --short
```
or

```
$ lshw -short
```

The long full forms but hard to read output 

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
$ lsblk
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

## Network

To see hardware details about your network card
```
# lshw -C network
```

Traditionally
```
$ ifconfig -a
```

Many people use
```
$ ip link show
```
or
```
$ netstat -i
```

To show your default gateway and routing tables
```
$ ip route | column -t
```
or
```
$ netstat -r
```

## Software

UEFI or BIOS date and version
```
# dmidecode -t bios
```

Kernel version
```
$ uname -a
```



