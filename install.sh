#!/bin/bash

apt-get install dnsmasq -y
apt-get install tmux -y

npm install -g http-server

IP="$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')"

echo "$IP	admin.cyp" > /etc/hosts

echo "listen-address=127.0.0.1" >> /etc/dnsmasq.conf
echo "listen-address=$IP" >> /etc/dnsmasq.conf
sudo service dnsmasq stop
sudo service dnsmasq start

sudo chmod a+x run.sh

sudo chmod a+x api.py
sudo ./api.py
