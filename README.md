# Odoo database autobackup script
This Python script performs automatic backups for your odoo instance databases and uploads the backup files to your git repository

## Warning

Depending on the version of PostgreSQL and your Odoo installation
backups may not work properly after restore when dumping them with the command in the script.
So I wrote down another two alternative commands which gives different results (commented out) in `dump_databases` function.
Please before using this script in production make sure that it will give you the appropriate results.

## Usage

* You need to have an already configured git repository to put backups in it, and you should have a clone of the repo on your server.
* The repo directory should be owned by the Postgresql user (usually named `postgres`).
* You should make sure that this repo have your credentials stored so that the script will be able to push automatically without your intervention, this can be done as follow:
    * cd to your repo directory
    * run `git config credential.helper store`
    * execute `git pull`
    * you will be asked for your username and password for the last time in this repository.
* You have to simply specify the following variables found at the top of the script:
    * `REPO_PATH`
    * `BACKUP_FREQUENCY`
* Copy your configured script to your server
* Run it with the PostgreSQL default user (usually named `postgres`) by executing first `sudo su postgres`
* You can configure this script to run at startup whenever your server starts, this can be done in many ways, one of them is :

    `sudo su postgres`

    `crontab -e`

    Then scroll down to the end of the file and add:

    `@reboot python3 <path_to_your_script>/odoo-backup.py &`

    then reboot your server

    check [this](https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu) link for other methods.


