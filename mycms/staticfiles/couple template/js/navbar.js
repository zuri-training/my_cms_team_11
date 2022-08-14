const hamburger = document.querySelector(".hamburger");
const navUl = document.querySelector(".nav-ul");
const navLink = document.querySelectorAll(".nav-link");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navUl.classList.toggle("active");
});

navLink.forEach((link) =>
  link.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navUl.classList.remove("active");
  })
);
