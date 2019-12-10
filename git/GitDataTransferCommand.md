__Remember, HEAD__ is an alias for the last commit-hash of the branch.

## git checkout

### The checkout command is used to copy files from the history (or stage) to the working directory, and to optionally switch branches.

###  The command __git checkout__ will replace everything in the working directory to the last committed version.
---
Use git checkout to clear any changes in the working directory.
###### git checkout .
---
Copies files from the latest commit to both the stage and the working directory
###### git checkout HEAD -- files
---
copies _file.java_ from the stage to the working directory. If no commit name is given, files are copied from the stage.
###### git checkout file.java 
---
If you want to check out all C source files out of the index. 
###### git checkout '*.c' 
---
If you have an unfortunate branch that is named hello.c, this step would be confused as an instruction to switch to that branch.
###### git checkout -- hello.c 
---
copies _file.java_ from the commit called HEAD~(the parent of the current commit) commit to the stage and the working directory. Note that the current branch is not changed
###### git checkout HEAD~ file.java 
---
 When a filename is not given but the reference is a (local) branch, HEAD is moved to that branch
###### git checkout develop
---
When a filename is not given and the reference is not a (local) branch — say, it is 
 * a tag,
 * a remote branch, 
 * a SHA-1 ID, 
 * or something like master~3 — we get an anonymous branch, called a detached HEAD. 
 
 This is useful for jumping around the history. Say you want to compile version 1.6.6.1 of git. You can ```git checkout v1.6.6.1``` (which is a tag, not a branch), switch back to another branch, say ```git checkout master```.

## git reset

### move files back from the staging area to the working directory

###### git reset HEAD .
---
Combine both git reset and git checkout in a single command. The result will be the files removed from the staging area and the working directory is taken back to the state of the last commit.
###### git reset --hard 

## git log

###### git log --pretty=oneline

###### git show { git log --pretty=format:"%h %an %ar - %s" }

###### git log --grep="1234"

---
To output the commit information with the differences of what changed you need to include the -p prompt 
###### git log -p 

---
The -n <number> specifies a limit of commits to display from the HEAD

###### git log -p -n 2

## git diff

### The git diff command is the simplest to compare what's changed between commits. It will output the differences between the two commits.


