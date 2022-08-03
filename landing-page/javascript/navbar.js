        // Responsive Nav bar
        const hamburger = document.getElementById("hamburger");
        const navMenu = document.getElementById("nav-menu");

        hamburger.addEventListener("click", mobileMenu);

        function mobileMenu() {
            hamburger.classList.toggle("active");
            navMenu.classList.toggle("active"); 
        }

        const navLink = document.querySelectorAll(".lnk");

        navLink.forEach(n => n.addEventListener("click", closeMenu));

        function closeMenu() {
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
        }

        // Responsive Dropdown links
        function dropFunction1() {
        document.getElementById("dropdown-content1").classList.toggle("show");
        }

        function dropFunction2() {
        document.getElementById("dropdown-content2").classList.toggle("show");
        }

        // Close the dropdown if the user clicks outside of it
        window.onclick = function(event) {
            if (!event.target.matches('.dropdown-btn')) {
                var dropdowns = document.getElementsByClassName("dropdown-content");
                var i;
                for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                    if (openDropdown.classList.contains('show')) {
                        openDropdown.classList.remove('show');
                    }
                }
            }
        }
