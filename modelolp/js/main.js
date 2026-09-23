"use strict";

/**
 * MAIN.JS — King Shopping
 * Lógica principal da Landing Page
 * Versão auditada: null-checks, strict mode, listeners limpos.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Detecta preferência de movimento reduzido uma única vez
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ==========================================================================
  // 1. SCROLL REVEAL — IntersectionObserver
  // Elementos com .reveal aparecem gradualmente ao entrar na viewport.
  // O observer é desconectado (unobserve) imediatamente após ativar,
  // evitando vazamento de memória e disparos repetidos.
  // ==========================================================================
  const revealEls = document.querySelectorAll('.reveal');

  if (!prefersReducedMotion && revealEls.length > 0) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => entry.target.classList.add('visible'), i * 80);
          revealObserver.unobserve(entry.target); // Para de observar após revelar
        }
      });
    }, { threshold: 0.12 });

    revealEls.forEach(el => revealObserver.observe(el));
  } else {
    // Se preferir sem animação, mostra tudo imediatamente
    revealEls.forEach(el => el.classList.add('visible'));
  }

  // ==========================================================================
  // 2. SMOOTH SCROLLING
  // Rola suavemente até seções ao clicar em links âncora internos.
  // ==========================================================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function handleAnchorClick(e) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: prefersReducedMotion ? 'auto' : 'smooth'
        });
      }
    });
  });

  // ==========================================================================
  // 3. STORE DOORS ANIMATION — IntersectionObserver
  // Abre as portas de vidro quando a seção #storefront entra na viewport.
  // Fecha ao sair. O observer persiste intencionalmente (efeito bidirecional).
  // ==========================================================================
  const storefrontSec = document.querySelector('#storefront');
  const storeDoors    = document.querySelector('.store-doors');

  let doorObserver = null;

  if (storefrontSec && storeDoors && !prefersReducedMotion) {
    doorObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        storeDoors.classList.toggle('doors-open', entry.isIntersecting);
      });
    }, { threshold: 0.4 });

    doorObserver.observe(storefrontSec);
  }

  // ==========================================================================
  // 4. GAMIFIED STORE ENTRANCE
  // Clique no wrapper do SVG → zoom-in + reveal do catálogo interno.
  // Botão "Sair da Loja" reverte a animação.
  // ==========================================================================
  const svgWrapper  = document.getElementById('storefront-svg-wrapper');
  const insideStore = document.getElementById('inside-store');
  const btnExit     = document.getElementById('btn-exit-store');

  if (svgWrapper && insideStore && storefrontSec) {

    svgWrapper.addEventListener('click', () => {
      // Abre as portas imediatamente
      storeDoors?.classList.add('doors-open');

      // Dispara o zoom-in via CSS (classe no body)
      document.body.classList.add('enter-store');

      // Após a transição CSS (~900ms), troca o conteúdo exibido
      setTimeout(() => {
        storefrontSec.style.display = 'none';

        // Desconecta o doorObserver para evitar disparos com a seção oculta
        doorObserver?.disconnect();

        insideStore.style.display = 'block';

        // Micro-delay para garantir que o browser aplique o display antes do fade-in
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            insideStore.style.opacity = '1';
          });
        });

        insideStore.scrollIntoView({ behavior: 'smooth' });
      }, 900);
    });

    // Botão "Sair da Loja" — reverte animação
    btnExit?.addEventListener('click', () => {
      insideStore.style.opacity = '0';

      setTimeout(() => {
        insideStore.style.display = 'none';
        storefrontSec.style.display = 'block';

        // Reativa o doorObserver após restaurar a seção
        requestAnimationFrame(() => {
          document.body.classList.remove('enter-store');
          storeDoors?.classList.remove('doors-open');

          if (storefrontSec && storeDoors && doorObserver && !prefersReducedMotion) {
            doorObserver.observe(storefrontSec);
          }

          storefrontSec.scrollIntoView({ behavior: 'smooth' });
        });
      }, 500);
    });
  }

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

});

