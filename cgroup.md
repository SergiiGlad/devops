```
apt install cgroup-tools
```

Create cgroup ```cgcreate -g cpu:devops``` or ```mkdir /sys/fs/cgroup/cpu/devops```
run process in group  ```cgexec -g cpu:devops stress -c 2```
add to gcroup ```echo 26932 ? cpu/devops/tasks``` ```cgclassify -g cpu:devops --stick 26932```
del cgroup ```cgdelete -g cpu:devops```
check cgroup ```ps -o cgroup 26932```

monitoring 
```
systemd-cgtop
systemd-cgls
cat cpu/devops/tasks
cat /proc/26932/cgroup
```
