#!/bin/bash

echo " Lancement des tests cloud VideoP ... ..."

python3 upload_to_s3.py
python3 dynamodb.py

echo " Déploiement cloud terminé"

