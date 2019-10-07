#!/usr/bin/env python

from bottle import run, get, post, request, route, response, hook, static_file
import os
import re
import subprocess

@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@get("/getDomains")
def getDomains():
#    key = request.forms.get("key")
    domains=[]
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()
    for line in lines:
        domains.append(reversed(line.strip("\n").split("	")))

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
        f.write("{}	{}\n".format(ip, domain))
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

@get("/restart")
def restart():
    os.system("sudo service dnsmasq stop")
    os.system("sudo service dnsmasq start")

run(reloader=True, debug=True, port=30, host='0.0.0.0')
