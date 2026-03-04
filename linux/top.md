#### Linux **top** command

https://man7.org/linux/man-pages/man1/top.1.html


Top:
![alt text](https://github.com/SergiiGlad/devops/blob/master/linux/top.png "Top")

###### $ top -v { version 3.3.10}

##### Memory usage

 * total - value total 
 * free - free
 * used - used
 * buff/cache - disk buffer
 * avail Mem - amount of memory that can be allocated to processes without causing more swapping


##### Tasks

 * total - value is simply the total number of processes
 * running - Runnable(R) state executing on the CPU
 * sleeping - Interruptible (S) Uninterruptible sleep (D)
 * stopped - Stopped (T) these processes have been stoped by a job control signal
 * zombie - Zombie (Z) such terminated processes whose data structures are still around are called zombies 


##### CPU Usage
 
%Cpu(s):

 * us - is the time the CPU spends executing processes in userspace
 * sy - kernelspace processes
 * ni - a manually set "nice" and gets a low priority
 * id - idle
 * wa - waiting for I/O to complete
 * hi - hardware interrupts
 * si - software interrupts
 * st - steal time , the CPU is busy on some other virtual machine (VM)

##### Load average

**The load average section represents the average "load" over one ( 60 sec ), five and fifteen minutes.**
On Linux the load is *the number of processes in the R and D states at any given moment.*
On a multi-core system you should first divide the load average with the number of CPU cores to get a similar measure.

##### The task area

 * PID 
 * USER
 * PR - priority of the process
 * NI - the "nice" value of a process 
 * VIRT - the total amount of memory consumed by a process
 * RES - is the memory consumed by the process in RAM
 * SHR - the amount of a memory shared with other processes
 * %MEM - expresses value as a persentage of the total RAM available
 * S - single-letter form show the process state
 * TIME+ - total CPU time used, precise to the hundredths of a second
 * COMMAND - the name of the processes

Using **top** command

https://developer.ibm.com/tutorials/l-lpic1-103-5/

The top command has a number of subcommands, of which the most useful to start with are:

h: Gets you help
q: Quits the top command
f: Lets you add or remove fields from the display
F: Selects fields to sort on
Shift V: forest view. you can see is relationship between a parent process and a child process
k: PID to signal/kill
W: Write-the-Configuration-File

[Understanding Linux System Performance | The Top Command by Akamai](https://www.youtube.com/watch?v=3r_PBLaZoFQ
)Developer / Learn Linux TV (22:52)

```bash
top -1 # show cpu usage per core
```

Alternatives:
* atop
* htop
* glances
* nmon
* dstat
* sar





