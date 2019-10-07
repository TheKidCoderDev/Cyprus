#!/usr/bin/env python

from bottle import run, get, post, request, route, response, hook, static_file, auth_basic
import os
import re
import subprocess

def is_authenticated_user(user, password):
    if user == "Admin" and password == "nimda":
        return True

@route('/auth.js')
@auth_basic(is_authenticated_user)
def index():
    return static_file("auth.js", root='./panel/')

@route('/')
@auth_basic(is_authenticated_user)
def index():
    return static_file("index.html", root='./panel/')

@route('/style.css')
@auth_basic(is_authenticated_user)
def index():
    return static_file("style.css", root='./panel/')

@route('/index.js')
@auth_basic(is_authenticated_user)
def index():
    return static_file("index.js", root='./panel/')

@get("/api/getDomains")
@auth_basic(is_authenticated_user)
def getDomains():
#    key = request.forms.get("key")
    domains=[]
    with open("/etc/hosts", "r") as f:
        lines = f.readlines()
    for line in lines:
        domains.append(reversed(line.strip("\n").split("	")))

    return dict(domains)

@post("/api/newDomain")
@auth_basic(is_authenticated_user)
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

@post("/api/delDomain")
@auth_basic(is_authenticated_user)
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

@get("/api/restart")
@auth_basic(is_authenticated_user)
def restart():
    os.system("sudo service dnsmasq stop")
    os.system("sudo service dnsmasq start")

run(reloader=True, debug=True, port=80, host='0.0.0.0')
