const nav = document.querySelector(".nav");
const revealElements = document.querySelectorAll(".reveal");

if (nav) {
    const setNavState = () => {
        nav.classList.toggle("is-scrolled", window.scrollY > 24);
    };

    setNavState();
    window.addEventListener("scroll", setNavState, { passive: true });
}

if (revealElements.length) {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.16,
            rootMargin: "0px 0px -10% 0px",
        },
    );

    revealElements.forEach((element) => observer.observe(element));
}
