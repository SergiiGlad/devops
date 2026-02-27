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

**** WITR 
Why is this running?

https://github.com/pranshuparmar/witr

Interactive Mode (TUI)
Running witr without any arguments or with the -i flag launches the Interactive Mode (TUI). This provides a real-time, terminal-based dashboard for exploring processes and ports.

Key Features:
* Live Process List: Real-time view of all running processes with sorting and filtering.
* Port View: Explore open ports and immediately see which processes are holding them.
* Process Details: Deep-dive into a specific process to see its full ancestry tree, child processes, environment variables, working directory, and more.
* Process Actions: Send signals (Kill, Terminate, Pause, Resume) or Renice processes directly from the UI.
* Mouse Support: Navigate, sort columns, and click rows using your mouse.

