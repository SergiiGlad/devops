## What is IPTables?
__iptables__ is a user-space application that allows configuring Linux kernel firewall (implemented on top of Netfilter) by configuring chains and rules.
## What is Netfilter? 
A framework provided by the Linux kernel that allows customization of networking-related operations, such as packet filtering, NAT, port translation etc.
## Issues with IPTables as a load balancer
* Latency to access service (routing latency)
* Latency to add/remove rules
