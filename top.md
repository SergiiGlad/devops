#### Linux *top* command

![alt text](https://github.com/sergeyglad/devops/top.png "Top")

###### $ top -v { version 3.3.10}

##### Memory usage
 * total 
 * free
 * used
 * buff/cache - disk buffer
 * avail Mem - amount of memory that can be allocated to processes without causing more swapping


##### Tasks


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

 

