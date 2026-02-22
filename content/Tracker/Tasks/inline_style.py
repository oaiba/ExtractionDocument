import glob
import os

path = r'd:\UE_Project\ExtractionDocument\content\Tracker\Tasks\Phase*.md'
for filepath in glob.glob(path):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Apply inline style to <details>
    text = text.replace('<details><summary>', '<details style="display: inline-block; width: 95%; vertical-align: top;"><summary>')
    # Just in case it was already applied or had spaces
    text = text.replace('<details >', '<details>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
print("Updated all files.")
