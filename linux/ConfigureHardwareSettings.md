https://developer.ibm.com/tutorials/l-lpic1-101-1/

## Virtual files for hardware and system information

### Sysfs and /sys

__Sysfs__ is a virtual filesystem that the Linux kernel uses. to export information about kernel objects to processes in user space.

Entry in /etc/fstab
```  
mount -t sysfs sysfs /sys
```  

```ls /sys/bloc``` you find your block devices

```tree /sys/bloc``` is a useful tool for exploring /sys


### procfs and /proc

The procfs filesystem provides insight into many of the kernel data structures and even allows a few to be changed on the fly.


Showing /proc entries for the current process ($$)
```
ls -l /proc/$$/
```

The parameters taht you can control by setting values in the procfs filesystem can also be controlled vi the ```sysctl``` command.

The procfs filesystem also provides information about interrupt, Direct Memory Access (DMA), and I/O port resiurces used by your system

Listing of 
```
cat /proc/interrupts

cat /proc/dma

cat /proc/ioports
```

The procinfo package contains the ```lsdev``` command, which summarizes info from /proc


### udev and /dev

__udev__ is responsible for the dynamic device management needed for hot plugging devices.

## Tools and utilities

Some useful tools are available for determinig information about your PCI and USB devices.
Let's look at ```lspci``` and ```lsusb```

__D-Bus__ (also known as __dbus__) is a message-passing bus developed under the auspices of freedesk-top.org. A single system daemon allows communication between the kernel and user space for events such as new hardware found.

## Kernel modules

Several command are used for interrogating and manipulating kernel modules
```
lsmod

modinfo vfat

modprobe
```

Location module files on your system
```
ls /lib/modules/$(uname -r)
```


