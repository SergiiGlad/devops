# Network configuration

https://docs.oracle.com/cd/E52668_01/E54669/html/ol7-netconf.html

File | Desc
 --- | --- 
vi /etc/sysconfig/network-scripts/ifcfg-lo | Configuration file named ifcfg-interface 
vi /etc/hosts | It allows the system to look up (resolve) the IP address of a host given its name, or the name given the IP address. 
vi /etc/nsswitch.conf | The /etc/nsswitch.conf file configures how the system uses various databases and name resolution mechanisms. 
vi /etc/resolv.conf | The /etc/resolv.conf file defines how the system uses DNS to resolve host names and IP addresses. 
vi /etc/sysconfig/network  | The /etc/sysconfig/network file specifies additional information that is valid to all network interfaces on the system. 
`/usr/share/doc/initscripts*/sysconfig.txt` | **see more information**

##### nmcli device status
##### ip addr show

 You can also use ip to set properties and activate a network interface. The following example sets the IP address of the em2 interface and activates it:

##### ip addr add 10.1.1.1/24 dev em2 --
##### ip link set em2 up

### Network Interface Bonding
#### Below are list of modes used in Network Bonding :
  * balance-rr ( round-robin fashion ), 
  * active-backup
  * 802.3ad 
  * broadcast 
  * balance-xor (exclusive-or), 
  * balance-tlb ( Transmit Load Balancing), 
  * balance-alb (Active Load Balancing)

###### # cat /proc/net/bonding/bond0  
For more information see `/usr/share/doc/iputils-*/README.bonding`. 

### Network Interface Teaming
Create a JSON-format definition file for the team and its component ports. For sample configurations, see the files under /usr/share/doc/teamd-*/example_configs/. 
##### teamd -g -f /root/team_config/team0.conf -d

### Configuring VLANs
*To obtain information about the configured VLAN interfaces, view the files in the /proc/net/vlan directory. *

### Network Routing
###### # ip route show
###### # netstat -rn 
###### # lsof -i :22

### Managing Partition Tables Using fdisk

###### # swapoff ----- command to disable the swap partition. 
###### # cfdisk ----- utility, which is a text-based, graphical version of fdisk. 
###### # fdisk -cu /dev/sdc
###### # parted /dev/sda ----- is more advanced than fdisk as it supports more disk label types, including GPT disks, and it implements a larger set of commands. 
###### # kpartx -l system.img ----- mapping partition tables to device

### To view a system's usage of swap space
Creating and Using a Swap File https://docs.oracle.com/cd/E52668_01/E54669/html/ol7-s6-storage.html

###### # cat /proc/swaps
###### # grep Swap /proc/meminfo
###### # free | grep Swap

### File System Administration

T
###### # blkid /dev/sdb1 ------ display the type of a file system, use the blkid command
###### # cat /proc/mounts ------ to display information about mounted file systems
###### # df -h ------ displays information about home much space remains on mounted file 

mount /dev/sdd1 as /test with read-only access and only root permitted to mount or unmount the file system
###### # mount -o nouser,ro /dev/sdd1 /test 

Mount an ISO image file on /mount/cdrom with read-only access by using the loop device:
###### # mount -o ro,loop ./OracleLinux-R6-U1-Server-x86_64-dvd.iso /media/cdrom

Remount the /test file system with both read and write access, but do not permit the execution of any binary files that are located in the file system:
###### # mount -o remount,rw,noexec /test

A loop device allows you to access a file as a block device. For example, to mount a file that contains a DVD ISO image on the directory mount point /ISO:
###### # mount -t iso9660 -o ro,loop /var/ISO_files/V33411-01.iso /ISO

### Creating a File System on a File

###### # dd if=/dev/zero of=/fsfile bs=1024 count=1000000 
###### # mkfs.ext4 -F /fsfile 
###### # mount -o loop /fsfile /mnt

###### # umount filesystem ------ Unmount the file system:
###### # fsck [-y] filesystem ------ Use the fsck command to check the file system
###### # ls /sbin/mkfs.* ------ see which file system os support
###### # mount -t cifs //server_name/share_name mountpoint -o sec=krb5

### Shutdown and reboot
# Make the user sudo with appropriate permissions on the commands required.
– Edit the file /etc/sudoers using the command “visudo”.

###### # systemctl reboot
###### # init 5
###### # reboot
###### # shutdowm -r
###### # poweroff


### About Authentication

1. Local files 
  * /etc/passwd 
  * /etc/shadow files
2. on remote systems using 
  * Identity Policy Audit (IPA), 
  * the Lightweight Directory Access Protocol (LDAP), 
  * the Network Information Service (NIS), 
  * Winbind.
  
  
  
 ### Local Account Configuration
 
The default settings are stored in the /etc/default/useradd file. 
###### # useradd -D ------ To display the default settings for an account 
###### echo "username:password" | chpasswd ------ change the password non-interactively (for example, from a script)
###### # passwd -l username ------ To lock a user's account
###### # passwd -u username ------ To unlock the account

### About umask and the setgid and Restricted Deletion Bits

###### # chgrp groupname directory
###### # chmod g+s directory ------ set the setgid bit on the directory
###### # chmod a+t directory ------ To set the restricted deletion bit on a directory
###### # usermod -aG groupname username ------ to add a user to a supplementary group (other than his or her login group)
###### # groups root ------ to display the groups to which a user belongs
###### # userdel username ------ To delete a user's account
###### # groupadd -g 1000 devgrp ------ greate a group
###### # groupmod [options] username ------ To modify a group
###### # groupdel username ------ To delete a user's account
###### # usermod -f 30 username ------ how long a user's account can be inactive before it is locked
###### # visudo ------ command to modify the /etc/sudoers file.


###### # rpm -qf /bin/ls {this would tell about the package to which this command (binary file) belongs to if installed by that package}

###### # find / -type f -perm -4000 2>/dev/null | xargs ls -l { to list all the files with SUID (Set User ID) bit set }

###### # find / -type f -perm /7000 2>/dev/null | xargs ls -l { to list all the files/folders with SUID/SGID/Sticky Bit (Set Group ID) bit set }

###### #ethtool -s eth0 speed 100 autoneg off duplex full {changing the speed on the fly}

#### How do you check the network routing table using commands?

###### # route -n
###### # netstat -nr
###### # ip route

#### Special Permissions 

##### SETUID
The binary file with the **setuid permission** is "run as" the owner of the file
###### # chmod u+s file { To add the setuid permission symbolically }
###### # chmod 4775 file { To add the setuid permission numerically, add 4000 }
###### chmod u-s file or chmod 0775 file { to remove }

#### SETGID
The setgid permission on a File is similar to setuid
-rwxr-**s**r-x. 1 root **tty** 10996 Jul 19  2011 /usr/bin/wall
crw--w----. 1 root tty  4, 0 Mar 29  2013 /dev/tty0

The setgid Permission on a Directory
Creates a new group called team.
###### # sudo chmod g+s /home/team  { setgid causes files created in the directory to automatically be owned by the group that owns the directory. To add the setgid permission numerically, add 2000  }

#### Sticky Bit Permission
The sticky bit permission is used to prevent other users from deleting files that they do not own in a shared directory. 
###### # chmod o+t <directory> { To set the sticky bit permission numerically, add 1000 }











