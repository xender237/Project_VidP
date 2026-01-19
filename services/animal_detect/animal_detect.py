"""
Animal Detect Pod
-----------------
Analyse quelques frames de la vidéo pour détecter
la présence d’animaux (version simplifiée TP).
"""

import cv2
import json
import os

VIDEO_PATH = "/data/downscaled/video_downscaled.mp4"
OUTPUT_FILE = "/data/metadata/animals.json"

cap = cv2.VideoCapture(VIDEO_PATH)
detections = []

frame_count = 0

# Analyse des 30 premières frames
while cap.isOpened() and frame_count < 30:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Simulation de détection
    if frame_count % 10 == 0:
        detections.append("animal_detected")

cap.release()

# Dossier de sortie
os.makedirs("/data/metadata", exist_ok=True)

# Sauvegarde des résultats
with open(OUTPUT_FILE, "w") as f:
    json.dump({"animals_detected": list(set(detections))}, f, indent=4)

print("✅ Détection d’animaux exécutée")

