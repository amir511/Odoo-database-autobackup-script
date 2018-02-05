# Odoo database autobackup script
This Python script performs automatic backups for your odoo instance database and uploads the backup to your git repository


## Usage

* You need to have an already configured git repository to put backups in it, and you should have a clone of the backup on your server.
* You have to simply specify the following variables in the script top:
    * REPO_PATH
    * BACKUP_FREQUENCY
* Copy your configured script to your server, preferably to : 
    
    `/opt/odoo-autobackup/`
    
* You can configure this script to run as a startup service whenever your server starts, this can be done in many ways.