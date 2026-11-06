const welcomeSection = document.getElementById("welcome-section");
const mainContent = document.getElementById("main-content")
const btn = document.getElementById("btn");


btn.addEventListener("click", () => {
    welcomeSection.style.display = "none";
    mainContent.hidden = false;
})