
## Intro to version control systems

##### A number of Version Control Systems are available today (Git, Mercurial, Subversion, and others...). 

### "It's impossible to get anything out of Git other than the exact bits you put in."
**git-scm.com - Data Assurance**

## Basic git workflows

```
Note: 
You should have already cloned the sample code to your computer. 
Please don't do it more than once. 
Having multiple copies of the code samples on your computer can cause confusion as to which one you are working with.
```

###### $ git clone https://github.com/CiscoDevNet/dne-security-code

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


