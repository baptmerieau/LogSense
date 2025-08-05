import re
import json
from collections import Counter

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
    print(f"\n🔍 Tentatives SSH échouées détectées : {sum(ip_counts.values())}\n")
    for ip, count in ip_counts.items():
        print(f"🔴 {ip} → {count} échec(s)")

    return ip_counts

def export_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"\n📦 Résultats exportés vers {output_file}")

if __name__ == "__main__":
    path = input("Chemin du fichier de logs à analyser : ")
    result = analyse_logs(path)

    save = input("Souhaitez-vous exporter les résultats en JSON ? (o/n) : ").lower()
    if save == 'o':
        output = input("Nom du fichier de sortie (ex: resultats.json) : ")
        export_to_json(result, output)
