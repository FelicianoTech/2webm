#!/usr/bin/env bash 

# Update Ubuntu 
apt-get update 
apt-get upgrade -y 

# Create Symbolic Link 
ln -fs /vagrant /var/www 

# Install Package Dependencies 
apt-get install python-dev python-pip ffmpeg -y 

# Install Python Pip Modules 
pip install -r /var/www/app/config/requirements.txt 

