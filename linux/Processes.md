## Linux processes

The kernel assigns a unique ID number to every process **PID** process ID number
 
When a process is cloned, the original process is referred to as the parent, and the copy is called the child **PPID** parent PID

A process's UID is the user identification number of the person who created it **UID** user ID

Foor most processes the UID and EUID are the same **EUID** effective user ID

**GID and EGID** real and effective group ID

### Niceness

A process's scheduling priority determines how much CPU time it receives

#### NICE AND RENICE

The most common range is -20 to +19
A low or negative value means high priority

Run with modified scheduling priority ```nice -n 5 /bin/dockerd```
Alter priority ```renice -5 8829```

### The life cycle of a process

To create a new process, a process copies itself with the **fork** system call.
After a fork, the child process will often usse one of the **exec** family of system calls to begin the execution of a new program.

##### By convention, 0 is used to indicate a normal of "successful" termination

### Signals

Signals are process-level interrupt requests

A list of signals names and number is also available from the bash built-in command ```kill -l```

### KILL:SEND SIGNALS

The ```kill``` command is most often used to terminate a process
``` kil -9 pid``` kill send signal

```killall httpd``` kills processes by name

```pgrep``` and ```pkill``` search for proccesses by name

### PPROCESS STATES

 * Runnable
 * Sleeping
 * Zombie
 * Stopped

### MONITORING PROCESSES

__ps__ is the system admin tool for monitoring processes

```ps aux``` output on a machine

```ps lax``` is also slightly faster to run than ps aux because it doesn't have to tranclate every UID to a username

```ps -ef``` is a good place to start

```ps -elf``` shows additional gory details

### Dynamic monitoring 

```top``` is a free utility that runs on many systems and provides a regularly updated summary of active processes

### The /PROC filesystem

The Linux versions of __ps__ and __top__ read their process status information from the __/proc__ directory, a pseudo-filesystem in which the kernek exposes a variety of interesting information about the system's state

### TRACE SIGNALS AND SYSTEM CALLS

Linux lets you directly observe a process with the  __strace__ command, which shows every system call the process makes and every signal it receives

### RUNAWAY PROCESSES

Use the ```uptime``` command to show the load averages over 1,5, and 15 minute intervals

Use ```fuser``` and ```lsof``` commands to determine which process is using the file

```strace -p 5810```
