import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir comentarios
content = content.replace('<!-- HEADER -->', '<!-- ==================== SEÇÃO: HEADER ==================== -->')
content = content.replace('<!-- HERO -->', '<!-- ==================== SEÇÃO: HERO ==================== -->')
content = content.replace('<!-- MARQUEE -->', '<!-- ==================== SEÇÃO: MARQUEE ==================== -->')
content = content.replace('<!-- BENEFITS -->', '<!-- ==================== SEÇÃO: BENEFITS ==================== -->')
content = content.replace('<!-- OBJECTIONS -->', '<!-- ==================== SEÇÃO: OBJECTIONS ==================== -->')
content = content.replace('<!-- STORE SVG -->', '<!-- ==================== SEÇÃO: STORE SVG ==================== -->')
content = content.replace('<!-- SOCIAL PROOF -->', '<!-- ==================== SEÇÃO: SOCIAL PROOF ==================== -->')
content = content.replace('<!-- FOOTER -->', '<!-- ==================== SEÇÃO: FOOTER ==================== -->')
content = content.replace('<!-- FLOATING WPP BUTTON -->', '<!-- ==================== SEÇÃO: FLOATING WPP BUTTON ==================== -->')

# Adicionar links legais no footer
footer_links = '''<div class="footer-links">
    <a href="politica-de-privacidade.html">Política de Privacidade</a> | 
    <a href="termos-de-uso.html">Termos de Uso</a>
  </div>'''
  
content = content.replace('<p class="footer-copy">', f'{footer_links}\n  <p class="footer-copy">')

# Substituir o script JS
script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
content = script_pattern.sub('<script src="js/main.js" defer></script>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
