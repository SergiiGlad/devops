# Network configuration

https://docs.oracle.com/cd/E52668_01/E54669/html/ol7-netconf.html

File | Desc
 --- | --- 
vi /etc/sysconfig/network-scripts/ifcfg-lo | Configuration file named ifcfg-interface 
vi /etc/hosts | It allows the system to look up (resolve) the IP address of a host given its name, or the name given the IP address. 
vi /etc/nsswitch.conf | The /etc/nsswitch.conf file configures how the system uses various databases and name resolution mechanisms. 
vi /etc/resolv.conf | The /etc/resolv.conf file defines how the system uses DNS to resolve host names and IP addresses. 
vi /etc/sysconfig/network  | The /etc/sysconfig/network file specifies additional information that is valid to all network interfaces on the system. 
`/usr/share/doc/initscripts*/sysconfig.txt` | **see more information**

##### nmcli device status
##### ip addr show

 You can also use ip to set properties and activate a network interface. The following example sets the IP address of the em2 interface and activates it:

##### ip addr add 10.1.1.1/24 dev em2 --
##### ip link set em2 up

### Network Interface Bonding
balance-rr ( round-robin fashion ), balance-xor, balance-tlb, balance-alb
For more information see `/usr/share/doc/iputils-*/README.bonding`. 

### Network Interface Teaming
Create a JSON-format definition file for the team and its component ports. For sample configurations, see the files under /usr/share/doc/teamd-*/example_configs/. 
##### teamd -g -f /root/team_config/team0.conf -d

### Configuring VLANs
*To obtain information about the configured VLAN interfaces, view the files in the /proc/net/vlan directory. *

### Network Routing
##### # ip route show
##### # netstat -rn 






