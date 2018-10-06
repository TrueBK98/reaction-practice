function randomColor() {
    var r = Math.floor(Math.random() * 256)
    var g = Math.floor(Math.random() * 256)
    var b = Math.floor(Math.random() * 256)

    return `rgb(${r}, ${g}, ${b})`
}

var numSquares = 6;

var colors = [

]

for (var i=0; i < 6; i++) {
    color = randomColor();
    colors.push(color);
}

var pickedColor = colors[
    Math.floor(Math.random() * 5)
]

var squares = document.querySelectorAll(".square");
console.log(squares);


for (var i = 0; i < squares.length; i++) {
    squares[i].style.backgroundColor = colors[i];
}

squares.forEach( (square) => {
    square.addEventListener("click", (event) => {
        var clickedColor = event.target.style.backgroundColor
        if (clickedColor === pickedColor) {
            console.log("dung");
        }
        else {
            console.log("sai");
        }
    })
} )