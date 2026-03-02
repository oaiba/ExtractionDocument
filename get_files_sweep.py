import os
import re

content_dir = r"d:\BaProject\ExtractionDocument\content"
tracker_dir = os.path.join(content_dir, "Tracker")

replacements = {
    "Viper": "Mamba", "VIPER": "MAMBA",
    "Blaze": "Ignition", "BLAZE": "IGNITION",
    "Havoc": "Tartarus", "HAVOC": "TARTARUS",
    "Doc": "Suture", "DOC": "SUTURE",
    "Angel": "Aegis", "ANGEL": "AEGIS",
    "Phantom": "Sonar", "PHANTOM": "SONAR",
    "Specter": "Mirage", "SPECTER": "MIRAGE",
    "Wraith": "Obsidian", "WRAITH": "OBSIDIAN",
    "Bulwark": "Bastion", "BULWARK": "BASTION",
    "Fortress": "Goliath", "FORTRESS": "GOLIATH",
    "Cipher": "Glitch", "CIPHER": "GLITCH",
    "Flux": "Pulse", "FLUX": "PULSE"
}

pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in replacements.keys()) + r')\b')
matched_files = set()

for root, dirs, files in os.walk(content_dir):
    if tracker_dir in root:
        continue
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if pattern.search(content):
                    matched_files.add(file_path)
            except Exception as e:
                pass

with open(r"d:\BaProject\ExtractionDocument\matched_files.txt", "w", encoding="utf-8") as f:
    for file_path in sorted(matched_files):
        f.write(file_path + "\n")
