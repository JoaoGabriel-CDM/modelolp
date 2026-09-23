import re

# 1. Get header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header
header_match = re.search(r'<!-- ==================== SEÇÃO: HEADER ==================== -->\n<header role="banner">.*?</header>', index_html, re.DOTALL)
header_str = header_match.group(0)

# Extract footer
footer_match = re.search(r'<!-- ==================== SEÇÃO: FOOTER ==================== -->\n<footer role="contentinfo">.*?</footer>', index_html, re.DOTALL)
footer_str = footer_match.group(0)

# 2. Update legal pages
for page in ['politica-de-privacidade.html', 'termos-de-uso.html']:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace header
    html = re.sub(r'<!-- ==================== SEÇÃO: HEADER ==================== -->\n<header>.*?</header>', header_str, html, flags=re.DOTALL)
    
    # Replace footer
    html = re.sub(r'<!-- ==================== SEÇÃO: FOOTER ==================== -->\n<footer>.*?</footer>', footer_str, html, flags=re.DOTALL)
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated legal pages")
