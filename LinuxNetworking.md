# Linux Networking

Using certain kernel tunables through the sysctl utility, you can adjust network configuration on a running system and directly affect the networking performance.
For permanent changes that persist across system restarts, add lines to the /etc/sysctl.conf file. 

###### #sysctl -a { To change network settings, use the sysctl commands. }

#### ncat utility , replace netcat

###### $ ncat -l 8080 > outputfile { Set a client machine to listen for connections on TCP port 8080 }
###### $ ncat -l 10.0.11.60 8080 < inputfile { On a server machine, specify the IP address of the client, the port and the file which is to be transferred }

#### Creating an HTTP proxy server

###### $  ncat -l --proxy-type http localhost 8080

| Application or Tool | Description |
|:----------------------- |:----------------------- |
| nmcli | A command-line tool which enables users and scripts to interact with NetworkManager. Note that nmcli can be used on systems without a GUI such as servers to control all aspects of NetworkManager. It provides a deeper functionality as GUI tools. |
| nmtui | A simple curses-based text user interface (TUI) for NetworkManager |
| nm-connection-editor | A graphical user interface tool for certain tasks not yet handled by the control-center utility such as configuring bonds and teaming connections. You can add, remove, and modify network connections stored by NetworkManager. To start it, enter nm-connection-editor in a terminal. |
| control-center | A graphical user interface tool provided by the GNOME Shell, available for desktop users. It incorporates a Network settings tool. To start it, press the Super key to enter the Activities Overview, type Network and then press Enter. The Network settings tool appears. |
| network connection icon | A graphical user interface tool provided by the GNOME Shell representing network connection states as reported by NetworkManager. The icon has multiple states that serve as visual indicators for the type of connection you are currently using. |
