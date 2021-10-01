

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
 *   ```git log --all --graph --decorate```
## diff

###### $ git diff

###### $ git diff "@{yesterday}"

###### $ git diff 1b6d "master~2" { back 2 last commit }

###### $ git whatchanged --since="2 weeks ago"

```git diff``` between stage and working directory

```git diff master``` between HEAD (last commit) and working dir

```git diff --cached``` between HEAD and stage

```git diff 7b49f27aece``` between commit and working dir

```git diff hg54wd er456gg``` between commites

 

## Checkout

###### $ git commit -a

###### $ git checkout HEAD~3

###### $ git checkout HEAD~ files {  copies the files from the commit called HEAD~ (the parent of the current commit) to the working directory, and also stages it.

###### $ git commit --amend {creates a new commit with the same parent as the current commit} 

Git fans love the ability to alter a repository, rearranging things how ever they want until they push.

###### $ git checkuot -b new { new branch }

## RESET

The reset command moves the current branch to another position

###### $ git reset HEAD~1 { from last commit to stage }

###### $ git reset HEAD~1 --hard { from last commit to stage and working dir }

## Merge

A merge creates a new commit that incorporates changes from other commits. 

###### $ git merge master { fast-forward merge }

###### $ git merge other { three-way commit if no conflict }

## Cherry Pick

The cherry-pick command "copies" a commit, creating a new commit on the current branch with the same message and patch as another commit.

###### $ git cherry-pick 2c33d

## Rebase

A rebase is an alternative to a merge for combining multiple branches. Whereas a merge creates a single commit with two parents, leaving a non-linear history, a rebase replays the commits from the current branch onto another, leaving a linear history. In essence, this is an automated way of performing several cherry-picks in a row.

###### $ git rebase master

###### $ git rebase --onto master 2c335 { to limit how far back to go, use the --onto option } 

##### Squash commints
Check difference from branch __dev__
###### git cherry -v dev | wc -l
Rebase
###### git rebase -i HEAD~60

## Technical Notes

The contents of files are not actually stored in the index (.git/index) or in commit objects. Rather, each file is stored in the object database (.git/objects) as a blob, identified by its SHA-1 hash. The index file lists the filenames along with the identifier of the associated blob, as well as some other data. For commits, there is an additional data type, a tree, also identified by its hash. Trees correspond to directories in the working directory, and contain a list of trees and blobs corresponding to each filename within that directory. Each commit stores the identifier of its top-level tree, which in turn contains all of the blobs and other trees associated with that commit.

If you make a commit using a detached HEAD, the last commit really is referenced by something: the reflog for HEAD. However, this will expire after a while, so the commit will eventually be garbage collected, similar to commits discarded with git commit --amend or git rebase.



