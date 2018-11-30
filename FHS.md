

### l[ Filesystem Hierarchy Standard ](http://refspecs.linuxfoundation.org/FHS_2.3/fhs-2.3.html#VARRUNRUNTIMEVARIABLEDATA "FHS" )


##### FHS categories
  Name | Shareable |	Unshareable
 --- | --- | ---
Static 	| /usr /opt 	| /etc /boot
Variable 	| /var/mail /var/spool/news | /var/run /var/lock


Directory 	| Purpose
--- | ---
bin 	| Essential command binaries
boot 	| Static files of the boot loader
dev 	| Device files
etc 	| Host-specific system configuration
lib 	| Essential shared libraries and kernel modules
media |	Mount point for removable media
mnt 	| Mount point for mounting a filesystem temporarily
opt 	| Add-on application software packages
run 	|
sbin 	| Essential system binaries
srv 	| Data for services provided by this system
tmp 	| Temporary files
usr 	| Secondary hierarchy
var 	| Variable data
home 	| User home directories (optional)


Directory 	| Purpose of Directory
--- | ---
/ 	| The base of the structure, or root of the filesystem, this directory unifies all directories regardless of if they are local partitions, removable devices or network shares
/bin |	To hold essential binaries like the ls, cp, and rm commands, and be a part of the root filesystem.
/boot |	Holds files necessary to boot the system such as the Linux kernel and associated configuration files
/dev 	| Populated with files that represent hardware devices and other special files, such as the /dev/null and /dev/zero files
/etc 	| Contain essential host configurations files such as the /etc/hosts or /etc/passwd files
/home |	The location of user home directories
/lib 	| The essential libraries to support the executable files in the /bin and /sbin directories
/lib<qual> 	| Essential libraries built for a specific architecture. For example, the /lib64 directory for 64 bit AMD/Intel x86 compatible processors
/media 	| The mount point for removable media mounted automatically
/mnt 	| A mount point for temporarily mounting filesystems manually
/opt 	| Optional third party software installation location
/proc 	| A virtual filesystem for the kernel to report process and other information
/root 	| The home directory of the root user
/sbin 	| The essential system binaries primarily used by the root user
/sys 	| A virtual filesystem holding information about hardware devices connected to the system
/srv 	| Location where site specific services may be hosted
/tmp 	| Directory where all users are allowed to create temporary files that is supposed to be cleared at boot time (but often is not)
/usr 	| Second hierarchy of non-essential files for multi-user use.
/usr/local |	Third hierarchy of files for software not originating from distribution
/var 	| The /var hierarchy contains files that change over time
/var/cache |	Files used for caching application data
/var/log 	| Directory where most log files are kept
/var/lock |	Where lock files are kept for shared resources
/var/spool |	Where spool files for printing and mail are stored
/var/tmp |	Temporary files to be preserved between reboots


Directory 	| Purpose of Directory
--- | ---
/usr/bin |	Binaries for ordinary user, used when the system is in multiuser mode
/usr/include |	Files to be included to compile software from distribution
/usr/lib 	| Libraries to support the executable files in the /usr/bin and /usr/sbin directories
/usr/lib<qual> |	Non-essential libraries built for a specific architecture
/usr/libexec	| Executable programs to be used by other programs and not directly by users
/usr/sbin 	| System binaries for use by administrator in multiuser mode
/usr/share 	| Where software documentation and other application data is stored
/usr/src 	| The source code for compiling the kernel

Directory 	| Purpose of Directory
--- | ---
/usr/local/bin | 	Local software binaries for ordinary user use
/usr/local/etc |	Local software configuration files
/usr/local/include |	Files that need to be included in order to compile local source code
/usr/local/lib 	| Library files to support the executable files in the /usr/local/bin and /usr/local/sbin directories
/usr/local/libexec 	| Local executable programs to be used by other programs and not directly by users
/usr/local/sbin 	| Local binaries for system administrator use
/usr/local/share 	| Where local software man pages, information pages, and other local application information is stored
/usr/local/src 	| The location where source code for software to be compiled locally is often placed


