
## Intro to version control systems

##### A number of Version Control Systems are available today (Git, Mercurial, Subversion, and others...). 

Unlike version control systems like subversion, git is a distributed version control system. What this means is that git is really great for sharing code with many individuals, and still being able to keep your changes in-sync, properly versioned, with a complete replica of the commits and repo content. 

### "It's impossible to get anything out of Git other than the exact bits you put in."
**git-scm.com - Data Assurance**

## Getting started with git config

###### $ git config --global user.name "Your Name Comes Here"
###### $ git config --global user.email you@yourdomain.example.com
###### $ git init { Initialized empty Git repository  }
###### $ git status { Checking status of a repo }
###### $ git remote add origin git@github.com:<your_username>/<your_repo>.git { add repo }

## Basic git workflows

```
Note: 
You should have already cloned the sample code to your computer. 
Please don't do it more than once. 
Having multiple copies of the code samples on your computer can cause confusion as to which one you are working with.
```

###### $ git clone https://github.com/CiscoDevNet/dne-security-code

##### git log --all --graph --decorate --oneline

###### $ git log *{ now have locally on your computer all of the files that have ever been committed to the repository }*

You can verify what branch you are working on, and the current status of your working tree with the git status command:

	$ git status

Run this on your workstation:

	$ git checkout -b mycode *{ Adding the -b option to the checkout command causes Git to create a new branch - and then switch to it.}*

**Note: If you recently cloned your repo, there might not have been any updates to the remote for you to retrieve.**

Run this on your workstation:

	$ git fetch

If you make any changes to a file under git's version control, git will know.
	
	$ git status

	$ git diff

## Reverting changes

**Need:** I made changes to a file, and now I want to revert those changes and get the original (last committed version) of the file back.

**Solution:** You can "checkout" the last version of the file to overwrite the changes you have made and restore the file to its last committed version.

	$ git checkout <file path>

**Need:** I created a branch to experiment with some changes, and now I just want to throw the whole thing out.

**Solution:** Delete the branch.
	
	$ git branch --delete --force <branch name>

**Note:** Always be careful when you see options like --hard or --force. These should be keywords that cause you to pause and think about what you are doing as you will lose some work when you run these commands. If that is your intention, proceed. If not, think twice (or three times) before running these commands.
	
**_Run this on your workstation, inserting your own name and e-mail address:_**

```
$ git config --global user.name "Your Name"
$ git config --global user.email your@email-address.com
```

## Making a commit

**Try this out by running the following commands on your workstation:**

	$ git add intro-python/git-basics/change_me.txt
	$ git commit -m "Git Commit - Done."




| Step 	| Action |	Git Commands |
| --- | --- | --- |
| 1 |	Clone the Remote Repository |	git clone <url> |
| 2 |	Create and Checkout a Local Branch |	git checkout -b new branch name |
| 3 |	Incrementally Commit Changes |	git add <new or modified file> git commit -m "Commit Message" |

## Git branch

Branching is pretty simple, you just execute the command git branch <branch name>!

###### $ git branch shakespeare { create the branch named shakespeare from current }
###### $ git branch { list all of the branches in your repo }
###### $ git checkout shakespeare { switch to exist branch }
###### $ git checkout -b new_my_branch { create and switch to new branch }

## Navigating branches

###### $ git checkout master {  switch to master }
###### $ git merge shakespeare { merge shakespeare to master }

###### $ git branch -d shakespeare { you can delete branch }

## How to stash work in progress

Now you are working with feature branch, and want to do commit without new changes

###### $ git stash { you will save changes }

Now, checkout the master branch.

Make the change, and commit your work.

Next, checkout your feature branch, and execute git stash pop. This will take the changes you have stashed, add them back to your file, and delete the stash.
	
###### $ git stash pop { return to changes }

[Usefull link ] (http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/ch01.html " Волшебство Git")


#### Inspecting Things

*  git diff - See all file changes locally
*  git log - See all commit history
*  git blame my_file - See who change 
*  git reflog - Show a log of changes to the local repository's HEAD. Good for finding lost work.

#### Undoing Things

*  git reset --hard HEAD - discard staged and unstaged changes sinc the most recent commit.
     --hard - specifies that both the staged and unstaged changes are discarded
     HEAD - specify a different commit instead of HEAD to discard changes since that commit

*  git checkout my_commit  - discard unstaged changes since my_commit

*  git revert my_commit - Undo the effects of changes in my_commit. ```revert``` makes a new commit when it undoes the changes.

* git clean -n - Delete untracked files in the local working directory.
	By default files untracked by .gitignore will not be deleted, but this behavior can be altered.

#### Tidying Things

*  git commit --amend - add your staged changes to the most recent commit. If nothing is staged just commit message

```git push <remote> <lcoal branch>:<remote branch>```
```git branch --set-upstream-to=origin/master```

Remove last commit from remote git repository

```git push origin +master^1:master``` 

### Tag
*  git push my_remote --tags - Send all local tags to the remote repo. Good for versioning changes.

#### Change Default Editor

###### $ git config --global core.editor "atom --wait"

  
