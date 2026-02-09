import os
import re

search_path = r"d:\BaProject\ExtractionDocument\GDD_Technical"
pattern = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', re.IGNORECASE)

print(f"Scanning {search_path} for Vietnamese characters...")

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if pattern.search(line):
                            print(f"Match in {file_path} at line {i+1}: {line.strip()[:100]}...")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
