echo "the script was run"
ssh sebastianl@%${{secret.IP_SERVER}}
${{secret.SERVER_PASSWORD}}
systemctl restart flask-app