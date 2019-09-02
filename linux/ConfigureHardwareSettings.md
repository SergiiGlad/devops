## Virtual files for hardware and system information

### Sysfs and /sys

__Sysfs__ is a virtual filesystem that the Linux kernel uses. to export information about kernel objects to processes in user space.

Entry in /etc/fstab
```  
mount -t sysfs sysfs /sys
```  

```ls /sys/bloc``` you find your block devices

```tree /sys/bloc``` is a useful tool for exploring /sys
