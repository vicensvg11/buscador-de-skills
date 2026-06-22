// ============================================
// REVOPARTNER — JAVASCRIPT INTERACTIVO
// ============================================

document.addEventListener('DOMContentLoaded', () => {

  // ---- NAV SCROLL ----
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });

  // ---- HAMBURGER MENU ----
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('open'));
  });

  // ---- COUNTER ANIMATION ----
  const counters = document.querySelectorAll('.stat-number');

  const animateCounter = (el) => {
    const target = parseInt(el.dataset.target);
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const update = () => {
      current += step;
      if (current < target) {
        el.textContent = Math.floor(current);
        requestAnimationFrame(update);
      } else {
        el.textContent = target;
      }
    };
    update();
  };

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => counterObserver.observe(c));

  // ---- FADE UP ANIMATIONS ----
  const fadeEls = document.querySelectorAll(
    '.service-card, .result-card, .team-card, .testimonio-card, .step, .value-item, .nosotros-text, .nosotros-team, .contacto-info, .contacto-form'
  );

  fadeEls.forEach(el => el.classList.add('fade-up'));

  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.index ? entry.target.dataset.index * 80 : 0;
        setTimeout(() => entry.target.classList.add('visible'), delay);
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  fadeEls.forEach(el => fadeObserver.observe(el));

  // ---- TESTIMONIOS SLIDER ----
  const track = document.getElementById('testimonios-track');
  const cards = track.querySelectorAll('.testimonio-card');
  const dotsContainer = document.getElementById('slider-dots');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');

  const isMobile = () => window.innerWidth <= 768;
  let currentSlide = 0;
  let totalSlides = isMobile() ? cards.length : Math.ceil(cards.length / 2);

  // Create dots
  const createDots = () => {
    dotsContainer.innerHTML = '';
    totalSlides = isMobile() ? cards.length : Math.ceil(cards.length / 2);
    for (let i = 0; i < totalSlides; i++) {
      const dot = document.createElement('button');
      dot.className = 'dot-item' + (i === currentSlide ? ' active' : '');
      dot.setAttribute('aria-label', `Slide ${i + 1}`);
      dot.addEventListener('click', () => goToSlide(i));
      dotsContainer.appendChild(dot);
    }
  };

  const updateDots = () => {
    dotsContainer.querySelectorAll('.dot-item').forEach((d, i) => {
      d.classList.toggle('active', i === currentSlide);
    });
  };

  const goToSlide = (index) => {
    currentSlide = Math.max(0, Math.min(index, totalSlides - 1));
    const cardWidth = cards[0].offsetWidth + 24;
    const offset = isMobile() ? currentSlide * cardWidth : currentSlide * (cardWidth * 2);
    track.style.transform = `translateX(-${offset}px)`;
    updateDots();
  };

  prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));

  createDots();

  // Auto-advance
  let autoSlide = setInterval(() => goToSlide((currentSlide + 1) % totalSlides), 5000);

  track.parentElement.addEventListener('mouseenter', () => clearInterval(autoSlide));
  track.parentElement.addEventListener('mouseleave', () => {
    autoSlide = setInterval(() => goToSlide((currentSlide + 1) % totalSlides), 5000);
  });

  window.addEventListener('resize', () => {
    currentSlide = 0;
    createDots();
    goToSlide(0);
  });

  // Touch swipe
  let touchStartX = 0;
  track.addEventListener('touchstart', e => touchStartX = e.touches[0].clientX);
  track.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      diff > 0 ? goToSlide(currentSlide + 1) : goToSlide(currentSlide - 1);
    }
  });

  // ---- BAR CHART HOVER ----
  document.querySelectorAll('.bar').forEach(bar => {
    bar.addEventListener('mouseenter', () => {
      if (!bar.classList.contains('active')) {
        bar.style.background = 'rgba(99,102,241,0.6)';
      }
    });
    bar.addEventListener('mouseleave', () => {
      if (!bar.classList.contains('active')) {
        bar.style.background = 'rgba(99,102,241,0.3)';
      }
    });
  });

  // ---- CONTACT FORM ----
  const form = document.getElementById('contacto-form');
  const formSuccess = document.getElementById('form-success');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    btn.textContent = 'Enviando...';
    btn.disabled = true;

    setTimeout(() => {
      formSuccess.classList.remove('hidden');
      form.reset();
      btn.textContent = 'Enviar mensaje';
      btn.disabled = false;
      formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 1200);
  });

  // ---- ACTIVE NAV LINK ----
  const sections = document.querySelectorAll('section[id]');
  const navA = document.querySelectorAll('.nav-links a[href^="#"]');

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navA.forEach(a => {
          a.style.color = a.getAttribute('href') === '#' + entry.target.id ? 'white' : '';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));

});
