## Module 2. Example
__As for help the best way to find smth is find it on official documentation:__
<https://git-scm.com/docs>
__Or read a free book Pro git__
<https://git-scm.com/book/en/v2>
__Online or download it offline using in different formats.__
 
As for config I would recommend to use only __global__ and __local__ config unless You configure some CI server or chestrator server and want to make some config options available for all users. In that case __system__ option is the best way to do it.
 
__As an example of it we can use default push behaviour.__        
```
git config --system push.default none
```
__And each user should specify branch name during push all the time by default. Or editor config:__
```
git config --system core.editor “/path/to/editor --editor_param1=smth --editor_param2-smth, ...”
```
__But the best example is git configuration like:__
__Proxy setting:__
```git config --system core.gitproxy '"proxy command" for example.com'```
__Garbage collector settings:__
```git config --system gc.auto 0```
 
Etc…
 
__Git clone commands is also not that simple.__
__With standard set of params we an use it to clone only one branch and each pull__ __just downloads only objects from that branch ignoring all other objects and__ __branches, or last snapshot for some that branch, or 5 latest snapshots but still be__ __able to push into that branch.__
```
git clone git@url.com:user/repo --branch <name>
```
__Will clone repo and checkout to that branch (master by default) but__
```
git clone git@url.com:user/repo --branch <name> --single-branch
```
__Clone only that branch. Basically it clones only history of that branch.__
```
git clone git@url.com:user/repo --branch <name> --depth=1
```
__Clone last commit from branch name. By default --depth invokes --single-branch.__
 
__Bare repo, is a repo that contains only objects that never unpacked. Basically bare repo is a pure .git directory.__

```
git clone git@url.com:user/repo --bare
```
__Will clone objects but never unpack it into working directory. From the other hand it allows you to clone from this directory and pushed into it. E.g. If you clone .git directory of existing project you can’t push into it by default.__

## Modules 3

### Branching: manual


List, create or delete branches
![alt text](images/branching.png)
```bash
git branch

git branch --remotes/-r

git branch --all/-a

git branch --list/-l *sql*

git branch --contains 07e5q56

git branch newbranch

git branch newbranch 07e5q56

git branch -d newbranch
```
## Commintting

![alt text](images/committing.png)

## Tagging

 * lightweight
 * annotated tags

 ![alt text](images/tagging1.png)

 ![alt text](images/tagging2.png)

 ## Lead the way

 ![alt text](images/checkout.png)