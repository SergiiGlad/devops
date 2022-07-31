# BASH Process Management Basics

## [Processes](https://abarrak.gitbook.io/linux-sysops-handbook/#processes)

The daemon __systemd__ process starts during boot time, and remains active until the shutdown. It's the parent process for all other process in the system.
Each __process__ contains several main parts, such as: PID, state, virtual space address (memory), threads, network and file descriptors, scheduler information, and links. Processes are controlled and respond to signals. 

```
ps auxc | head

ps fax

ps aux | grep <name>

pgrep 

psgrep -u abdullah -l

pstree

```

Adjusting Process Priority with _nice_

ranging from -20 to 19

__Regular processes start with the priority number 20 ( is set 0)__
The default niceness is set to 0
```
nice -n 5 dd if=/dev/zero of=/dev/null &

renice -n 10 -p <PID>
```

Sending Signals to Processes with __kill, killall and pkill__

SIGTERM(15) - normal terminated

SIGKILL(9) - force a process stop

SIGHUP(1)

```
kill -l
kill -9 5921
kill -SIGTERM 6152

kill <PID> the same kill -15
kill -9
kill -l

pkill firefox-bin
killall -15 nginx
pkill -U tester

killall <NAME MULTITHREDING PROCESS>

```

Using __top__ to Manage Processes

State | Meaning
--- | ---
Running (R) | 
Stopped (Sq)
