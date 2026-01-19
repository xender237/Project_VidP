"""
DynamoDB
--------
Stocke les métadonnées vidéo.
"""

import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VideoMetadata")

# Chargement des métadonnées
with open("/data/metadata/language.json") as f:
    language = json.load(f)

with open("/data/metadata/animals.json") as f:
    animals = json.load(f)

table.put_item(
    Item={
        "video_id": "video1",
        "language": language["language_detected"],
        "animals": animals["animals_detected"],
        "status": "processed"
    }
)

print("✅ Métadonnées enregistrées dans DynamoDB")

