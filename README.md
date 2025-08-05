# LogSense 

Outil Python pour analyser des fichiers de logs système et identifier les comportements suspects.

## 📊 Fonctionnalités

- Analyse des logs SSH (`auth.log`)
- Détection des IPs avec tentatives de connexion échouées
- Score de risque automatique
- Export JSON des résultats
- Interface web locale (Streamlit)

## 🚀 Lancer l'interface

pip install -r requirements.txt
streamlit run logsense.py

## Export des résultats

À la fin de l'analyse, vous pouvez exporter les résultats dans un fichier `.json` :



## Utilisation

```bash
git clone https://github.com/baptmerieau/LogSense.git
cd LogSense
python logsense.py
