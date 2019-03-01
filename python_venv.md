
https://developers.redhat.com/blog/2018/08/13/install-python3-rhel/

### Using Python virtual environments is a best practice to isolate project-specific dependencies and create reproducible environments. 

### Create a Python virtual environment (best practice)

Using Python virtual environments is a best practice to isolate project-specific dependencies and create reproducible environments. In other words, it’s a way to avoid conflicting dependencies that lead to dependency hell. Using a virtual environment will let you use 'pip' to install whatever modules you need for your project in an isolated directory under your normal user ID. You can easily have multiple projects with different dependencies. To work on a specific project, you activate the virtual environment, which adds the right directories to your path(s).

Using virtual environments along with 'pip list', 'pip freeze', and a 'requirements.txt' file gives you a path to a reproducible environment to run your code it. Others that need to run your code can use the 'requirements.txt' file you generate to create a matching environment.

By default, virtual environments will not use any system installed modules, or modules installed under your home directory. From an isolation perspective and for creating reproducible environments this is generally considered the correct behavior. However, you can change that by using the argument '--system-site-packages'.

To avoid surprises, don’t type python. Use an explicit version number in the command, such as python3.6 or python2.7.

### Do not run pip install as root (or with sudo)



