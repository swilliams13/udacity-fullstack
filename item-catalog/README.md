# Build An Item Catalog Project
by Samantha Williams, Project in [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

### Overview
The goal of this project was to develop an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

#### Key Lessons Learned
- How to develop a RESTful web application using the Python framework Flask
- Implementing third-party OAuth authentication
- When to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.
- How to create JSON endpoints

## Getting Started
Live Demo Coming Soon

### How to Run Locally
1. Install Vagrant and VirtualBox, see instructions further below
2. Download the latest VM configuration from Udacity using Github to fork and clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).
2. Clone this [repository](https://github.com/swilliams13/udacity-fullstack.git)
3. Copy the item-catalog directory into the Udacity vagrant directory
4. Launch the Vagrant VM (vagrant up)
4. Run your application within the VM (python /vagrant/item-catalog/application.py)
5. Access and test your application by visiting http://localhost:8000 locally

#### Requirements
To customize this project for your own use, you'll need:
- Python 2 or 3 installed.
    - Download the latest version of Python [here](https://www.python.org/downloads/)
- VirtualBox
- Vagrant
- Google Developer Account
- Facebook Developer Account

#### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

#### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

#### Download the VM configuration
To download the VM configuration, use Github to fork and clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.

#### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

   ```sh
   $ vagrant up
   ```

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

   ```sh
   $ vagrant ssh
   ```

   If you are alerted that a restart is required above the virtual machine's prompt upon login, you can simply:
   ```sh
   $ vagrant halt
   ```
   Then
   ```sh
   $ vagrant up
   $ vagrant ssh
   ```

Once logged in, navigate to the shared directory:
   ```sh
   cd /vagrant/item-catalog
   ```

Finally run application.py:
   ```sh
   $ python application.py
   ```

#### Logging in and out

If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM.

#### References
- [Flask] (http://flask.pocoo.org/docs/0.12/)
- [Jinja2 for Flask templates] (http://jinja.pocoo.org/docs/2.10/)
- [Bootstrap4]( https://v4-alpha.getbootstrap.com/)
- [Google Developer Console] (https://console.developers.google.com/apis)
- [Facebook Developer page] (https://developers.facebook.com/)
