#!/usr/bin/env bash
 
# Update sources
sudo apt-get update -y
 
# Git
sudo apt-get install git

# Clone project

git clone https://github.com/zachkont/dotaUpdatesBot

# AWS Cli
sudo apt-get update
sudo apt-get install -y python-pip
pip install awscli

 
# Python

sudo apt-get install python3-setuptools
sudo easy_install3 pip       # will be a Python3 pip
sudo pip install virtualenv  # will be py3
 
# mongodb
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update
sudo apt-get install -y mongodb-org

sudo service mongod start
sudo systemctl enable mongod.service

 
# Vim
sudo apt-get install vim -y
 
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle