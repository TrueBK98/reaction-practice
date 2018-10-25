var text1 = document.querySelectorAll(".text")
var button = document.getElementById("bt")
button.addEventListener('click', () => {
    text1.forEach((t) => {
        t.style.display = "none";
    });
})