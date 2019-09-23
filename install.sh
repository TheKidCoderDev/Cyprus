#!/bin/bash

apt-get install dnsmasq -y

echo "What Top-Level Domain should we use: "
read TLD

IP="$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')"

echo "$IP	admin.$TLD" >> /etc/hosts

echo "listen-address=127.0.0.1" >> /etc/dnsmasq.conf
echo "listen-address=$IP" >> /etc/dnsmasq.conf
