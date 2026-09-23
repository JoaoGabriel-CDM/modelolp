import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Logo and Crown
crown_svg = '''<svg width="24" height="24" viewBox="0 0 60 40" style="margin-bottom:-4px;"><polygon points="0,38 0,8 15,22 30,0 45,22 60,8 60,38" fill="#FFD700" stroke="#B8860B" stroke-width="1.5"/><rect x="0" y="34" width="60" height="10" rx="2" fill="#FFD700" stroke="#B8860B" stroke-width="1.2"/></svg>'''
logo_html = f'''<a href="#hero" class="logo-link" style="text-decoration:none; display:flex; align-items:center; gap:8px;">
    {crown_svg}
    <div>
      <span class="king" style="color:var(--red);">KING</span>
      <span class="shop" style="color:var(--white); font-size:1rem; letter-spacing:4px; display:block; margin-top:-4px;">SHOPPING</span>
    </div>
  </a>'''

# Replace header logo
html = re.sub(r'<div class="logo-text">\s*<span class="king">KING</span>\s*<span class="shop">SHOPPING</span>\s*</div>', logo_html.replace('var(--white)', 'var(--white)'), html, count=1)

# Replace footer logo
footer_logo_html = logo_html.replace('class="logo-link"', 'class="logo-link footer-logo-link" style="text-decoration:none; display:inline-flex; align-items:center; gap:8px; justify-content:center; margin-bottom:1rem;"')
html = re.sub(r'<div class="footer-logo"><span>KING</span> SHOPPING</div>', footer_logo_html, html)

# 2. Hero Text Updates
html = re.sub(r'<p class="hero-eyebrow">.*?</p>', '<p class="hero-eyebrow">Centro de Passos — MG</p>', html)
html = re.sub(r'<h1 class="hero-h1">.*?</h1>', '<h1 class="hero-h1">Compre tudo que precisa em<br><em>uma única loja.</em></h1>', html, flags=re.DOTALL)
html = re.sub(r'<p class="hero-sub">.*?</p>', '<p class="hero-sub">De material escolar a utilidades e eletrônicos. Compre mais pagando menos, com retirada imediata em Passos.</p>', html, flags=re.DOTALL)

# Update Address in Objections
html = re.sub(r'na loja física no Jardim Colégio', 'na loja física no Centro', html)
html = re.sub(r'Jardim Colégio, Passos — MG\.', 'Centro, Passos — MG.', html)
html = re.sub(r'Jardim Colégio, Passos – MG', 'Centro, Passos – MG', html)

# Update Address in Footer and add Google Maps link
footer_address = '''<strong>📍 R. Pres. Antônio Carlos, 110 - Centro, Passos - MG, 37900-092</strong><br>
    <strong>📱 WhatsApp:</strong> (35) 9 9999-9999<br>
    <strong>⏰ Horário:</strong> Seg–Sáb, 8h às 18h
  </p>
  <a class="btn-wpp-footer" href="https://www.google.com/maps/dir/?api=1&destination=R.+Pres.+Ant%C3%B4nio+Carlos,+110+-+Centro,+Passos+-+MG,+37900-092" target="_blank" rel="noopener noreferrer" style="background:#4285F4; margin-bottom: 1rem; margin-right: 1rem;">
    🗺️ Como Chegar / Abrir Rota no GPS
  </a>'''
html = re.sub(r'<strong>📍 Jardim Colégio.*?</p>', footer_address, html, flags=re.DOTALL)

# Move Storefront
storefront_match = re.search(r'<!-- ==================== SEÇÃO: STORE SVG ==================== -->.*?</section>', html, flags=re.DOTALL)
if storefront_match:
    storefront_html = storefront_match.group(0)
    html = html.replace(storefront_html, '') # remove from original
    # Insert after marquee
    html = html.replace('<!-- ==================== SEÇÃO: BENEFITS ==================== -->', storefront_html + '\n\n<!-- ==================== SEÇÃO: BENEFITS ==================== -->')

# Add sliding doors to SVG
# The store entrance is around x=355 to 540
# We'll create two glass doors.
doors_svg = '''
  <!-- GLASS DOORS -->
  <g class="store-doors">
    <g class="door-left">
      <rect x="355" y="268" width="92" height="172" fill="#88ccff" opacity="0.4" stroke="#444" stroke-width="2"/>
      <rect x="360" y="273" width="82" height="162" fill="none" stroke="#fff" stroke-width="1" opacity="0.5"/>
    </g>
    <g class="door-right">
      <rect x="447" y="268" width="92" height="172" fill="#88ccff" opacity="0.4" stroke="#444" stroke-width="2"/>
      <rect x="452" y="273" width="82" height="162" fill="none" stroke="#fff" stroke-width="1" opacity="0.5"/>
    </g>
  </g>
'''
html = html.replace('<!-- STORE ENTRANCE (center door) -->', doors_svg + '\n  <!-- STORE ENTRANCE (center door) -->')

# Fix numbers in SVG (110 and 106)
# Move them lower and give them a background pill or something, or move to pillars.
html = re.sub(r'<text x="780" y="200" font-family="Arial" font-size="18" fill="#888" font-weight="bold">106</text>', '<rect x="770" y="270" width="40" height="20" fill="#111"/><text x="775" y="285" font-family="Arial" font-size="14" fill="#fff" font-weight="bold">106</text>', html)
html = re.sub(r'<text x="700" y="200" font-family="Arial" font-size="18" fill="#888" font-weight="bold">110</text>', '<rect x="690" y="270" width="40" height="20" fill="#111"/><text x="695" y="285" font-family="Arial" font-size="14" fill="#fff" font-weight="bold">110</text>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
# Update CSS for doors
css_add = '''
/* Store Doors */
.door-left, .door-right {
  transition: transform 0.8s ease-in-out;
}
.doors-open .door-left {
  transform: translateX(-80px);
}
.doors-open .door-right {
  transform: translateX(80px);
}
.logo-link {
  text-decoration: none;
}
.logo-link:hover .king, .logo-link:hover .shop {
  opacity: 0.9;
}
'''
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_add)
    
# Update JS for IntersectionObserver of doors
js_add = '''
  // ==========================================================================
  // 3. STORE DOORS ANIMATION
  // ==========================================================================
  const storeFront = document.querySelector('#storefront');
  const storeDoors = document.querySelector('.store-doors');
  
  if (storeFront && storeDoors && !prefersReducedMotion) {
    const doorObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          storeDoors.classList.add('doors-open');
        } else {
          storeDoors.classList.remove('doors-open');
        }
      });
    }, { threshold: 0.4 }); // Trigger when 40% of the section is visible
    
    doorObserver.observe(storeFront);
  }
'''
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('});', js_add + '\n});')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

