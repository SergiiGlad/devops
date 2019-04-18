
** Shell Scripts

###### $ export PATH=~/bin:"$PATH" { add new path to $PATH }

The dot (.) command is a synonym for the source command, a shell builtin that reads a
specified file of shell commands and treats it like input from the keyboard.

#### Good Locations for Scripts
The ~/bin directory is a good place to put scripts intended for personal use. If we write
a script that everyone on a system is allowed to use, the traditional location is /usr/
local/bin. Scripts intended for use by the system administrator are often located in /
usr/local/sbin. In most cases, locally supplied software, whether scripts or com-
piled programs, should be placed in the /usr/local hierarchy and not in /bin or /
usr/bin. These directories are specified by the Linux Filesystem Hierarchy Standard
to contain only files supplied and maintained by the Linux distributor.

echo "Would you like to continue? [yes\no]"; read CON; if [ ${CON} != "yes" ]; then echo "Canceled"; else echo "Runnnig..."; fi

##
#!/bin/bash 

number=
if [ $number=1 ]; then echo "Number is equal to 1 "  # [ =1 ]
if [ "$number"=1 ]; then echo "Number is equal to 1" # [ ""=1 ]
# "" prevent empty value

##

[[ -d $myfolder ]] && cd $myfolder && rm * # prevent remove data without cd command
#!/bin/bash -x 
-x debug mode
 
 
