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

# Combine all keys into a single regex. Boundaries require non-alphanumeric.
pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in replacements.keys()) + r')\b')

for root, dirs, files in os.walk(content_dir):
    # Exclude Tracker directory
    if tracker_dir in root:
        continue
        
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                for i, line in enumerate(lines):
                    matches = pattern.findall(line)
                    if matches:
                        match_str = ", ".join(set(matches))
                        print(f"MATCH_FOUND|{file_path}|{i+1}|{match_str}|{line.strip()}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
