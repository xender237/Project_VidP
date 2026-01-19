"""
Downscale Pod
-------------
Ce script prend une vidéo en entrée et la redimensionne
afin de réduire sa taille (optimisation stockage et réseau).
"""

import os
import subprocess

# Chemin de la vidéo d’entrée
INPUT_VIDEO = "/videos/input.mp4"

# Dossier de sortie
OUTPUT_DIR = "/data/downscaled"
OUTPUT_VIDEO = f"{OUTPUT_DIR}/video_downscaled.mp4"

# Création du dossier de sortie s’il n’existe pas
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Commande FFmpeg pour redimensionner la vidéo
subprocess.run([
    "ffmpeg",
    "-i", INPUT_VIDEO,
    "-vf", "scale=640:360",
    OUTPUT_VIDEO
], check=True)

print("✅ Downscale terminé avec succès")

