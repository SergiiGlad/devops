

## TEXT PROCCESING

grep - global regular expression print

grep [options] regex [file...]

###### $ grep -i ROOT /etc/passwd

| Option | Long Option | Description |
| --- | --- | --- |
| -i | -igrone-case | Ignore case. Do not distinguish between uppercase and lowercase characters. |
| -v | --invert-match | Invert match. Normally, grep prints lines that contain a match. This option causes grep to print every line that does not contain a match. |
| -c | --count | Print the number of matches (or non-matches if the -v option is also specified) instead of the lines themselves. |
| -l | --files-with-matches | Print the name of each file that contains a match instead of the lines themselves.|
| -L | --files-without-match | Like the -l option, but print only the names of files that do not contain matches. |
| -n | --line-number|  Prefix each matching line with the number of the line within the file. |
| -h | --no-filename | For multi-file searches, suppress the output of filenames. |

*Metacharacter*

^ $ . [ ] { } - ? * + ( ) | \

###### $ grep -i ^..j.r$ /usr/share/dict/words { one example for this pattern is word - Major }
###### $ ls /bin | grep [bg]zip - { bzip gzip }
###### $ ls /bin | grep [!bg]zip - { bg must not be present }

#### Some patterns for grep

'^[ABCDEFGHIJKLMNOPQRSTUVWXZY]'
^[A-Z]'
'^[A-Za-z0-9]'

	All lines wothout "#" 
###### $ grep -v "#" /etc/dnsmasq.conf

	Show lines after **-A** and before **-B** and **-C** about 
###### $ ifconfig | grep -A 4 eth0

	Count match word **-c**
###### $ ifconfig | grep -c 192.168

	Number lines **-n**
###### ifconfig | grep -n 192.168

	Find recursive to throuth all files and folders
###### $ grep -r mysql *

	Find into zip files
###### $ zgrep -i error /var/log/syslog.2.gz

	Find by regex ```Egrep``` or ```grep -E```

	Find by template ```fgrep -f```

###### $ ls /sbin/[[:upper:]]* { only begin with Capital letter output - /sbin/NetworkManager /sbin/ModeManager }

| Character Class | Description |
| --- | --- |
[:alnum:] | The alphanumeric characters. In ASCII, equivalent to: [A-Za-z0-9]
[:word:] | The same as [:alnum:], with the addition of the underscore (_) character.
[:alpha:] | The alphabetic characters. In ASCII, equivalent to:[A-Za-z]
[:blank:] | Includes the space and tab characters.
[:cntrl:] | The ASCII control codes. Includes the ASCII characters 0 through 31 and 127.
[:digit:] | The numerals 0 through 9.
[:graph:] | The visible characters. In ASCII, it includes characters 33 through 126.
[:lower:] | The lowercase letters.
[:punct:] | The punctuation characters. In ASCII, equivalent to: [-!"#$%&'()*+,./:;<=>?@[\\\]_`{|}~]
[:print:] | The printable characters. All the characters in [:graph:] plus the space character.
[:space:] | The whitespace characters including space, tab, carriage return, newline, vertical tab, and form feed. In ASCII, equivalent to:[ \t\r\n\v\f]
[:upper:] | The uppercase characters.

-----

###### $ cat > foo.txt
The quick brown fox jumped over the lazy dog 1 .
###### $ cat -A foo.txt { cat with spec symbol like TAB ENTER EOL}
-----
###### $ ls -lt { list and sort by time }
###### $ ls -l /usr/bin | sort -nr -k 5 | head  { list and sort by time }
------
###### $ sort -t ':' -k 3n -k 4n /etc/passwd | head { sort by several fields }
###### $ cut -d ':' -f 1,3 /etc/passwd { user name, uid }
###### $ cut -d: -f7 < /etc/passwd | sort -u { all no duplicat shells }
###### $ echo '1234567890' | cut -c 1-5 { 12345 }
-------
###### $ comm /ets/shadow /etc/shadow- { compare sorted files by lines }
-------
###### # diff /etc/shadow /etc/shadow- { compare by text }
###### # diff -c /etc/shadow /etc/shadow- { context format }
###### # diff -u /etc/shadow /etc/shadow- { universal compact format }
-----------
##### Patching
###### $ diff -Naur file1.txt file2.txt > patchfile.txt
###### $ patch < patchfile.txt
patching file file1.txt
###### $ cat file1.txt
----------
###### $ echo "lower" | tr a-z A-Z { translate to LOWER }
###### $ tr -d '\r' < файл_dos > файл_unix { dos2unix }
###### $ echo "front" | sed 's/front/back/'
###### $ sed -n '/SUSE/p' distros.txt { like grep SUSE distros.txt }
###### $ sed -n '/SUSE/!p' distros.txt { !SUSE }
###### $ sed -i 's/foo/boo/' foo.txt { -i replace input file}
------------
###### $ aspell -H check foo.txt { check spelling }
---------------
###### echo "The quick brown fox jumped over the lazy dog." | fold -w 10 
	The quick 
	brown fox 
	jumped ove
	r the lazy
	 dog.
-------------
###### $ fmt -w 50 fmt-info.txt | head  { to reformat this text to fit a 50-character-wide column }
----------
###### $ pr -l 15 -w 65 distros.txt { formatting our distros.txt file to printing into a series of short pages } 	
-------------------
###### $ printf "I formatted the string: %s\n" foo

|Specifier| Description|
| --- | --- |
|d |Format a number as a signed decimal integer.
|f |Format and output a floating-point number.
|o |Format an integer as an octal number.
|s |Format a string.
|x |Format an integer as a hexadecimal number using lowercase a to f where needed.
|X |Same as x but use uppercase letters.
|% |Print a literal % symbol (i.e., specify %%)
-----------------
###### $ printf "%d, %f, %o, %s, %x, %X\n" 380 380 380 380 380 380
--------------------
###### $ zcat /usr/share/man/man1/bash.1.gz  | groff -mandoc > ~/Desktop/bash.ps  { formatting to PostScript }
---------------------
###### $ ps2pdf ~/Desktop/foo.ps ~/Desktop/ls.pdf { convert to PDF } 
---------------
#### Printing

  * pr – Convert text files for printing
  * lpr – Print files
  * a2ps – Format files for printing on a PostScript printer
  * lpstat – Show printer status information
  * lpq – Show printer queue status
  * lprm – Cancel print jobs
---------------------

Common Unix Printing System (CUPS) provides print drivers and print-job man-
agement, and the second, Ghostscript, a PostScript interpreter, acts as a RIP.

###### $ lpstat -s { info about printers }
###### $ lpq { maintaining print queues }





