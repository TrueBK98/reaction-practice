var circle = document.querySelector('#circle');
var counter = document.querySelector('#counter')
var container = document.querySelector("#container")
var start = document.querySelector("#start")
var setTimer;
var milliseconds = 2000;
var numCircle = 0;

counter.style.fontSize = "xx-large";
counter.style.fontWeight = "bold";
counter.style.fontFamily = "Raleway, sans-serif";

function judge() {
    var score = document.createElement("h1")
    if (numCircle <= 5) {
        var scoreText = document.createTextNode("Slow")
        score.style.color = "brown";
    }
    else if (numCircle <= 12) {
        var scoreText = document.createTextNode("Quite Slow")
        score.style.color = "gray";
    }
    else if (numCircle <= 18) {
        var scoreText = document.createTextNode("Average")
        score.style.color = "blue";
    }
    else if (numCircle <= 21) {
        var scoreText = document.createTextNode("Quite Fast")
        score.style.color = "orange";
    }
    else if (numCircle <= 27) {
        var scoreText = document.createTextNode("Fast")
        score.style.color = "red";
    }
    else if (numCircle > 27) {
        var scoreText = document.createTextNode("Inhuman")
        score.style.color = "gold";
    }
    score.appendChild(scoreText);
    score.style.fontFamily = "Impact, Merriweather, sans-serif";
    score.style.fontSize = "500%"
    container.appendChild(score)
    finalCounter(score);
}

function mouseEntered() {
    cancelTimer();
    numCircle++;
    circleCounter();
    milliseconds -= (milliseconds / 10); 
    applyMargin();
}

function addReplay(eC, sc) {
    var restart = document.createElement("button");
    var text = document.createTextNode("Replay");
    restart.appendChild(text);
    container.appendChild(restart);
    restart.addEventListener("click", () => {
        milliseconds = 2000;
        numCircle = 0;
        play();
        container.removeChild(restart);
        container.removeChild(eC);
        container.removeChild(sc);
    })
}

function finalCounter(score) {
    var endCounter = document.createElement("p");
    endCounter.innerText = "Circle = " + numCircle;
    endCounter.style.width = "15%";
    endCounter.style.height = "50px";
    endCounter.style.backgroundColor = "red";
    endCounter.style.display = "flex";
    endCounter.style.justifyContent = "center";
    endCounter.style.alignItems = "center";
    container.appendChild(endCounter);
    addReplay(endCounter, score);
}

function containerChange() {
    document.getElementById("container").style.justifyContent = "center"
    document.getElementById("container").style.alignItems = "center"    
    document.getElementById("container").style.height = "600px"
    document.getElementById("container").style.flexDirection = "column"
}

function containerInitial() {
    document.getElementById("container").style.justifyContent = "initial"
    document.getElementById("container").style.alignItems = "initial"    
    document.getElementById("container").style.height = "initial"
    document.getElementById("container").style.flexDirection = "initial"
}

function circleCounter() {
    document.getElementById("counter").innerText = "Circle = " + numCircle
}

function end() {
    document.getElementById("circle").style.display = "none";
    document.getElementById("counter").style.display = "none";
    containerChange();
    judge();
    document.getElementById("circle").removeEventListener("mouseenter", mouseEntered)
}

function timer() {
    setTimer = setTimeout(function() {
        end();
    }, milliseconds);
}

function cancelTimer() {
    clearTimeout(setTimer);
}

function randomMargin() {
    marginTop = Math.random() * 450
    marginLeft = Math.random() * 1100
    return `${marginTop}px ${marginLeft}px -10px`
};

function applyMargin() {
    margin2Apply = randomMargin();
    document.getElementById("circle").style.margin = margin2Apply;
    timer();
}

circle = circle.getContext("2d");
circle.beginPath();
circle.arc(150, 75, 75, 0, 2 * Math.PI);
circle.fillStyle = "green"
circle.fill();

function play() {
    containerInitial();
    document.getElementById("circle").style.display = "initial";
    document.getElementById("counter").style.display = "initial";
    circleCounter();
    applyMargin()
    document.getElementById("circle").addEventListener("mouseenter", mouseEntered);
}

document.getElementById("start").addEventListener("click", () => {
    container.removeChild(start)
    play();
});

document.getElementById("circle").style.display = "none";
document.getElementById("counter").style.display = "none";

