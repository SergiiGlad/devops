
** Shell Scripts

If __bash__ is invoked with the name __sh__ as an interactive login shell
it first attempts to read and execute commands from _/etc/profile_ and _~/.profile_ , in that order.

__Bash__ as an interactive login shell, or as a non-interactive shell with the --login option:
 * /etc/profile  
 *  ~/.bash_profile 
 * ~/.bash_login
 * ~/.profile
  in  that  order if the files exists

When a login shell exits, bash reads and executes commands from the files 
 * ~/.bash_logout 
 * /etc/bash.bash_logout 
if the files exists.

## FILES
```/bin/bash``
   The bash executable

```/etc/profile```
   The systemwide initialization file, executed for login shells

```/etc/bash.bash_logout```
   The systemwide login shell cleanup file, executed when a login shell exits

```~/.bash_profile```
   The personal initialization file, executed for login shells

```~/.bashrc```
   The individual per-interactive-shell startup file

```~/.bash_logout```
   The individual login shell cleanup file, executed when a login shell exits

```~/.inputrc```
   Individual readline initialization file


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
 
 
