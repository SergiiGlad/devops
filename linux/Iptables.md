## What is IPTables?
__iptables__ is a user-space application that allows configuring Linux kernel firewall (implemented on top of Netfilter) by configuring chains and rules.
## What is Netfilter? 
A framework provided by the Linux kernel that allows customization of networking-related operations, such as packet filtering, NAT, port translation etc.
## Issues with IPTables as a load balancer
* Latency to access service (routing latency)
* Latency to add/remove rules
## IPTables Example
```
iptables -t nat -L -n
```

Enable ip forwarding
```
vi /etc/sysctl.conf
```
__Edit__ /etc/sysctl.conf
net.ipv4.ip_forward=1
net.ipv4.conf.default.forwarding=1
net.ipv4.cong.all.forwarding=1

## What is IP Virtual Server (IPVS)?

* Transport layer load balancer which directs requests for TCP and UDP based services to real servers.
* Part of the Linux Virtual Server (LVS) project.
* As with IPTables, IPVS is built on top of Netfilter.
* Supports 3 load balancing modes: 
  - NAT
  - DR (L2 load balancing via MAC rewriting)
  - IP Tunneling

