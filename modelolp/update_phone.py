import os

files_to_check = [
    'index.html',
    'politica-de-privacidade.html',
    'termos-de-uso.html',
    'css/style.css',
    'js/main.js'
]

for filepath in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace wa.me links
        content = content.replace('5535999999999', '5535988186660')
        # Replace display text
        content = content.replace('(35) 9 9999-9999', '(35) 98818-6660')
        content = content.replace('(35) 99999-9999', '(35) 98818-6660')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Replacement complete")
