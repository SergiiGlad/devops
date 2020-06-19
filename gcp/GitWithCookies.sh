#!/bin/bash
# Configure Git with a cookie for this service by copying this script and pasting it into a shell.

eval 'set +o history' 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
 touch ~/.gitcookies
 chmod 0600 ~/.gitcookies

 git config --global http.cookiefile ~/.gitcookies

 tr , \\t <<\__END__ >>~/.gitcookies
source.developers.google.com,FALSE,/,TRUE,2147483647,o,git-sergii.gladchenko.gmail.com=1//035ke9-iVbl2PCgYIARAAGAMSNwF-L9IrER3Vy8ujhb6QkVqSlRAcKJpLE5b1tQSAhl9yd1zprrYHUOnMK9LWFcshrfUf1uJ3hbI
__END__
eval 'set -o history' 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null
