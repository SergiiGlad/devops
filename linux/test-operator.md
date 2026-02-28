  Canonical Source

  The most authoritative and complete source is the GNU Bash Reference Manual, specifically the section on Conditional Expressions.


   * Link: Bash Reference Manual - Conditional Expressions (https://www.gnu.org/software/bash/manual/bash.html#Conditional-Expressions)

  Summarized List of Common Test Operators

  Here's a summary of the most commonly used operators, categorized for easier understanding:

  1. String Operators


  Used for comparing or checking properties of strings.


   * -z STRING: True if the length of STRING is zero (empty).
   * -n STRING: True if the length of STRING is non-zero (not empty).
   * STRING1 = STRING2: True if the strings are equal. (== also works in [[ ... ]]).
   * STRING1 != STRING2: True if the strings are not equal.
   * STRING1 < STRING2: True if STRING1 sorts before STRING2 lexicographically (based on current locale).
   * STRING1 > STRING2: True if STRING1 sorts after STRING2 lexicographically (based on current locale).

  2. Integer Operators

  Used for comparing numeric values. Important: These only work for integers. For string comparisons, use STRING1 = STRING2.


   * INT1 -eq INT2: True if INT1 is equal to INT2.
   * INT1 -ne INT2: True if INT1 is not equal to INT2.
   * INT1 -lt INT2: True if INT1 is less than INT2.
   * INT1 -le INT2: True if INT1 is less than or equal to INT2.
   * INT1 -gt INT2: True if INT1 is greater than INT2.
   * INT1 -ge INT2: True if INT1 is greater than or equal to INT2.

  3. File Operators

  Used for checking properties of files or directories.


   * -a FILE / -e FILE: True if FILE exists.
   * -b FILE: True if FILE exists and is a block special file.
   * -c FILE: True if FILE exists and is a character special file.
   * -d FILE: True if FILE exists and is a directory.
   * -f FILE: True if FILE exists and is a regular file.
   * -g FILE: True if FILE exists and has its set-group-id bit set.
   * -h FILE / -L FILE: True if FILE exists and is a symbolic link.
   * -k FILE: True if FILE exists and has its sticky bit set.
   * -p FILE: True if FILE exists and is a named pipe (FIFO).
   * -r FILE: True if FILE exists and is readable by the current process.
   * -s FILE: True if FILE exists and has a size greater than zero.
   * -t FD: True if file descriptor FD is open and refers to a terminal.
   * -u FILE: True if FILE exists and has its set-user-id bit set.
   * -w FILE: True if FILE exists and is writable by the current process.
   * -x FILE: True if FILE exists and is executable by the current process.
   * -O FILE: True if FILE exists and is owned by the effective user ID.
   * -G FILE: True if FILE exists and is owned by the effective group ID.
   * -N FILE: True if FILE exists and has been modified since it was last read.
   * FILE1 -nt FILE2: True if FILE1 is newer than FILE2 (based on modification dates).
   * FILE1 -ot FILE2: True if FILE1 is older than FILE2 (based on modification dates).
   * FILE1 -ef FILE2: True if FILE1 and FILE2 refer to the same device and inode numbers (i.e., they are hard links to the same file).


  4. Logical Operators (within [ ... ] or test)

  These combine multiple expressions.


   * ! EXPRESSION: True if EXPRESSION is false.
   * EXPRESSION1 -a EXPRESSION2: True if both EXPRESSION1 and EXPRESSION2 are true (AND).
   * EXPRESSION1 -o EXPRESSION2: True if either EXPRESSION1 or EXPRESSION2 is true (OR).

  ---

  Important Considerations: [ ... ] vs [[ ... ]] vs (( ... ))


   * `[ EXPRESSION ]` (aka `test`): This is the traditional POSIX-compliant syntax. It's a standard external command.
       * Requires proper quoting of variables (e.g., [ -z "$VAR" ]).
       * Does not perform word splitting or pathname expansion on the expression.
       * && and || are treated as separate commands, so for logical AND/OR you use -a/-o within the same [ ].


   * `[[ EXPRESSION ]]`: This is a Bash-specific keyword (not an external command) and offers more advanced features.
       * Does not require quoting of variables as much (e.g., [[ -z $VAR ]] works fine, though quoting is still good practice for clarity).
       * Supports regular expression matching (=~ operator).
       * Supports && and || for logical AND/OR operations directly within the [[ ]].
       * Performs word splitting and pathname expansion on unquoted variables within.


   * `(( ARITHMETIC_EXPRESSION ))`: This is for evaluating arithmetic expressions.
       * Returns true (exit status 0) if the expression evaluates to a non-zero value, and false (exit status 1) if it evaluates to zero.
       * Supports standard arithmetic operators (+, -, *, /, %, ==, !=, <, >).
       * (( a > b )) is equivalent to [ "$a" -gt "$b" ].


  For modern Bash scripting, [[ ... ]] is generally preferred for its enhanced features and fewer quoting pitfalls, especially for string comparisons
  and regex matching.
