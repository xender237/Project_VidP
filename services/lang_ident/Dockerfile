FROM python:3.9-slim

# Installation de la librairie de détection de langue
RUN pip install langdetect

WORKDIR /app
COPY lang_ident.py .

CMD ["python", "lang_ident.py"]

