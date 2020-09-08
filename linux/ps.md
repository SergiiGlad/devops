# BASH Process Management Basics

```
ps aux | head

ps fax

ps aux | grep <name>

pgrep 

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
kill <PID> the same kill -15

kill -9

kill -l

pkill firefox-bin

killall <MULTITHREDING PROCESS>

```

Using __top__ to Manage Processes

State | Meaning
--- | ---
Running (R) | 
Stopped (Sq)
