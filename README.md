# VideoP – Pipeline hybride de traitement vidéo

## 1. Présentation du projet

**VideoP** est un pipeline hybride de traitement vidéo conçu dans le cadre du cours de **Cloud Computing**.  
Le projet illustre une architecture distribuée combinant :

- un **traitement local** basé sur des conteneurs Docker,
- une **agrégation et exposition des résultats dans le Cloud (AWS)**.

Le pipeline automatise le traitement de vidéos stockées localement, génère des métadonnées, puis centralise les résultats sur des services Cloud accessibles publiquement via une page web.

---

## 2. Objectifs pédagogiques

- Mettre en œuvre une architecture **hybride Local / Cloud**
- Utiliser la **conteneurisation (Docker)**
- Exploiter des services Cloud AWS (EC2, S3, DynamoDB)
- Comprendre la notion de **pipeline distribué**
- Déployer une **application accessible publiquement**
- Identifier les limites d’un déploiement Cloud académique

---

## 3. Architecture globale

### Vue d’ensemble


## 4. Structure du dépôt


---

## 5. Exécution du pipeline en local (Docker)

### 5.1 Prérequis

- Docker ≥ 20.x
- Docker Compose
- Système Linux / Windows / macOS

Vérification :
```bash
docker --version
docker compose version
```

### 5.2 Lancer le pipeline

Placer une vidéo .mp4 dans le dossier : videos/input.mp4

Lancer le pipeline :
```bash
docker compose up --build
```
---



