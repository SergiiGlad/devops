#!/bin/bash

#
# git status
#
  echo "HEAD:     $(git cat-file -p HEAD:myfile)"
  echo "Stage:    $(git cat-file -p :myfile)"
  echo "Worktree: $(cat myfile)"

