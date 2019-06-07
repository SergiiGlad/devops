

## Basic Usage

Visual Git

[Visual Git Guide](http://marklodato.github.io/visual-git-guide/index-en.html)

The four commands above copy files between the working directory, the stage (also called the index), and the history (in the form of commits).

 *   ```git add files``` copies files (at their current state) to the stage.
 *   ```git commit``` saves a snapshot of the stage as a commit.
 *   ```git reset -- files``` unstages files; that is, it copies files from the latest commit to the stage. Use this command to "undo" a git add files. You can also git reset to unstage everything.
 *   ```git checkout -- files``` copies files from the stage to the working directory. Use this to throw away local changes.

 *   ```git commit -a``` is equivalent to running git add on all filenames that existed in the latest commit, and then running git commit.
 *   ```git commit files``` creates a new commit containing the contents of the latest commit, plus a snapshot of files taken from the working directory. Additionally, files are copied to the stage.
 *   ```git checkout HEAD -- files``` copies files from the latest commit to both the stage and the working directory.

## Diff
2
3
4
5
6
7

###### $ git diff

###### $ git diff "@{yesterday}"

###### $ git diff 1b6d "master~2" { back 2 last commit }

###### $ git whatchanged --since="2 weeks ago"

## Checkout

###### $ git commit -a

###### $ git checkout HEAD~3

###### $ git commit --amend {creates a new commit with the same parent as the current commit} 


