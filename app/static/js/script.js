const welcomeSection = document.getElementById("main-con");
const mainContent = document.getElementById("main-content")
const btn = document.getElementById("btn");
const bars = document.querySelectorAll('.trans-cont .bar')
const trans = document.getElementById("trans")



btn.addEventListener("click", () => {
    bars.forEach((bar, index) => {
        setTimeout(() => {
            bar.classList.add('active');
        }, index* 100)
    });

    const totalduration = 500 + (bars.length - 1)* 100;

    setTimeout(() => {
        welcomeSection.style.display = "none";
        trans.style.display = "none"
        mainContent.hidden = false;
        document.body.style.backgroundColor = "#fff"
    }, totalduration);
})