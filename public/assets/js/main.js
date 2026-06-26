document.addEventListener('DOMContentLoaded', () => {
    
    // --- Loader ---
    const loader = document.getElementById('loader');
    setTimeout(() => {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
            // Trigger initial scroll animations after loader
            handleScrollAnimations();
        }, 500);
    }, 1500); // Show loader for 1.5s for premium feel

    // --- Sticky Header & Back to Top ---
    const header = document.getElementById('header');
    const backToTop = document.getElementById('back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.add('scrolled'); // keep background white on scroll
            if(window.scrollY < 10) {
               header.classList.remove('scrolled'); 
            }
        }
        
        if (window.scrollY > 500) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // --- Mobile Menu Toggle ---
    const mobileToggle = document.getElementById('mobile-toggle');
    const nav = document.querySelector('.nav');
    
    mobileToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
        const icon = mobileToggle.querySelector('i');
        if (nav.classList.contains('active')) {
            icon.classList.remove('ph-list');
            icon.classList.add('ph-x');
        } else {
            icon.classList.remove('ph-x');
            icon.classList.add('ph-list');
        }
    });

    // Close mobile menu on link click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('active');
            const icon = mobileToggle.querySelector('i');
            icon.classList.remove('ph-x');
            icon.classList.add('ph-list');
        });
    });

    // --- Scroll Reveal Animations ---
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .reveal-fade');
    
    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    function handleScrollAnimations() {
        revealElements.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            if (elementTop < window.innerHeight - 50) {
                el.classList.add('active');
            }
        });
    }

    // --- Animated Counters ---
    const counters = document.querySelectorAll('.counter');
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const endValue = parseInt(target.getAttribute('data-target'));
                let startValue = 0;
                const duration = 2000;
                let startTime = null;

                const step = (timestamp) => {
                    if (!startTime) startTime = timestamp;
                    const progress = Math.min((timestamp - startTime) / duration, 1);
                    // easeOutQuart
                    const easeProgress = 1 - Math.pow(1 - progress, 4);
                    const currentVal = Math.floor(easeProgress * endValue);
                    target.innerText = currentVal;
                    
                    if (progress < 1) {
                        window.requestAnimationFrame(step);
                    } else {
                        target.innerText = endValue;
                    }
                };
                window.requestAnimationFrame(step);
                observer.unobserve(target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    // --- Countdown Timer (Mega Camp) ---
    // Set target date to July 5, 2026
    const targetDate = new Date('July 5, 2026 10:00:00').getTime();
    
    function updateCountdown() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
            document.getElementById('countdown').innerHTML = "<h3>The Camp has started!</h3>";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById('cd-days').innerText = days.toString().padStart(2, '0');
        document.getElementById('cd-hours').innerText = hours.toString().padStart(2, '0');
        document.getElementById('cd-mins').innerText = minutes.toString().padStart(2, '0');
        document.getElementById('cd-secs').innerText = seconds.toString().padStart(2, '0');
    }

    setInterval(updateCountdown, 1000);
    updateCountdown(); // Initial call

    // --- Testimonials Slider ---
    const testiSlider = document.getElementById('testi-slider');
    if (testiSlider) {
        const dots = document.querySelectorAll('.slider-dots .dot');
        let currentSlide = 0;
        const totalSlides = dots.length;

        function goToSlide(index) {
            testiSlider.style.transform = `translateX(-${index * 100}%)`;
            dots.forEach(dot => dot.classList.remove('active'));
            dots[index].classList.add('active');
            currentSlide = index;
        }

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => goToSlide(index));
        });

        // Auto slide
        setInterval(() => {
            let nextSlide = (currentSlide + 1) % totalSlides;
            goToSlide(nextSlide);
        }, 5000);
    }

    // --- Gallery Filter ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active to clicked
            btn.classList.add('active');
            
            const filterValue = btn.getAttribute('data-filter');
            
            galleryItems.forEach(item => {
                if (filterValue === 'all' || item.classList.contains(filterValue)) {
                    item.classList.remove('hide');
                } else {
                    item.classList.add('hide');
                }
            });
        });
    });

    // --- FAQ Accordion ---
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Close all
            faqItems.forEach(faq => {
                faq.classList.remove('active');
                faq.querySelector('.faq-answer').style.maxHeight = null;
            });
            
            // Open clicked if it wasn't active
            if (!isActive) {
                item.classList.add('active');
                const answer = item.querySelector('.faq-answer');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });

    // Open first FAQ by default
    if(faqItems.length > 0) {
        faqItems[0].classList.add('active');
        const firstAnswer = faqItems[0].querySelector('.faq-answer');
        firstAnswer.style.maxHeight = firstAnswer.scrollHeight + "px";
    }
});

// --- Modal Global Functions ---
const modal = document.getElementById('appointmentModal');

function openAppointmentModal() {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function closeAppointmentModal() {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto'; // Re-enable scrolling
}

// Close modal on click outside
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeAppointmentModal();
    }
});

// --- Form Submissions to Backend ---

const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('contactName').value,
            phone: document.getElementById('contactPhone').value,
            email: document.getElementById('contactEmail').value,
            message: document.getElementById('contactMessage').value
        };
        
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            if (result.success) {
                alert(result.message);
                contactForm.reset();
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            alert('There was an error sending your message. Please try again later.');
        }
    });
}

const appointmentForm = document.getElementById('appointmentForm');
if (appointmentForm) {
    appointmentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            patientName: document.getElementById('appPatientName').value,
            phone: document.getElementById('appPhone').value,
            department: document.getElementById('appDepartment').value,
            date: document.getElementById('appDate').value
        };
        
        try {
            const response = await fetch('/api/appointment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const result = await response.json();
            if (result.success) {
                alert(result.message);
                appointmentForm.reset();
                closeAppointmentModal();
            }
        } catch (error) {
            console.error('Error booking appointment:', error);
            alert('There was an error booking your appointment. Please try again later.');
        }
    });
}
