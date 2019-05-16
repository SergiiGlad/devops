
## View logs: journalctl 

###### $ journalctl { show all messages }

###### $ journalctl --list-boots { all lists boots }
###### $ journalctl -b { current boot }
###### $ journalctl -b -1 { last boot }

###### $ journalctl --since "2018-06-15 08:15:00"
###### $ journalctl --since today
###### $ journalctl --since yesterday
###### $ journalctl --since 09:00 until now

###### $ journalctl -n { last 10 messages }
###### $ journalctl -n 20

###### $ journalctl -k { kernel messages like dmesg }
###### $ journalctl -k -b

###### $ journalctl -u apache2.service
###### $ journalctl -u nginx.service -o json
###### $ journalctl _PID=19487 --since today
###### $ journalctl _UID=1000
###### $ journalctl -F _UID
###### $ journalctl /usr/bin/bash
###### $ journalctl /usr/bin/dbus-daemon
 
###### $ journalctl -p err { prioritet error }
###### $ journalctl -p emerg..warning
	0 - EMERG
	1 - ALERT
	2 - CRIT
`	3 - ERR
	4 - WARNING
	5 - NOTICE
	6 - INFO
	7 - DEBUG

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










