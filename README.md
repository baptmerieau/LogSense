# LogSense 

Outil Python pour analyser des fichiers de logs système et identifier les comportements suspects.

##  Fonctionnalités actuelles

- Analyse des logs SSH (`auth.log`)
- Détection d'adresses IP avec connexions échouées
- Affichage des IPs suspectes et nombre de tentatives

## Utilisation

```bash
git clone https://github.com/baptmerieau/LogSense.git
cd LogSense
python logsense.py
