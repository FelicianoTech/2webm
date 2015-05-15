#!/usr/bin/env bash 

# Update Ubuntu 
apt-get update 
apt-get upgrade -y 

# Install Package Dependencies 
apt-get install git python-mysqldb python-dev python-pip ffmpeg -y 

# Install Python Pip Modules 
pip install -r /var/www/app/config/requirements.txt 

# Install and Configure MySQL 
debconf-set-selections <<< 'mysql-server mysql-server/root_password password 2webm'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 2webm'
apt-get install mysql-server -y 

mysql -u root -p2webm -e "CREATE DATABASE webm; GRANT ALL ON webm.* to 'admin' identified by '2webm';" 

# Start Flask App 
python /var/www/run.py 