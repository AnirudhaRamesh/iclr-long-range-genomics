// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.navbar-nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Close the mobile navbar if open
                const navbarToggler = document.querySelector('.navbar-toggler');
                const navbarCollapse = document.querySelector('.navbar-collapse');
                
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
                
                // Smooth scroll to the target section
                window.scrollTo({
                    top: targetSection.offsetTop - 60,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add active class to navbar links on scroll
    window.addEventListener('scroll', function() {
        const fromTop = window.scrollY + 100;
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const id = section.getAttribute('id');
            const link = document.querySelector(`.navbar-nav a[href="#${id}"]`);
            
            if (
                section.offsetTop <= fromTop &&
                section.offsetTop + section.offsetHeight > fromTop
            ) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    });
});
