import os

css_additions = """
/* ==========================================================================
   PREMIUM REDESIGN ADDITIONS
   ========================================================================== */

/* Typography & Colors */
.text-gradient {
    background: linear-gradient(90deg, #4ade80, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.text-primary { color: var(--primary); }
.text-primary-dark { color: var(--primary-dark); }
.text-accent { color: var(--accent); }
.text-white { color: #fff; }
.text-light { color: rgba(255,255,255,0.8); }

.bg-primary-dark { background-color: var(--primary-dark); }
.bg-gradient-light {
    background: linear-gradient(135deg, #f7fafc 0%, #e6f4f0 100%);
}
.gradient-bg {
    background: linear-gradient(135deg, var(--primary) 0%, #054a34 100%);
}
.pattern-bg {
    background-color: #f8fafc;
    background-image: radial-gradient(var(--primary-light) 2px, transparent 2px);
    background-size: 30px 30px;
}

/* Shadows & Glass */
.shadow-premium { box-shadow: 0 20px 40px rgba(0,0,0,0.08); }
.shadow-glow { box-shadow: 0 0 20px rgba(10, 143, 102, 0.4); }
.premium-glass {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.6);
}

/* Buttons & Inputs */
.btn-xl {
    padding: 18px 40px;
    font-size: 1.1rem;
}
.btn-white {
    background: #fff;
    color: var(--accent);
}
.btn-white:hover {
    background: #f8f9fa;
    transform: translateY(-2px);
}
.btn-outline-primary {
    border: 2px solid var(--primary);
    color: var(--primary);
}
.btn-outline-primary:hover {
    background: var(--primary);
    color: #fff;
}
.premium-input {
    background: rgba(255,255,255,0.9);
    border: 2px solid var(--border-color);
    transition: all 0.3s ease;
}
.premium-input:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 4px rgba(10, 143, 102, 0.1);
}

/* Animations */
.hover-lift { transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease; }
.hover-lift:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-premium);
}
.hover-glow { transition: all 0.3s ease; }
.hover-glow:hover {
    box-shadow: 0 0 25px rgba(10, 143, 102, 0.2);
    transform: translateY(-5px);
}
.hover-zoom { overflow: hidden; }
.hover-zoom img { transition: transform 0.6s ease; }
.hover-zoom:hover img { transform: scale(1.1); }

.floating-anim { animation: float-premium 5s ease-in-out infinite; }
@keyframes float-premium {
    0% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}

.tracking-in { animation: tracking-in 1s cubic-bezier(0.215, 0.610, 0.355, 1.000) both; }
@keyframes tracking-in {
    0% { letter-spacing: -0.5em; opacity: 0; }
    40% { opacity: 0.6; }
    100% { opacity: 1; }
}

.fade-in-up { animation: fadeInUp 1s ease 0.5s both; }
@keyframes fadeInUp {
    0% { transform: translateY(20px); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

/* Wave Dividers */
.custom-shape-divider-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}
.custom-shape-divider-bottom svg {
    position: relative;
    display: block;
    width: calc(100% + 1.3px);
    height: 60px;
}
.custom-shape-divider-bottom .shape-fill { fill: var(--primary-dark); }

.custom-shape-divider-top {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}
.custom-shape-divider-top svg {
    position: relative;
    display: block;
    width: calc(100% + 1.3px);
    height: 60px;
}
.custom-shape-divider-top .shape-fill-white { fill: #fff; }

/* Hero Floating Elements */
.floating-elements {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
}
.float-icon-1 { position: absolute; top: 20%; left: 10%; font-size: 40px; color: rgba(255,255,255,0.2); animation: float 6s infinite; }
.float-icon-2 { position: absolute; top: 70%; left: 80%; font-size: 50px; color: rgba(74,222,128,0.2); animation: float 8s infinite reverse; }
.float-icon-3 { position: absolute; top: 40%; left: 85%; font-size: 30px; color: rgba(96,165,250,0.2); animation: float 7s infinite 2s; }

.hero-glass-panel {
    display: flex;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: var(--radius-lg);
    padding: 25px;
    margin-top: 50px;
    gap: 30px;
    align-items: center;
    max-width: 800px;
}
.glass-stat {
    display: flex;
    align-items: center;
    gap: 15px;
    color: #fff;
}
.glass-stat i { font-size: 40px; }
.glass-stat h4 { font-size: 24px; margin: 0; display: inline-block; color: #fff; }
.glass-divider { width: 1px; height: 50px; background: rgba(255,255,255,0.2); }

/* Trust Bar */
.trust-bar {
    padding: 15px 0;
    overflow: hidden;
    white-space: nowrap;
    display: flex;
    color: #fff;
    font-weight: 600;
    letter-spacing: 1px;
}
.trust-track {
    display: flex;
    animation: scroll-trust 30s linear infinite;
}
.trust-track span {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 0 40px;
    font-size: 1.1rem;
}
.trust-track span i { color: #4ade80; font-size: 24px; }
@keyframes scroll-trust {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* Emergency Banner */
.emergency-banner {
    background: linear-gradient(135deg, #d62828 0%, #8b0000 100%);
    padding: 60px 0;
    color: #fff;
    position: relative;
    overflow: hidden;
}
.emergency-banner::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: url('data:image/svg+xml;utf8,<svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><circle cx="2" cy="2" r="2" fill="rgba(255,255,255,0.1)"/></svg>');
    opacity: 0.5;
}
.emergency-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 1;
}
.em-text {
    display: flex;
    align-items: center;
    gap: 20px;
}
.em-icon i { font-size: 60px; color: #fff; }
.emergency-content h2 { color: #fff; margin-bottom: 5px; font-size: 2.2rem; }
.emergency-content p { font-size: 1.1rem; opacity: 0.9; }

/* Doctor Cards Premium */
.doctor-card-premium {
    flex: 0 0 320px;
    background: #fff;
    border-radius: var(--radius-xl);
    overflow: hidden;
    border: 1px solid var(--border-color);
}
.doc-social {
    position: absolute;
    top: 20px; right: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    opacity: 0;
    transform: translateX(20px);
    transition: all 0.4s ease;
}
.doctor-card-premium:hover .doc-social {
    opacity: 1; transform: translateX(0);
}
.doc-social a {
    width: 40px; height: 40px;
    background: #fff;
    color: var(--primary);
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 20px;
    box-shadow: var(--shadow-md);
}
.doc-badge {
    background: var(--primary-light);
    color: var(--primary-dark);
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
}
.doc-exp { color: var(--text-muted); font-weight: 600; font-size: 0.95rem; }

/* Timeline Process */
.process-timeline {
    position: relative;
    border-top: 5px solid var(--primary);
}
.timeline-container {
    position: relative;
    padding: 40px 0;
}
.timeline-line {
    position: absolute;
    top: 50px;
    left: 0;
    width: 100%;
    height: 4px;
    background: rgba(255,255,255,0.2);
    z-index: 0;
}
.timeline-steps {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
    position: relative;
    z-index: 1;
}
.t-step { text-align: center; }
.t-icon {
    width: 80px; height: 80px;
    background: var(--primary);
    border: 4px solid var(--primary-dark);
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    margin: 0 auto 20px;
    font-size: 32px;
    color: #fff;
    box-shadow: 0 0 20px rgba(74,222,128,0.3);
}
.t-step h4 { color: #fff; font-size: 1.2rem; }
.t-step p { color: rgba(255,255,255,0.7); font-size: 0.95rem; }

/* Facilities Premium */
.fac-card-premium {
    background: #fff;
    border-radius: var(--radius-lg);
    padding: 30px;
    text-align: center;
    border: 1px solid var(--border-color);
}
.fac-icon {
    width: 70px; height: 70px;
    background: var(--bg-light);
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    margin: 0 auto 20px;
    font-size: 32px;
    color: var(--primary);
    transition: all 0.3s ease;
}
.fac-card-premium:hover .fac-icon {
    background: var(--primary);
    color: #fff;
    transform: rotateY(180deg);
}

/* Health Tips Carousel */
.tips-carousel {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
}
.tip-card {
    padding: 30px;
    text-align: left;
    border-top: 4px solid var(--primary);
}
.tip-card i { font-size: 40px; margin-bottom: 20px; }
.tip-card h4 { margin-bottom: 10px; font-size: 1.2rem; }
.tip-card p { font-size: 0.95rem; color: var(--text-muted); }

/* Testimonials Premium */
.testi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}
.testi-card-premium {
    background: #fff;
    padding: 40px;
    border-radius: var(--radius-xl);
    position: relative;
}
.quote-icon {
    position: absolute;
    top: -20px; right: 30px;
    width: 50px; height: 50px;
    background: var(--primary);
    color: #fff;
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 24px;
}
.stars-sm { color: var(--google-star); margin-bottom: 15px; font-size: 14px; }
.review-text { font-size: 1.1rem; font-style: italic; color: var(--text-main); margin-bottom: 30px; }
.patient-profile { display: flex; align-items: center; gap: 15px; }
.patient-profile img { width: 50px; height: 50px; border-radius: 50%; }
.patient-profile h4 { margin: 0; font-size: 1.1rem; }
.patient-profile span { color: var(--text-muted); font-size: 0.9rem; }

/* Responsive Updates for New Elements */
@media (max-width: 992px) {
    .timeline-line { display: none; }
    .timeline-steps { grid-template-columns: 1fr; gap: 30px; }
    .t-step { display: flex; align-items: center; text-align: left; gap: 20px; }
    .t-icon { margin: 0; }
    .hero-glass-panel { flex-direction: column; align-items: flex-start; gap: 15px; padding: 20px; }
    .glass-divider { width: 100%; height: 1px; }
    .emergency-content { flex-direction: column; text-align: center; gap: 30px; }
    .em-text { flex-direction: column; }
    .tips-carousel { grid-template-columns: 1fr 1fr; }
    .testi-grid { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
    .tips-carousel { grid-template-columns: 1fr; }
}
"""

with open(r'c:\Users\krish\OneDrive\Desktop\life line hospital\public\assets\css\style.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

print("CSS appended successfully.")
