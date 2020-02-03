# AWK		

technically, AWK was created before both python and bash
It is a great language
Awk is geared toward text processing and report generation, yet features many well-designed features that allow for serious programming.
Examples:
	#### gawk '{ sum += $1 }; END { print sum }' file


print command for each line in file
```
awk '{print}' /etc/password
```
// the same thing  
```
awk '{ print $0 }' /etc/password
```
Multiple fields
-F as the field separator
__default FS__ is set to a single space character, which awk interprets to mean
"one or more spaces or tabs"
```
awk -F":" '{print $1 " " $3}' /etc/passwd
```

External script
```
awk 'BEGIN { FS=":"} {print $1}' /etc/passwd
```

Regular expressions and blocks
```
awk 'BEGIN { FS=":"} $7 == "/sbin/nologin"  {print $0}' /etc/passwd

awk 'BEGIN { FS=":"} $6 ~ /\/home/  {print $0}' /etc/passwd

awk 'BEGIN { FS=":"}  { if ($5 ~ /root/) { print $3 } }' /etc/passwd
```

Numeric variables!
awk automatically takes care of the string-to-number conversion steps
```
echo | awk '{print "12.13" + "13.12"}'
```

Number of fields NF

this particular record has NF fields

```
awk -F "\t" '{print $3 "  " $NF}' jan20only.tsv
```

Record Number NR
like head -n 10
```
awk 'NR < 11 { print "\t" i " " $0}' /etc/passwd
```
