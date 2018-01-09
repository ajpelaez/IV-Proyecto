#!/bin/bash
USER="ubuntu"
KEYPAIR="~/AWS/ClaveAWS.pem"
FABFILE="./fabfile.py"

if (( $# == 1 )); then
  IP=$1
  fab -f $FABFILE -i $KEYPAIR -H $USER@$IP deploy_wep_app
  fab -f $FABFILE -i $KEYPAIR -H $USER@$IP start_web_app
else
  echo "Uso: provision.sh IP"
fi
