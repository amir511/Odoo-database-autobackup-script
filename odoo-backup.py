#! usr/bin/python3
"""
Odoo database autobackup script
===============================
This Python script performs automatic backups for your odoo instance database and uploads the backup to your git repository

Author: Amir Anwar
Email: amir.anwar.said@gmail.com
Github: https://github.com/amir511


Usage
=====
* You need to have an already configured git repository to put backups in it, and you should have a clone of the backup on your server.
* You should make sure that this repo have your credentials stored so that the script will be able to push automatically without your intervention, this can be done as follow:
    * cd to your repo directory
    * run `git config credential.helper store`
    * execute `git push`
    * you will be asked for your username and password for the last time in this repository.
* You have to simply specify the following variables in the script top:
    * REPO_PATH
    * BACKUP_FREQUENCY
    * SUDO_PASSWORD (if needed)
* Copy your configured script to your server, preferably to : 
    
    `/opt/odoo-autobackup/`
    
* You can configure this script to run as a startup service whenever your server starts, this can be done in many ways.
"""

# Constants:
# Change these constants so that they will suit your conditions
REPO_PATH = "" # Absolute path to the directory of the git repo that will hold the regular backups
BACKUP_FREQUENCY = 3600 # Number of seconds afterwhich the script will run again (1 hour = 3600 seconds)
SUDO_PASSWORD = '' # This is the password that will be used to change to the database user via 'sudo su postgres',
                   # leave it blank if there is no password, or if you want to connect via postgres password i.e. 'su postgres'
# other configurations that might also be needed depending on your system configuration:
DB_USER = 'postgres' # this is the default database username, usually you don't need to change this, change it only if your postgresql was installed on a different user,
                     # This is not to be confused with the odoo user that has a role in the db
DB_USER_PASSWORD = ''   # password of the postgres user, only specify if the postgres has a password already, if not specified, the script will automatically 
                        # change user via 'sudo'

# imports
import os
from time import sleep
from datetime import datetime

def change_directory(dir):
    pass

def change_user():
    pass

def get_all_databases():
    pass

def dump_databases():
    pass

def remove_old_backups():
    pass

def commit_and_push():
    pass



