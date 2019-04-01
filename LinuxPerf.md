

## Linux system untils for monitoring

#### Special soft for monitoring system are Zabbix and Prometheus 
(Graphite/Icinga/Zabbix/Prometheus/Netdata have nice grafics )

###### $ uptime { 17:09:42 up 2 days,  5:23,  4 users,  load average: 0.77, 1.21, 1.14 }
###### $ w 
###### $ cat /proc/uptime { 192411.43 130228.29 }
###### $ cat /proc/loadavg { 0.60 0.86 1.00 1/824 15317 }

###### $ pidstat
###### $ htop
###### $ pidof
###### $ pstree { pstree $(pidof dockerd) }

###### $ time python ‐c "import time; time.sleep(1)" { time on run program }
###### $ mpstat -P ALL 1 { on each core }

###### $ cat /proc/meminfo
###### $ free -ht { human readable , total sum with swap }
###### $ sudo dmidecode ‐‐type 17 { from BIOS }
###### $ ps aux
###### $ top
###### $ vmstat 1

###### $ sudo fdisk -l
###### $ sudo cfdisk
###### $ sudo gdisk
###### $ sudo gparted
###### $ gnome-disks
###### $ sudo parted /dev/sda
###### $ df -h
###### $ du -sh /home/user { size of folder /home/user }

###### $ iostat { read/write disk operation }
###### $ iotop { I/O CPU }
###### $ sudo iftop -i eth0 { send/recieve network interface }

###### $ ip address { ip a }
###### $ brctl show
###### $ route -n
###### $ ip route show { ip r s }
###### $ netstat -nr
###### $ cat /proc/net/fib_trie

###### $ sudo netstat -tnlp { list ports }
###### $ sudo lsof | grep TCP { list of open files,  TCP connection info }
###### $ sar -n DEV 1 { info rx/tx by each interface }
###### $ sar ‐1 TCP,ETCP 1
###### $ tcpdump -i eth0
###### $ tcpdump ‐w test.dump
###### $ ss { similar netstat socket stat }















