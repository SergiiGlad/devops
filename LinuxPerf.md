

## Linux system untils for monitoring

#### Special soft for monitoring system are Zabbix and Prometheus 
(Graphite/Icinga/Zabbix/Prometheus/Netdata have nice grafics )
##
###### $ uptime { 17:09:42 up 2 days,  5:23,  4 users,  load average: 0.77, 1.21, 1.14 }
###### $ w 
###### $ cat /proc/uptime { 192411.43 130228.29 }
###### $ cat /proc/loadavg { 0.60 0.86 1.00 1/824 15317 }
##
###### $ pidstat
###### $ htop
###### $ pidof java
###### $ pstree 1 { pstree $(pidof dockerd) }
###### $ sar -r 
###### $ time python ‐c "import time; time.sleep(1)" { time on run program }
###### $ mpstat -P ALL 1 { on each core }
##
###### $ cat /proc/meminfo
###### $ free -ht { human readable , total sum with swap }
###### $ sudo dmidecode ‐‐type 17 { from BIOS }
###### $ ps aux
###### $ top
###### $ vmstat 1
###### $ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
##
###### $ sudo fdisk -l
###### $ sudo cfdisk
###### $ sudo gdisk
###### $ sudo gparted
###### $ gnome-disks
###### $ sudo parted /dev/sda
###### $ df -h
###### $ du -sh /home/user { size of folder /home/user }
##
###### $ iostat { read/write disk operation }
###### $ iotop { I/O CPU }
###### $ sudo iftop -i eth0 { send/recieve network interface }
###### $ ifstat { reports the network bandwidth in a batch style mode }
###### $ netstat -i { network metrics }
##
###### $ ip address { ip a }
###### $ brctl show
###### $ route -n
###### $ ip route show { ip r s }
###### $ netstat -nr
###### $ cat /proc/net/fib_trie
##
###### $ sudo netstat -tnlp { list ports }
###### $ sudo lsof | grep TCP { list of open files,  TCP connection info }
###### $ sar -n DEV 1 { info rx/tx by each interface }
###### $ sar ‐1 TCP,ETCP 1
###### $ tcpdump -i eth0
###### $ tcpdump ‐w test.dump
###### $ ss { similar netstat socket stat }
##
###### $ cat /proc/cpuinfo
###### $ lscpu
###### $ nproc
###### $ dmidecode
##

###### $ journalctl { show all messages }

###### $ journalctl --list-boots { all lists boots }
###### $ journalctl -b { current boot }
###### $ journalctl -b -1 { last boot }

###### $ journalctl --since "2018-06-15 08:15:00"
###### $ journalctl --since today
###### $ journalctl --since yesterday

###### $ journalctl -n { last 10 messages }
###### $ journalctl -n 20

###### $ journalctl -k { like dmesg }
###### $ journalctl -k -b

###### $ journalctl -u apache2.service
###### $ journalctl _PID=19487 --since today
###### $ journalctl _UID=1000
###### $ journalctl /usr/bin/bash
###### $ journalctl /usr/bin/dbus-daemon
 
###### $ journalctl -p err { prioritet error }
###### $ journalctl -p emerg..warning

###### $ journalctl -f { real time messages }

###### $ journalctl --disk-usage
###### $ sudo journalctl --vacuum-size=50M #delete files until the disk space they use falls below the specified size
###### $ sudo journalctl --vacuum-time=1years #delete files so that all journal files contain no data older than the specified timespan
###### $ sudo journalctl --vacuum-files=4 #delete files so that no more than the specified number of separate journal files remain in storage location

###### $ $ sudo journalctl --rotate

##

###### dmesg -t -k
###### dmesg -t -l err
###### dmesg -t -l emerg
###### dmesg -t -l warn { alert }










