#!/bin/bash
echo "the script was run"
ssh sebastianl@188.166.49.249
${{secrets.SERVER_PASSWORD}}
sudo systemctl restart flask-app