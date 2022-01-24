# Continuous deployment flask-app

![example workflows](https://github.com/SebastianLomme/flask-app-cd/actions/workflows/python-app.yml/badge.svg)
[![Website monip.org](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)](http://167.99.35.30)

main server ip: 167.99.35.30
staging server ip: 167.71.74.5

this repository is setup for continuous deploment this means that when you push a commit to the main branch the followings steps will be executed!
- ubuntu environment is setup for tests
- all dependencies are installed
- the code is checkt for syntax errors
- all test from pytest are executed
- if test fail or syntax errors are found de actions are stopt
- else a connection to de vps is set up
- directed to correct folder
- git pull is done
- than a system restart of the app is done

## The problems that i encountered
- The first problom was that i tried to connect to the svp within the github action. with ssh root@<ip-address> this dit nog work. so i search the markplace for a package i could use. I found this package of appleboy/ssh-action@master which was easy to use

- The second problom was that i did not want to give root acces to the cd. I made a new user. but then i couldn't run any more commands for sudo. The first solution was to give the user sudo access. And make sure it didn't require a password
The problom now was that still all sudo commands could be used. So i changed it to only accept the systemctl restart flask-app command.

```bash
    echo "user ALL=(ALL:ALL) NOPASSWD:ALL"  >>  /etc/sudoers.d/user
```

```bash
    echo "user ALL=(ALL:ALL) NOPASSWD: /bin/systemctl restart flask-app"  >>  /etc/sudoers.d/user
```
- The third problom was that when i started adding a database. I kept running into errors.
To make sure this wouldn't happen in a live application. I set up a staging server linked to the develop branch. so when i push to the develop branch. The application deployed on the staging server. 
The problem with the database was that it kept saying that it only had read-only permissions.
first i had the flask-app-cd.service file setup with `DynamicUser=yes`. This means that a temporary user is created every time, who didn't have the right permissions to write to the database. I changed this to a specific user with the correct permissions to write to the database. Like so `User=sebastian, Group=www-data`



