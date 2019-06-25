# Managing Services on Linux with systemd

https://linuxaria.com/article/how-to-manage-processes-with-cgroup-on-systemd

## Verifying Bootup

Use ```systemctl``` and ```systemctl``` status as modern, more complete replacements for the traditional boot-up status messages of SysV services. 

```
###### # systemctl status ntpd.service
```

## Which Service Owns Which Processes?

In systemd we place every process that is spawned in a _control group_ named after its service. Control groups (or cgroups) at their most basic are simply groups of processes that can be arranged in a hierarchy and labelled individually.

```
$ ps xawf -eo pid,user,cgroup,args
```
A different way to present the same information is the systemd-cgls tool we ship with systemd. It shows the cgroup hierarchy in a pretty tree. Its output looks like this:

```
$ systemd-cgls
```

## Killing Services

With systemctl kill you can easily send a signal to all processes of a service. Example:

```# systemctl kill -s SIGKILL crond.service```

## The Three Levels of "Off"

In systemd, there are three levels of turning off a service (or other unit). Let's have a look which those are:

* __stop__ That simply terminates the running instance of the service and does little else.

* __disable__ That means, that depending on your service it will no longer be activated on boot, by socket or bus activation or by hardware plug (or any other trigger that applies to it). However, you can still start it manually if you wish.

* __mask__ This is like disabling a service, but on steroids. It not only makes sure that service is not started automatically anymore, but even ensures that a service cannot even be started manually anymore. 

## Changing Roots

As administrator or developer sooner or later you'll ecounter __chroot()__ environments. The __chroot()__ system call simply shifts what a process and all its children consider the root directory /, thus limiting what the process can see of the file hierarchy to a subtree of it.




