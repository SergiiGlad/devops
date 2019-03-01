
## The Python behind the curtain

https://developers.redhat.com/blog/2018/11/14/python-in-rhel-8/

### Python 3 was first released in 2008. Today, in 2018, the python == python2 side is more popular, even among those that prefer Python 3 (which they spell out as python3).

Always use the explicit version in these cases. 
Better yet, don’t rely on the wrapper scripts for pip, venv and other Python modules that you call from the command line.  

#### Instead use 

``` python3 -m pip ``` 
``` python3 -m venv ``` 
``` python2 -m virtualenv ```

### To install a third-party package, many sources on the Internet will suggest using `sudo pip install` **Do not do this!** This command translates to “download a package from the internet, and run it on my machine as root to install it”.

### Even if the package is **trustworthy**, this is a bad idea.

### If you want to use third-party packages, create a virtual environment using `python3 -m venv --system-site-packages myenv ` or `python2 -m virtualenv --system-site-packages myenv`
### Then, activate the environment using `source myenv/bin/activate` and install packages into it using `pip install`.

### The packages will then be available as long as the environment is activated. While this does not protect you against malicious packages, it does protect the system from unexpected breakage.

### (or if you prefer being explicit, 'python -m pip install requests').
### The **--system-site-packages** switch makes the environment re-use libraries installed system-wide. 

**Note:** Use the `deactivate` command to exit out of an active virtual environment.

## Takeaways

To install or run Python, use python3 – unless you have a different version in mind.

Do not use sudo pip.

And if you have some code for Python 2, now is a great time to start modernizing it.

Enjoy Python!
