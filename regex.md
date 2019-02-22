

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

	some patterns for grep
'^[ABCDEFGHIJKLMNOPQRSTUVWXZY]'
^[A-Z]'
'^[A-Za-z0-9]'

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













