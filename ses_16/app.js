var quizz = document.querySelector("#default-code");
var message = document.querySelector("#message");
var reset = document.querySelector("#reset");

var restart = () => {
    colors = generateColor(6);
    pickedColor = pickColor();
    quizz.innerHTML = pickedColor;
    message.innerHTML = "Đoán Xem";
    message.style.color = "white";
    for (var i = 0; i < squares.length; i++) {
        squares[i].style.backgroundColor = colors[i];
    }
}

function randomColor() {
    var r = Math.floor(Math.random() * 256)
    var g = Math.floor(Math.random() * 256)
    var b = Math.floor(Math.random() * 256)

    return `rgb(${r}, ${g}, ${b})`
}

var generateColor = (numColors) => {
    var listColor = [];
    for(var i=0; i < numColors; i++) {
        var ranColor = randomColor();
        listColor.push(ranColor);
    }
    return listColor;
}

var numSquares = 6;

var colors = generateColor(numSquares);

var pickColor = () => {
    var random_num = Math.floor(Math.random() * colors.length )
    return colors[random_num]
}


var pickedColor = pickColor();

quizz.innerHTML = pickedColor;

var squares = document.querySelectorAll(".square");
console.log(squares);


for (var i = 0; i < squares.length; i++) {
    squares[i].style.backgroundColor = colors[i];
}

squares.forEach( (square) => {
    square.addEventListener("click", (event) => {
        var clickedColor = event.target.style.backgroundColor
        if (clickedColor === pickedColor) {
            message.innerHTML = "Dung";
            message.style.color = "green";
        }
        else {
            message.innerHTML = "Sai";
            message.style.color = "red";
        }
        for (var i=0; i < numSquares; i++) {
            squares[i].style.backgroundColor = pickedColor;
        }
    })
} )

reset.addEventListener("click", () => {
    restart();
})