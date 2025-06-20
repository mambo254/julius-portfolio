document.addEventListener("DOMContentLoaded", () => {
  AOS.init({ duration: 800 });

  const filterButtons = document.querySelectorAll(".filter-btn");
  const cards = document.querySelectorAll(".project-card");

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.getAttribute("data-filter");

      cards.forEach((card) => {
        const tags = card.getAttribute("data-tags");
        const match = filter === "all" || tags.includes(filter);
        card.style.display = match ? "block" : "none";
        if (match) {
          card.classList.add("aos-animate");
        }
      });
    });
  });
});
