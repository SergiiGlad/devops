## Checkout

### The checkout command is used to copy files from the history (or stage) to the working directory, and to optionally switch branches.

```git checkout file.java``` copies _file.java_ from the stage to the working directory

```git checkout HEAD~ file.java``` copies _file.java_ from the commit called HEAD~(the parent of the current commit) commit to the stage and the working directory

```git checkout HEAD -- files``` copies files from the latest commit to both the stage and the working directory.
