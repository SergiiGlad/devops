
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
