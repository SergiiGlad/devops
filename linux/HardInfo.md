
http://opensource.com/article/19/9/linux-commands-hardware-information

## Hardware overview

```hwinfo --short```

or

```lshw -short```

The long full froms but hard to read output 

```hwinfo``` or ```lshw```

## CPU details

```lscpu```
or
```
lshw -C cpu

lshw -C cpu | grep -i mhz

```

## Memory

```dmidecode -t memory | grep -i size```

For more specifics

```lshw -short -C memory```

Video device

```lspci | grep -i vga```

```free -m```
or

```top``` 


