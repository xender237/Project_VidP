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

Machine locale (Edge)
│
├── Vidéos (.mp4)
├── Pipeline Docker
│ ├── Downscale Pod
│ ├── LangIdent Pod
│ ├── Subtitle Pod
│ └── Animal Detect Pod
│
└── Résultats (data/)
↓
Cloud AWS
│
├── EC2 (VM)
│ ├── Scripts d’upload
│ ├── Serveur Web (NGINX)
│
├── S3 (stockage vidéos)
└── DynamoDB (métadonnées)


