# Logs Analysis Project
by Samantha Williams, Project in [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

### Project Overview
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

This project will answer the following 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


### How to Run
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

#### Installing the Virtual Machine
You'll use a virtual machine (VM) to run an SQL database server and python to run the log analysis program.

#### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

#### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

#### Download the VM configuration
To download the VM configuration, use Github to fork and clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.

#### Download the data
Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.
We will do that later when we log into the virtual machine.


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
   cd /vagrant
   ```

If you didn't already extract the newsdata SQL script, run:
   ```sh
   $ unzip newsdata.zip
   ```

Now populate the database with test data using this command:
   ```sh
   $ psql -d news -f newsdata.sql

   ```

Here's what this command does:

  psql — the PostgreSQL command line program
  -d news — connect to the database named news which has been set up for you
  -f newsdata.sql — run the SQL statements in the file newsdata.sql
  Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

Finally run analysis.py:
   ```sh
   $ python analysis.py
   ```


## EXPECTED OUTPUT
````
MOST POPULAR THREE ARTICLES OF ALL TIME
    "Candidate is jerk, alleges rival" - 338647 views
    "Bears love berries, alleges bear" - 253801 views
    "Bad things gone, say good people" - 170098 views

MOST POPULAR ARTICLE AUTHORS OF ALL TIME
    Ursula La Multa - 507594 views
    Rudolf von Treppenwitz - 423457 views
    Anonymous Contributor - 170098 views
    Markoff Chaney - 84557 views

DAYS WITH MORE THAN 1% REQUEST ERRORS
    July 17, 2016 - 2.3% errors

````

#### Logging in and out

If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM.



#### Requirements
To customize this project for your own use, you'll need:
- Python 2 or 3 installed.
  - Download the latest version of Python [here](https://www.python.org/downloads/)
