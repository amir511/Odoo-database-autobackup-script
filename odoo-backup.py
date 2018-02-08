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
* Copy your configured script to your server, preferably to : 
    
    `/opt/odoo-autobackup/`
    
* You can configure this script to run as a startup service whenever your server starts, this can be done in many ways.
"""

# Constants:
# Change these constants so that they will suit your conditions
REPO_PATH = "" # Absolute path to the directory of the git repo that will hold the regular backups
BACKUP_FREQUENCY = 3600 # Number of seconds afterwhich the script will run again (1 hour = 3600 seconds)

# imports
import os
from time import sleep
from datetime import datetime

def sys_command(cmd):
	for i in os.popen(cmd):
		print(i)

def get_all_databases():
	generator = os.popen("psql --tuples-only -c '\l' | awk -F\| '{ print $1 }' | grep -E -v '(template0|template1|^$)'")
	all_dbs = []
	for i in generator:
		i = i.strip()
		if i != "":
			all_dbs.append(i)
	return all_dbs

def dump_databases(dbs):
	for db in dbs:
		filename = db+"_"+datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
		"""
		Depending on the version of postgresql and your Odoo installation
		backups may not work properly after restore when dumping them with the below command
		So I wrote down another two commands which gives alternative results (commented out)
		Please before using this script in production make sure that this script will give you the appropriate results
		"""
		sys_command("nice -n 19 pg_dump -Fp -h '/var/run/postgresql' -U 'postgres' '{db}' --file={f}".format(db=db,f=filename))
#		sys_command("nice -n 19 pg_dump --format=c --no-owner --username='postgres' --host='/var/run/postgresql' --port=5432 --dbname={db} | gzip > {f}+]'.zip'".format(db=db,f=filename))
#		sys_command("nice -n 19 pg_dump -E UTF-8 --blobs --format=c --dbname={db} | gzip>{f}+'.zip'".format(db=db,f=filename))

def remove_old_backups():
	all_files = os.listdir()
	for obj in all_files:
		if os.path.isfile(obj):
			os.remove(obj)

def add_commit_push(msg):
	sys_command('git pull --force origin master')
	sys_command('git add --all')
	sys_command("git commit -m'{}'".format(msg))
	sys_command('git push')

def main():
	while True:
		dbs = get_all_databases()
		os.chdir(REPO_PATH)
		remove_old_backups()
		add_commit_push('Automatic deletion of old database backups')
		dump_databases(dbs)
		add_commit_push('Automatic new database backups')
		sleep(BACKUP_FREQUENCY)

if __name__ == '__main__':
    main()


