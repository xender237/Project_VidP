"""
LangIdent Pod
-------------
Détecte la langue parlée (simulation via texte).
"""

from langdetect import detect
import json
import os

# Texte simulant une transcription audio
TEXT_SAMPLE = "Bonjour, ceci est une démonstration du pipeline VideoP."

# Détection de la langue
language = detect(TEXT_SAMPLE)

# Métadonnées générées
metadata = {
    "language_detected": language
}

# Dossier de sortie
os.makedirs("/data/metadata", exist_ok=True)

# Sauvegarde des métadonnées
with open("/data/metadata/language.json", "w") as f:
    json.dump(metadata, f, indent=4)

print(f"✅ Langue détectée : {language}")

