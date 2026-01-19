"""
Subtitle Pod
------------
Génère des sous-titres au format SRT (simulation).
"""

import os

subtitle_content = """1
00:00:01,000 --> 00:00:04,000
Bienvenue sur la plateforme VideoP.

2
00:00:05,000 --> 00:00:08,000
Pipeline hybride de traitement vidéo.
"""

# Dossier de sortie
os.makedirs("/data/subtitles", exist_ok=True)

# Écriture du fichier SRT
with open("/data/subtitles/subtitles.srt", "w") as f:
    f.write(subtitle_content)

print("✅ Sous-titres générés")

