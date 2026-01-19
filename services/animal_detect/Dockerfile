FROM python:3.9-slim

# Dépendances nécessaires pour OpenCV
RUN apt update && apt install -y \
    ffmpeg \
    libgl1

RUN pip install opencv-python numpy

WORKDIR /app
COPY animal_detect.py .

CMD ["python", "animal_detect.py"]

