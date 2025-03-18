
## Linux system untils for monitoring

#### Special soft for monitoring system are Zabbix and Prometheus
(Graphite/Icinga/Zabbix/Prometheus/Netdata have nice grafics )
##
###### $ uptime { 17:09:42 up 2 days,  5:23,  4 users,  load average: 0.77, 1.21, 1.14 }
###### $ w
###### $ cat /proc/uptime { 192411.43 130228.29 }
###### $ cat /proc/loadavg { 0.60 0.86 1.00 1/824 15317 }
##
###### $ sudo starce -p $PID { figure out what a process is actually doing }
###### $ pidstat -r { memory leak }
###### $ htop
###### $ pidof java
###### $ pstree 1 { pstree $(pidof dockerd) }
###### $ sar -r
###### $ time python ‐c "import time; time.sleep(1)" { time on run program }
###### $ mpstat -P ALL 1 { on each core }
###### # fuser /var/run/docker.sock { to get number processes which use file }
##
###### $ cat /proc/meminfo
###### $ free -ht { human readable , total sum with swap }
###### $ sudo dmidecode ‐‐type 17 { from BIOS }
###### $ ps aux
###### $ top
###### $ vmstat 1
###### $ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head

## Disk

###### $ findmnt { to list all mounted file system }
###### $ blkid
###### $ lsblk --fs /dev/sda1
###### $ sudo fdisk -l
###### $ sudo cfdisk
###### $ sudo gdisk
###### $ sudo gparted
###### $ gnome-disks
###### $ sudo parted /dev/sda
###### $ df -h
###### $ du -sh /home/user { size of folder /home/user }
###### $ du -hs $(ls -A) { This command shows the space each file uses within each sub-directory}

##
###### $ iostat { read/write disk operation }
###### $ iotop { I/O CPU }
###### $ sudo iftop -i eth0 { send/recieve network interface }
###### $ ifstat { reports the network bandwidth in a batch style mode }
###### $ netstat -i { network metrics }

## Network
---
###### $ ip address { ip a }
###### $ brctl show
###### $ route -n
###### $ ip route show { ip r s }
###### $ netstat -nr
###### `# cat /proc/net/fib_trie`  { show ip address }
###### `# cat /proc/net/route` { show ip table }
###### `# lsof -i` { show all TCP/IP socket }
CHECK FOR OPENS PORT
echo > /dev/tcp/<server ip>/<port>

```
echo > /dev/tcp/localhost/22
```
---
###### $ sudo netstat -tnlp { list ports }
###### $ sudo lsof | grep TCP { list of open files,  TCP connection info }
###### $ sar -n DEV 1 { info rx/tx by each interface }
###### $ sar ‐1 TCP,ETCP 1
---
###### $ tcpdump -i eth0
###### $ tcpdump ‐w test.dump
###### # tcpdump -n host google.com
###### # tcpdump -n not host domain.com
###### # tcpdump -n port 53 or port 443
###### # tcpdump -n -l host web1 | tee outputfile { -l oprion buffers to output }
###### # tcpdump -w -C 10 -W 5 output.pcap { for Wireshark 5 files 10M }
###### # tcpdump -n -r output.pcap { real time }

###### $ ss { similar netstat socket stat }
###### # iptables -L

##
###### $ cat /proc/cpuinfo
###### $ lscpu
###### $ nproc
###### $ dmidecode

## Linux Performance Analysis in 60,000 Milliseconds

<http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html>

```
uptime
dmesg | tail
vmstat 1
mpstat -P ALL 1
pidstat 1
iostat -xz 1
free -m
sar -n DEV 1
sar -n TCP,ETCP 1
top
```

## Stress Test CPU and Memory (VM)

###### tload - representation of system load average

```
stress -c 2 -i 1 -m 1 --vm-bytes 128M -t 10s
```
Where:
 * -c 2 : Spawn two workers spinning on sqrt()
 * -i 1 : Spawn one worker spinning on sync()
 * -m 1 : Spawn one worker spinning on malloc()/free()
 * --vm-bytes 128M : Malloc 128MB per vm worker (default is 256MB)
 * -t 10s : Timeout after ten seconds
 * -v : Be verbose


## Create a CPU load

```dd if=/dev/urandom | gzip -9 >> /dev/null &```

