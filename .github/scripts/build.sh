#!/bin/bash
echo "the script was run"
ssh sebastianl@${{secrets.IP_SERVER}}
${{secrets.SERVER_PASSWORD}}
systemctl restart flask-app