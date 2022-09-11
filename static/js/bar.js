let menuActive = false;

const menuTrigger = document.getElementById("menu-trigger");
const menuBackground = document.getElementById("link-menu");

menuTrigger?.addEventListener("mousedown", (event) => {
    event.stopPropagation();
    const display = menuActive ? "none": "flex";
    const menu = document.getElementById("link-menu");

    menu.style.display = display;
    menuActive = !menuActive;
});

menuBackground?.addEventListener("mousedown", (event) => {
    if (!event.target.classList.contains("menu")) return;
    event.target.style.display = "none";
    menuActive = false;
});