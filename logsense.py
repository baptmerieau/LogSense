import re

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

    print(f"🔍 Tentatives SSH échouées détectées : {len(ssh_failures)}")
    unique_ips = set(ssh_failures)
    for ip in unique_ips:
        count = ssh_failures.count(ip)
        print(f"🔴 {ip} → {count} échec(s)")

if __name__ == "__main__":
    path = input("Chemin du fichier de logs à analyser : ")
    analyse_logs(path)
