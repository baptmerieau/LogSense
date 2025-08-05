import re
import json
from collections import Counter
import streamlit as st

def analyse_logs(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        logs = file.readlines()

    ssh_failures = []
    for line in logs:
        if "Failed password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                ssh_failures.append(ip)

    ip_counts = Counter(ssh_failures)

    # Score simple : 1 tentative = 10 points
    scored_data = {ip: {'attempts': count, 'risk_score': count * 10} for ip, count in ip_counts.items()}
    return scored_data

def export_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.title("🔍 LogSense – Analyse des logs SSH")
    uploaded_file = st.file_uploader("Dépose ton fichier de log (ex: auth.log)", type=["log", "txt"])

    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
        with open("temp_log.log", "w") as temp:
            for line in content:
                temp.write(line + "\n")

        result = analyse_logs("temp_log.log")
        st.success(f"{len(result)} IPs détectées")

        if result:
            st.subheader("Résultats")
            for ip, data in result.items():
                st.write(f"🔴 **{ip}** → {data['attempts']} tentatives, score : {data['risk_score']}")

            if st.button("📦 Exporter en JSON"):
                export_to_json(result, "resultats_logsense.json")
                st.success("Fichier `resultats_logsense.json` créé.")

if __name__ == "__main__":
    main()
