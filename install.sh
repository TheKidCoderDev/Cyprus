#!/bin/bash

apt-get install dnsmasq -y

echo "What Top-Level Domain should we use: "
read tld

echo "127.0.0.1	admin.$tld" >> /etc/hosts
