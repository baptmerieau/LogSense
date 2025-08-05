# LogSense 

Outil Python pour analyser des fichiers de logs système et identifier les comportements suspects.

##  Fonctionnalités actuelles

- Analyse des logs SSH (`auth.log`)
- Détection d'adresses IP avec connexions échouées
- Affichage des IPs suspectes et nombre de tentatives

## Export des résultats

À la fin de l'analyse, vous pouvez exporter les résultats dans un fichier `.json` :



## Utilisation

```bash
git clone https://github.com/baptmerieau/LogSense.git
cd LogSense
python logsense.py
