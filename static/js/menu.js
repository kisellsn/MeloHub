const menu_icon = document.getElementById('menu_icon');
const nav = document.querySelector('nav');
menu_icon.addEventListener('click', function() {
    nav.classList.toggle('active');
});