import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove black bars
html = html.replace('<polygon points="180,268 220,268 120,440 80,440"  pointer-events="none"/>', '')
html = html.replace('<polygon points="780,268 820,268 720,440 680,440"  pointer-events="none"/>', '')

# 2. Remove subtitle
subtitle = '<text x="350" y="195" font-family="Arial, sans-serif" font-size="11"\n        fill="#aaaaaa" letter-spacing="4">UTILIDADES · BRINQUEDOS · ELETRÔNICOS · PAPELARIA</text>'
if subtitle in html:
    html = html.replace(subtitle, '')
else:
    # Just in case formatting is different
    import re
    html = re.sub(r'<text[^>]*>UTILIDADES · BRINQUEDOS · ELETRÔNICOS · PAPELARIA</text>', '', html)

# 3. Fix entrance mat text
old_text = '<text x="400" y="475" font-family="Arial" font-size="14" font-weight="bold" fill="#FFD700" text-anchor="middle" style="filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.8));">CLIQUE PARA ENTRAR</text>'
new_text = '<text x="455" y="464" font-family="Arial" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle" style="filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.6));">CLIQUE PARA ENTRAR</text>'
html = html.replace(old_text, new_text)

# Also remove the "KING SHOPPING" plaque if that's what was overlapping, wait, the user said "O texto CLIQUE PARA ENTRAR está desalinhado (a sobrepor a base da loja)". The plaque has "KING SHOPPING" text at y="464". If I replace the plaque text with "CLIQUE PARA ENTRAR" it would be perfect.
old_plaque_text = '<text x="388" y="464" font-family="\'Bebas Neue\',sans-serif" font-size="16" fill="#CC0000" letter-spacing="2">KING SHOPPING</text>'
html = html.replace(old_plaque_text, '')

# Let's fix the FAQ
faq_start = html.find('<div class="faq-container max-w">')
faq_end = html.find('</div>\n</section>\n\n\n\n<!-- ==================== SEÇÃO: SOCIAL PROOF ==================== -->')

if faq_start != -1 and faq_end != -1:
    new_faq = '''<div class="faq-container max-w">
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Dá para pedir pelo WhatsApp e só passar para retirar na loja?</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Sim! Sabemos que o seu dia a dia é corrido. Você pode chamar nossa equipe no WhatsApp, conferir o que temos, separar o seu pedido e vir retirar aqui no Centro de Passos. É rápido, prático e você não paga nenhuma taxa de entrega, só o valor do produto.</p>
      </div>
    </div>
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Comprei um brinquedo ou eletrônico e deu problema. É fácil trocar?</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Muito fácil e sem dor de cabeça. Se qualquer produto apresentar defeito, basta trazer na nossa loja física. Fazemos a troca na hora, pessoalmente, sem formulários online demorados ou enrolação. A nossa prioridade é você sair satisfeita.</p>
      </div>
    </div>
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Vocês vendem de tudo mesmo? Tem valor mínimo para comprar?</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Vendemos no varejo com preço super acessível e não tem valor mínimo! Você pode vir comprar só um caderno escolar ou renovar as utilidades da sua cozinha de uma vez só. Temos de papelaria a eletrônicos para você parar de bater perna na cidade e resolver tudo numa loja só.</p>
      </div>
    </div>
    <div class="faq-item reveal">
      <button class="faq-question">
        <h3>Onde a King Shopping fica exatamente?</h3>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>Nossa loja é física, de verdade, e está cheia de novidades te esperando! Ficamos bem no coração de Passos: na Rua Pres. Antônio Carlos, 110 - Centro. Pode vir nos fazer uma visita de segunda a sábado.</p>
      </div>
    </div>'''
    html = html[:faq_start] + new_faq + html[faq_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("done")
