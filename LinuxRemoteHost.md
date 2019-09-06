
## ftp

###### myhost $ ftp server1
###### anonymous
###### cd Folder1
###### lcd MyHomeDownloadFolder
###### ls
###### get file1
###### bye
###### myhost $


###### ssh remote free { run command on remote host }

###### scp remote:file1 . { copy file1 from remote host to current folder }

###### ssh remote 'tar cf - Documents' | tar xf - { copy folder Documents form remote host to local }

	make mirror
###### $ mkdir fedora-devel
###### $ rsync -av -delete rsync://rsync.gtlib.gatech.edu/fedora-linux-core/development/i386/os fedora-devel 

---

## Disconnect the node

- We will use `iptables` to block all traffic exiting the node

  (except SSH traffic, so we can repair the node later if needed)

.exercise[

- SSH to the node to disrupt:
  ```bash
  ssh `nodeX`
  ```

- Allow SSH traffic leaving the node, but block all other traffic:
  ```bash
  sudo iptables -I OUTPUT -p tcp --sport 22 -j ACCEPT
  sudo iptables -I OUTPUT 2 -j DROP
  ```

]
---

## Re-enable the node

- Let's fix the node that we disconnected from the network

.exercise[

- SSH to the node:
  ```bash
  ssh `nodeX`
  ```

- Remove the iptables rule blocking traffic:
  ```bash
  sudo iptables -D OUTPUT 2
  ```

]

---

