import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Working hours
html = html.replace('Seg–Sáb, 8h às 18h', 'Seg-Sex, 8h às 18h | Sáb, 8h às 16h')

# Footer buttons alignment
footer_buttons_pattern = r'<a class="btn-wpp-footer" href="https://www.google.com/maps.*?</a>\s*<a class="btn-wpp-footer" href="https://wa.me/5535999999999.*?</a>'
# Let's find the exact block to replace safely
buttons_start = html.find('<a class="btn-wpp-footer" href="https://www.google.com/maps')
buttons_end = html.find('</a>\n  <nav class="footer-links"')
if buttons_start != -1 and buttons_end != -1:
    buttons_html = html[buttons_start:buttons_end+4]
    new_buttons_html = f'<div class="footer-buttons-wrapper">\n    {buttons_html.replace("margin-bottom: 1rem; margin-right: 1rem;", "").replace("margin-bottom: 1rem;", "")}\n  </div>'
    html = html[:buttons_start] + new_buttons_html + html[buttons_end+4:]

# FAQ transformation
faq_pattern = r'<div class="obj-grid max-w">.*?</div>\s*</section>'
new_faq_html = '''<div class="faq-container max-w">
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Produto com problema?</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Troca feita pessoalmente, na loja física no Centro. Sem burocracia, sem formulário online, sem longa espera.</p>
      </div>
    </div>
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Retirada grátis na loja</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Compre pelo WhatsApp, separe com a gente e venha retirar. Zero taxa de entrega. Você paga só pelo produto.</p>
      </div>
    </div>
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Aqui é loja de verdade</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Veja a fachada, veja as fotos dos clientes, veja o endereço no Google. Não é loja virtual sem rosto — é a King Shopping que Passos já conhece.</p>
      </div>
    </div>
  </div>
</section>'''
html = re.sub(faq_pattern, new_faq_html, html, flags=re.DOTALL)

# Glass panels transparency
html = html.replace('fill="#88ccff" opacity="0.1"', 'fill="#88ccff" opacity="0.4"')
html = html.replace('fill="#ffffff" opacity="0.1"', 'fill="none" stroke="#fff" stroke-width="1" opacity="0.5"')
html = html.replace('fill="#ffffff" opacity="0.05"', '') # Remove extra reflections

# Door mat text
mat_text = '<text x="400" y="475" font-family="Arial" font-size="14" font-weight="bold" fill="#FFD700" text-anchor="middle" style="filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.8));">CLIQUE PARA ENTRAR</text>'
html = html.replace('<!-- STORE ENTRANCE (center door) -->', f'<!-- STORE ENTRANCE (center door) -->\n  {mat_text}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Reduce logo sizes
css = css.replace('.logo-crown    { width: 36px; height: 36px; margin-bottom: -6px; }', '.logo-crown    { width: 24px; height: 24px; margin-bottom: -4px; }')
css = css.replace('.logo-king     { font-family: var(--font-display); font-size: 2.5rem; font-weight: 900; color: var(--red); }', '.logo-king     { font-family: var(--font-display); font-size: 1.6rem; font-weight: 900; color: var(--red); }')
css = css.replace('.logo-shopping { font-family: var(--font-display); font-size: 1rem; letter-spacing: 6px; font-weight: 600; display: block; margin-top: -6px; }', '.logo-shopping { font-family: var(--font-display); font-size: 0.7rem; letter-spacing: 4px; font-weight: 600; display: block; margin-top: -4px; }')

# Fix footer buttons CSS
css = css.replace('.btn-wpp-footer {\\n  display:    inline-flex;\\n  align-items: center;\\n  gap:        .6rem;\\n  background:  var(--green-wpp);\\n  color:       var(--white);\\n  font-weight: 700;\\n  font-size:   .95rem;\\n  padding:     .85rem 1.8rem;\\n  border-radius: 50px;\\n  text-decoration: none;\\n  transition: background .2s, transform .2s;\\n}', '''.btn-wpp-footer {
  display:    inline-flex;
  align-items: center;
  justify-content: center;
  gap:        .6rem;
  background:  var(--green-wpp);
  color:       var(--white);
  font-weight: 700;
  font-size:   .95rem;
  padding:     .85rem 1.8rem;
  border-radius: 50px;
  text-decoration: none;
  min-height: 48px;
  transition: background .2s, transform .2s;
}
.footer-buttons-wrapper {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}''')

# Remove old obj-grid CSS and add FAQ CSS
css = re.sub(r'\.obj-grid \{.*?\.obj-card p\s*\{.*?\}', '''/* FAQ Accordion */
.faq-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 760px;
  margin: 0 auto;
}
.faq-item {
  background: var(--dark2);
  border-radius: var(--radius);
  overflow: hidden;
  border: 1px solid #333;
}
.faq-question {
  width: 100%;
  background: transparent;
  border: none;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--white);
  cursor: pointer;
  text-align: left;
  transition: background 0.2s;
}
.faq-question:hover {
  background: rgba(255, 255, 255, 0.05);
}
.faq-question h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin: 0;
}
.faq-icon {
  font-size: 1.5rem;
  font-weight: 300;
  color: var(--gray);
  transition: transform 0.3s ease;
}
.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
  background: rgba(0, 0, 0, 0.2);
}
.faq-answer p {
  padding: 0 1.5rem 1.5rem;
  color: #bbb;
  font-size: 0.95rem;
  line-height: 1.6;
}
.faq-item.active .faq-icon {
  transform: rotate(45deg);
}''', css, flags=re.DOTALL)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 3. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

faq_js = '''
  // ==========================================================================
  // 5. FAQ ACCORDION
  // ==========================================================================
  const faqQuestions = document.querySelectorAll('.faq-question');
  
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const item = question.parentElement;
      const answer = question.nextElementSibling;
      const isActive = item.classList.contains('active');
      
      // Fecha todos os outros
      document.querySelectorAll('.faq-item').forEach(otherItem => {
        otherItem.classList.remove('active');
        otherItem.querySelector('.faq-answer').style.maxHeight = null;
      });
      
      // Toggle o clicado
      if (!isActive) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
'''

# Insert before closing brace
js = js.replace('});', faq_js + '\n});')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Success")
