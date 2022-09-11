let menuActive = false;

const menuTrigger = document.getElementById("menu-trigger");

menuTrigger?.addEventListener("mousedown", () => {
    const display = menuActive ? "none": "flex";
    const menu = document.getElementById("link-menu");

    menu.style.display = display;
    menuActive = !menuActive;
});