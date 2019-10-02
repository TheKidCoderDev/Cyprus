#!/usr/bin/env python

from bottle import run, get, post, request, route, response, hook, static_file
import os

@get("/getDomains")
def getDomains():
#    key = request.forms.get("key")
    domains=[]
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()
    for line in lines:
        domains.append(line.split("	").reverse())

    return dict(domains)

@post("/newDomain")
def newDomain():
#    key = request.forms.get("key")
    ip = request.forms.get("ip")
    domain = request.forms.get('domain')
    with open('/etc/hosts', 'r') as f:
        if domain in f.read():
            return {'Error':"Domain taken"}
    with open('/etc/hosts', 'a') as f:
        f.write("{}	{}".format(ip, domain))
    return {}

@post("/delDomain")
def delDomain():
#    key = request.forms.get("key")
    domain = request.forms.get('domain')
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()
    with open("/etc/hosts", "w") as f:
        for line in lines:
            if domain not in line.strip("\n"):
                f.write(line)
    return {}

@post("/restart")
def restart():
    os.system("sudo service dnsmasq stop")
    os.system("sudo service dnsmasq start")


run(reloader=True, debug=True, port=30, host='10.7.19.175')
