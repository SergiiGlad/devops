## Checkout

### The checkout command is used to copy files from the history (or stage) to the working directory, and to optionally switch branches.

```git checkout file.java``` copies _file.java_ from the stage to the working directory. If no commit name is given, files are copied from the stage.

```git checkout '*.c'``` If you want to check out all C source files out of the index. 
```git checkout -- hello.c``` If you have an unfortunate branch that is named hello.c, this step would be confused as an instruction to switch to that branch.

```git checkout HEAD~ file.java``` copies _file.java_ from the commit called HEAD~(the parent of the current commit) commit to the stage and the working directory. Note that the current branch is not changed.

```git checkout develop``` When a filename is not given but the reference is a (local) branch, HEAD is moved to that branch

When a filename is not given and the reference is not a (local) branch — say, it is 
 * a tag,
 * a remote branch, 
 * a SHA-1 ID, 
 * or something like master~3 — we get an anonymous branch, called a detached HEAD. 
 
 This is useful for jumping around the history. Say you want to compile version 1.6.6.1 of git. You can ```git checkout v1.6.6.1``` (which is a tag, not a branch), switch back to another branch, say ```git checkout master```.

## Log

###### git log --pretty=oneline


