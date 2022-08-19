const hamburger = document.querySelector(".hamburger");
const logo = document.querySelector(".logo");
const navUl = document.querySelector(".nav-ul");
const navLink = document.querySelectorAll(".nav-link");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  logo.classList.toggle("active");
  navUl.classList.toggle("active");
  logo.classList.toggle("active");
});

navLink.forEach((link) =>
  link.addEventListener("click", () => {
    hamburger.classList.remove("active");
    logo.classList.remove("active");
    navUl.classList.remove("active");
    logo.classList.remove("active");
  })
);
