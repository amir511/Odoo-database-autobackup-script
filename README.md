# Odoo database autobackup script
This Python script performs automatic backups for your odoo instance database and uploads the backup to your git repository


## Usage

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