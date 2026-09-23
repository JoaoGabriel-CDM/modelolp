import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. LOGO ADJUSTMENT
logo_pattern = r'<span class="king"(.*?)>KING</span>\s*<span class="shop"(.*?)>SHOPPING</span>'
replacement = r'<span class="king logo-king"\1>KING</span>\n      <span class="shop logo-shopping"\2>SHOPPING</span>'
html = re.sub(logo_pattern, replacement, html)

crown_pattern = r'<svg width="24" height="24" viewBox="0 0 60 40"'
html = html.replace(crown_pattern, '<svg class="logo-crown" viewBox="0 0 60 40"')

# 2. HERO CTA BUTTON
cta_pattern = r'<a class="btn-hero" href="#benefits">Ver Ofertas Disponíveis Hoje ↓</a>'
new_cta = '<a href="#storefront" class="btn-primary pulse" style="display:inline-flex; align-items:center; justify-content:center; gap:8px;">Ver Ofertas Disponíveis Hoje <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg></a>'
html = html.replace(cta_pattern, new_cta)

# Make sure CSS has scroll-behavior
# (Already there in style.css: html { scroll-behavior: smooth; })

# 3. STOREFRONT SVG UPDATE
# Replace backpacks wall with diverse items
backpacks_start = html.find('<!-- Backpack wall grid — right half -->')
backpacks_end = html.find('<!-- PRICE TAGS on shelves (small white rectangles) -->')

diverse_items = '''<!-- DIVERSE STORE ITEMS -->
  <!-- Electronics Boxes -->
  <rect x="385" y="270" width="40" height="30" fill="#ddd" rx="2"/>
  <rect x="390" y="275" width="30" height="20" fill="#333" rx="1"/>
  <rect x="435" y="260" width="35" height="40" fill="#555" rx="2"/>
  <circle cx="452" cy="280" r="12" fill="#222"/>
  <rect x="480" y="270" width="50" height="30" fill="#eee" rx="2"/>
  <rect x="485" y="275" width="40" height="20" fill="#0055ff"/>
  
  <!-- Kitchenware -->
  <path d="M550 280 Q560 300 570 280 Z" fill="#ff4444"/>
  <rect x="555" y="265" width="10" height="15" fill="#ff4444"/>
  <path d="M590 285 Q600 305 610 285 Z" fill="#44aa44"/>
  <rect x="595" y="270" width="10" height="15" fill="#44aa44"/>
  <circle cx="640" cy="285" r="15" fill="#ddd"/>
  <circle cx="640" cy="285" r="10" fill="#fff"/>
  
  <!-- Toys & Stationery -->
  <rect x="670" y="270" width="20" height="30" fill="#ffcc00"/>
  <rect x="695" y="270" width="20" height="30" fill="#ff44aa"/>
  <rect x="720" y="270" width="20" height="30" fill="#44ccff"/>
  <circle cx="760" cy="285" r="15" fill="#ff0000"/>
  <rect x="755" y="270" width="10" height="15" fill="#222"/>
  <circle cx="800" cy="280" r="12" fill="#00ccff"/>
  <circle cx="830" cy="285" r="14" fill="#ffaa00"/>
  <rect x="850" y="260" width="25" height="40" fill="#aa44ff"/>

  <!-- Row 2 -->
  <!-- More diverse items -->
  <rect x="385" y="330" width="45" height="25" fill="#ffbb00" rx="2"/>
  <rect x="440" y="325" width="30" height="30" fill="#44ffaa" rx="15"/>
  <rect x="480" y="320" width="40" height="35" fill="#ff4444" rx="3"/>
  <path d="M540 330 L560 350 L580 330 Z" fill="#4488ff"/>
  <rect x="600" y="330" width="35" height="25" fill="#ccaaee" rx="2"/>
  <rect x="645" y="320" width="20" height="35" fill="#ff8800" rx="2"/>
  <rect x="670" y="320" width="20" height="35" fill="#ff8800" rx="2"/>
  <circle cx="720" cy="340" r="16" fill="#00aa55"/>
  <rect x="750" y="330" width="50" height="25" fill="#ddd" rx="2"/>
  <circle cx="765" cy="342" r="8" fill="#333"/>
  <circle cx="785" cy="342" r="8" fill="#333"/>
  <rect x="810" y="325" width="30" height="30" fill="#ff22aa"/>
  <rect x="850" y="335" width="40" height="20" fill="#22ccff"/>
'''
if backpacks_start != -1 and backpacks_end != -1:
    html = html[:backpacks_start] + diverse_items + html[backpacks_end:]

# Add glass reflections over side windows
glass_svg = '''
  <!-- GLASS PANELS & REFLECTIONS -->
  <g class="glass-windows">
    <!-- Left Window -->
    <rect x="0" y="268" width="355" height="172" fill="#88ccff" opacity="0.1" pointer-events="none"/>
    <polygon points="50,268 150,268 50,440" fill="#ffffff" opacity="0.1" pointer-events="none"/>
    <polygon points="180,268 220,268 120,440 80,440" fill="#ffffff" opacity="0.05" pointer-events="none"/>
    
    <!-- Right Window -->
    <rect x="540" y="268" width="360" height="172" fill="#88ccff" opacity="0.1" pointer-events="none"/>
    <polygon points="650,268 750,268 650,440" fill="#ffffff" opacity="0.1" pointer-events="none"/>
    <polygon points="780,268 820,268 720,440 680,440" fill="#ffffff" opacity="0.05" pointer-events="none"/>
  </g>
'''
html = html.replace('<!-- STORE ENTRANCE (center door) -->', glass_svg + '\n  <!-- STORE ENTRANCE (center door) -->')

# Add pointer to svg wrapper
html = html.replace('<div class="svg-wrapper reveal">', '<div class="svg-wrapper reveal" id="storefront-svg-wrapper" title="Clique para entrar na loja!">')

# 5. NEW SECTION "INSIDE STORE"
inside_store_html = '''
<!-- ==================== SEÇÃO: INSIDE STORE ==================== -->
<section id="inside-store">
  <div class="max-w center">
    <h2 class="section-title">Bem-vindo à King Shopping! <br>O que você procura hoje?</h2>
    <button id="btn-exit-store" class="btn-secondary">← Sair da Loja</button>
  </div>
  
  <div class="catalog-grid max-w">
    <div class="catalog-card">
      <div class="catalog-icon">🎧</div>
      <h3>Eletrônicos</h3>
      <p>Fones de ouvido, caixas de som, cabos, carregadores e acessórios.</p>
      <a href="https://wa.me/5535999999999?text=Oi!%20Quero%20ver%20os%20eletrônicos." class="btn-catalog" target="_blank">Ver preços no WhatsApp</a>
    </div>
    <div class="catalog-card">
      <div class="catalog-icon">🧸</div>
      <h3>Brinquedos</h3>
      <p>Pelúcias, carrinhos, bonecas, jogos de tabuleiro e educativos.</p>
      <a href="https://wa.me/5535999999999?text=Oi!%20Quero%20ver%20os%20brinquedos." class="btn-catalog" target="_blank">Ver preços no WhatsApp</a>
    </div>
    <div class="catalog-card">
      <div class="catalog-icon">🍳</div>
      <h3>Utilidades do Lar</h3>
      <p>Potes, panelas, utensílios de cozinha, decoração e organização.</p>
      <a href="https://wa.me/5535999999999?text=Oi!%20Quero%20ver%20as%20utilidades." class="btn-catalog" target="_blank">Ver preços no WhatsApp</a>
    </div>
    <div class="catalog-card">
      <div class="catalog-icon">🎒</div>
      <h3>Papelaria e Escolar</h3>
      <p>Mochilas, cadernos, canetas coloridas, agendas e materiais.</p>
      <a href="https://wa.me/5535999999999?text=Oi!%20Quero%20ver%20a%20papelaria." class="btn-catalog" target="_blank">Ver preços no WhatsApp</a>
    </div>
  </div>
</section>
'''
html = html.replace('<!-- ==================== SEÇÃO: BENEFITS ==================== -->', inside_store_html + '\n<!-- ==================== SEÇÃO: BENEFITS ==================== -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# UPDATE CSS
css_updates = '''
/* 1. Logo Adjustments */
.logo-crown { width: 36px; height: 36px; margin-bottom: -6px; }
.logo-king { font-size: 2.5rem; font-weight: 900; }
.logo-shopping { font-size: 1rem !important; letter-spacing: 6px !important; margin-top: -6px !important; font-weight: 600; }

/* 2. Hero CTA Button */
.btn-primary {
  background: var(--red);
  color: var(--white);
  font-weight: 900;
  font-size: 1.1rem;
  padding: 1rem 2.2rem;
  border-radius: 50px;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: background 0.2s, transform 0.2s;
  box-shadow: 0 4px 15px rgba(204,0,0,0.4);
}
.btn-primary:hover {
  background: var(--red-bright);
  transform: translateY(-2px);
}
.pulse {
  animation: pulse-btn 2.2s infinite;
}

/* 4 & 5. Gamification and Inside Store */
#storefront-svg-wrapper {
  cursor: pointer;
  transition: transform 1s cubic-bezier(0.645, 0.045, 0.355, 1), filter 1s ease, opacity 1s ease;
  transform-origin: 50% 70%; /* Center near the door */
}

body.enter-store #storefront-svg-wrapper {
  transform: scale(8);
  filter: blur(4px) brightness(0.2);
  opacity: 0;
  pointer-events: none;
}

#inside-store {
  display: none;
  opacity: 0;
  padding: 4rem 1.25rem;
  background: var(--dark);
}

.catalog-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin-top: 2rem;
}
@media (min-width: 600px) { .catalog-grid { grid-template-columns: 1fr 1fr; } }

.catalog-card {
  background: var(--dark2);
  border: 1px solid #333;
  border-radius: var(--radius);
  padding: 2rem 1.5rem;
  text-align: center;
  transition: transform 0.25s, border-color 0.25s;
}
.catalog-card:hover {
  transform: translateY(-5px);
  border-color: var(--gold);
}
.catalog-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}
.catalog-card h3 {
  color: var(--gold);
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
.catalog-card p {
  color: #ccc;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}
.btn-catalog {
  display: inline-block;
  background: #25d366;
  color: #fff;
  padding: 0.6rem 1.2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: bold;
  font-size: 0.85rem;
  transition: background 0.2s;
}
.btn-catalog:hover { background: #1db954; }

.btn-secondary {
  background: transparent;
  color: #ccc;
  border: 1px solid #555;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s, color 0.2s;
  margin-bottom: 2rem;
}
.btn-secondary:hover {
  background: #333;
  color: #fff;
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_updates)

# UPDATE JS
js_updates = '''
  // ==========================================================================
  // 4. GAMIFIED STORE ENTRANCE
  // ==========================================================================
  const svgWrapper = document.getElementById('storefront-svg-wrapper');
  const insideStore = document.getElementById('inside-store');
  const btnExit = document.getElementById('btn-exit-store');
  const benefitsSec = document.getElementById('benefits');
  const storefrontSec = document.getElementById('storefront');

  if (svgWrapper && insideStore) {
    svgWrapper.addEventListener('click', () => {
      // Abre as portas antes de dar o zoom
      storeDoors.classList.add('doors-open');
      
      // Inicia a animação de zoom-in
      document.body.classList.add('enter-store');
      
      // Após 1 segundo (tempo da transição CSS)
      setTimeout(() => {
        storefrontSec.style.display = 'none';
        // benefitsSec.style.display = 'none'; // Opção: esconder o resto
        
        insideStore.style.display = 'block';
        // Pequeno delay para a transição de opacidade funcionar
        setTimeout(() => {
          insideStore.style.opacity = '1';
        }, 50);
        
        // Scrolla para o catálogo automaticamente
        insideStore.scrollIntoView({ behavior: 'smooth' });
      }, 900);
    });
    
    // Reverse animation
    if (btnExit) {
      btnExit.addEventListener('click', () => {
        insideStore.style.opacity = '0';
        
        setTimeout(() => {
          insideStore.style.display = 'none';
          storefrontSec.style.display = 'block';
          
          // Volta as propriedades
          setTimeout(() => {
            document.body.classList.remove('enter-store');
            storeDoors.classList.remove('doors-open');
            storefrontSec.scrollIntoView({ behavior: 'smooth' });
          }, 50);
        }, 500);
      });
    }
  }
'''

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# insert before last });
js = js.replace('});', js_updates + '\n});')
with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

