# Linux Networking

Using certain kernel tunables through the sysctl utility, you can adjust network configuration on a running system and directly affect the networking performance.
For permanent changes that persist across system restarts, add lines to the /etc/sysctl.conf file. 

###### #sysctl -a { To change network settings, use the sysctl commands. }

#### ncat utility , replace netcat

###### $ ncat -l 8080 > outputfile { Set a client machine to listen for connections on TCP port 8080 }
###### $ ncat -l 10.0.11.60 8080 < inputfile { On a server machine, specify the IP address of the client, the port and the file which is to be transferred }

#### Creating an HTTP proxy server

###### $  ncat -l --proxy-type http localhost 8080

#### Measurements of the maximum achivable bandwidth on IP networks

__host1__ `$ iperf -s -u`
__host2__ `$ iperf -c IPADRESS -u`

### Linux Network Manager

###### # systemctl status network.service { start, restart, status }

can configure network aliases, IP addresses, static routes, DNS information, and VPN connections, as well as many connection-specific parameters. 

| Application or Tool | Description |
|:----------------------- |:----------------------- |
| nmcli | A command-line tool which enables users and scripts to interact with NetworkManager. Note that nmcli can be used on systems without a GUI such as servers to control all aspects of NetworkManager. It provides a deeper functionality as GUI tools. |
| nmtui | A simple curses-based text user interface (TUI) for NetworkManager |
| nm-connection-editor | A graphical user interface tool for certain tasks not yet handled by the control-center utility such as configuring bonds and teaming connections. You can add, remove, and modify network connections stored by NetworkManager. To start it, enter nm-connection-editor in a terminal. |
| control-center | A graphical user interface tool provided by the GNOME Shell, available for desktop users. It incorporates a Network settings tool. To start it, press the Super key to enter the Activities Overview, type Network and then press Enter. The Network settings tool appears. |
| network connection icon | A graphical user interface tool provided by the GNOME Shell representing network connection states as reported by NetworkManager. The icon has multiple states that serve as visual indicators for the type of connection you are currently using. |

if you edit an ifcfg file, NetworkManager is not automatically aware of the change
###### # nmcli connection reload

Alternatively, to reload only one changed file, ifcfg-ifname:
###### # nmcli con load /etc/sysconfig/network-scripts/ifcfg-ifname

to restart the connection after changes are made, use:
###### # nmcli con up connection-name


Additional resources

..* NetworkManager(8) man page — Describes the network management daemon.
..* NetworkManager.conf(5) man page — Describes the NetworkManager configuration file.
..* /usr/share/doc/initscripts/sysconfig.txt — Describes ifcfg configuration files and their directives as understood by the legacy network service.
..* ifcfg(8) man page — Describes briefly the ifcfg command. 

#### nmcli

###### $ nmcli connection show --active
###### $ nmcli connection up id bond0 { up interface }
###### $ nmcli device disconnect id bond0 { preventing it from automatically started again }

#### Creating a connection profile with an IPv4 address
###### $ nmcli c add type ethernet ifname eth0 con-name "My Connection" ip4 192.168.2.100/24 gw4 192.168.2.1

###### $ nmcli con edit { connection editor } 

#### Configuring a Static Ethernet Connection
###### $ nmcli con mod test-lab ipv4.dns "8.8.8.8 8.8.4.4"
###### $ nmcli con edit type ethernet con-name ens3

#### Connection to wifi

###### $ nmcli radio { show enable radio interface }

        To connection WiFi
###### $ nmcli connection show { list all connection }
###### $ nmcli connection up id SSID-Connection --ask { ask password }
        
        To new WiFi AP
###### $ nmcli dev wifi { scan all WiFi AP}
###### $ nmcli device wifi SSID-Name --ask { wireless-password }
        
###### $ nmcli con add type wifi ifname wl12 con-name MyWIFI ssid $SSID
###### $ nmcli con up id MyWIFI
