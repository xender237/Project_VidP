# Image Python légère
FROM python:3.9-slim

# Installation de FFmpeg pour le traitement vidéo
RUN apt update && apt install -y ffmpeg

# Répertoire de travail
WORKDIR /app

# Copie du script Python
COPY downscale.py .

# Commande exécutée au démarrage du container
CMD ["python", "downscale.py"]

