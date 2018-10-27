var circle = document.querySelector('#circle');
var counter = document.querySelector('#counter');
var container = document.querySelector("#container");
var start = document.querySelector("#start");
var header = document.querySelector("#header-text");
var tutorials = document.querySelectorAll(".tutorials");
var read_more = document.querySelector("#read_more");
var tutorial_box = document.querySelector("#tutorial-box")
var setTimer;
var setCountdown;
var milliseconds = 2000;
var numCircle = 0;
var tutorialDisplay = false;
var scores = [];

function callCountdown() {
    var timeLeft = milliseconds;
    setCountdown = setInterval(function(){
        timeLeft -= 10;
        document.getElementById("countdown").innerText = "Time: " + (timeLeft / 1000).toFixed(2) + "s";
    }, 10);
};

function clearCountdown() {
    clearInterval(setCountdown);
}

function newScore() {
    scores.push(numCircle);
    localStorage.removeItem("scoresList");
    localStorage.setItem("scoresList", JSON.stringify(scores));
    scores.sort(function(a, b) {return b - a});
    for (var i = 0; i < scores.length; i++) {
        if (scores[i] == scores[i + 1]) {
            scores[i + 1] = 0;
        }
    };
    scores.sort(function(a, b) {return b - a});
};

function leaderboard(endCounter, score, restart) {
    var show = true
    var leaderboard = document.createElement("div");
    container.appendChild(leaderboard);
    leaderboard.style.width = "15%";
    leaderboard.style.height = "40%";
    leaderboard.style.backgroundImage = "url('https://cdn.hipwallpaper.com/i/75/34/qHZtJ2.jpg')"
    leaderboard.style.backgroundSize = "cover";
    leaderboard.style.border = "2px solid black"
    leaderboard.style.display = "none";
    leaderboard.style.justifyContent = "space-between"
    leaderboard.style.alignItems = "center"
    leaderboard.style.flexDirection = "column"
    if (scores.length == 1) {
        for (var i = 1; i < 6; i++) {
            var line = document.createElement("div");
            var lineScores = document.createTextNode(i + ".");
            line.appendChild(lineScores);
            leaderboard.appendChild(line)
            line.style.fontSize = "170%"
        }
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    else if (scores.length == 2) {
        var line = document.createElement("div");
        var lineScores = document.createTextNode("1. " + scores[0])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        for (var i = 2; i < 6; i++) {
            var line = document.createElement("div");
            var lineScores = document.createTextNode(i + ".");
            line.appendChild(lineScores);
            leaderboard.appendChild(line)
            line.style.fontSize = "170%"

        }
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    else if (scores.length == 3) {
        var line = document.createElement("div");
        var lineScores = document.createTextNode("1. " + scores[0])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("2. " + scores[1])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        for (var i = 3; i < 6; i++) {
            var line = document.createElement("div");
            var lineScores = document.createTextNode(i + ".");
            line.appendChild(lineScores);
            leaderboard.appendChild(line)
            line.style.fontSize = "170%"

        }
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    else if (scores.length == 4) {
        var line = document.createElement("div");
        var lineScores = document.createTextNode("1. " + scores[0])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("2. " + scores[1])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("3. " + scores[2])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        for (var i = 4; i < 6; i++) {
            var line = document.createElement("div");
            var lineScores = document.createTextNode(i + ".");
            line.appendChild(lineScores);
            leaderboard.appendChild(line)
            line.style.fontSize = "170%"

        }
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    else if (scores.length == 5) {
        var line = document.createElement("div");
        var lineScores = document.createTextNode("1. " + scores[0])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("2. " + scores[1])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = createTextNode("3. " + scores[2])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("4. " + scores[3])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        for (var i = 5; i < 6; i++) {
            var line = document.createElement("div");
            var lineScores = document.createTextNode(i + ".");
            line.appendChild(lineScores);
            leaderboard.appendChild(line)
            line.style.fontSize = "170%"

        }
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    else if (scores.length >= 6) {
        var line = document.createElement("div");
        var lineScores = document.createTextNode("1. " + scores[0])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("2. " + scores[1])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("3. " + scores[2])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("4. " + scores[3])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("5. " + scores[4])
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
        var line = document.createElement("div");
        var lineScores = document.createTextNode("Your: " + numCircle);
        line.appendChild(lineScores);
        leaderboard.appendChild(line)
        line.style.fontSize = "170%"
    }
    var showLeaderboard = document.createElement("button");
    var text = document.createTextNode("Scores");
    showLeaderboard.appendChild(text);
    container.appendChild(showLeaderboard);
    showLeaderboard.addEventListener("click", () => {
        if (show == true) {
            endCounter.style.display = "none";
            score.style.display = "none";
            restart.style.display = "none";
            leaderboard.style.display = "initial";
            leaderboard.style.display = "flex";
            show = false
        }

        else {
            endCounter.style.display = "initial";
            score.style.display = "initial";
            restart.style.display = "initial";
            endCounter.style.display = "flex";
            leaderboard.style.display = "none";
            show = true
        }
    })
    return showLeaderboard;
};

function judge() {
    var score = document.createElement("h1")
    if (numCircle <= 20) {
        var scoreText = document.createTextNode("Slow")
        score.style.color = "brown";
    }
    else if (numCircle <= 30) {
        var scoreText = document.createTextNode("Quite Slow")
        score.style.color = "white";
    }
    else if (numCircle <= 40) {
        var scoreText = document.createTextNode("Average")
        score.style.color = "blue";
    }
    else if (numCircle <= 50) {
        var scoreText = document.createTextNode("Quite Fast")
        score.style.color = "orange";
    }
    else if (numCircle <= 70) {
        var scoreText = document.createTextNode("Fast")
        score.style.color = "red";
    }
    else if (numCircle > 70) {
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
    clearCountdown();
    numCircle++;
    circleCounter();
    milliseconds -= (milliseconds / 20); 
    applyMargin();
}

function addReplay(eC, sc) {
    var restart = document.createElement("button");
    var text = document.createTextNode("Replay");
    restart.appendChild(text);
    container.appendChild(restart);
    restart.style.marginBottom = "10px"
    var lB = leaderboard(eC, sc, restart);
    restart.addEventListener("click", () => {
        milliseconds = 2000;
        numCircle = 0;
        play();
        container.removeChild(restart);
        container.removeChild(eC);
        container.removeChild(sc);
        container.removeChild(lB);
    })
}

function finalCounter(score) {
    var endCounter = document.createElement("p");
    endCounter.innerText = "Circle(s) = " + numCircle;
    endCounter.style.width = "18%";
    endCounter.style.height = "50px";
    endCounter.style.backgroundImage  = "url('https://orig00.deviantart.net/76e6/f/2018/011/1/c/output_dmfg1x_by_crazyraingirl-dbzpev2.gif')";
    endCounter.style.display = "flex";
    endCounter.style.justifyContent = "center";
    endCounter.style.alignItems = "center";
    endCounter.style.fontSize = "x-large";
    endCounter.style.fontWeight = "bold";
    endCounter.style.fontFamily = "Raleway, sans-serif";
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
    document.getElementById("counter").innerText = "Circle(s) = " + numCircle
}

function end() {
    newScore();
    document.getElementById("countdown").style.display = "none";
    document.getElementById("circle").style.display = "none";
    document.getElementById("counter").style.display = "none";
    containerChange();
    judge();
    document.getElementById("circle").removeEventListener("mouseenter", mouseEntered)
}

function timer() {
    setTimer = setTimeout(function() {
        clearInterval(setCountdown);
        end();
    }, milliseconds);
}

function cancelTimer() {
    clearTimeout(setTimer);
    clearInterval(setCountdown);
}

function randomMargin() {
    marginTop = Math.random() * 32
    marginLeft = Math.random() * 70
    return `${marginTop}% ${marginLeft}% -10px`
};

function applyMargin() {
    margin2Apply = randomMargin();
    document.getElementById("circle").style.margin = margin2Apply;
    timer();
    callCountdown();
}

function play() {
    containerInitial();
    document.getElementById("circle").style.display = "initial";
    document.getElementById("counter").style.display = "initial";
    document.getElementById("counter").style.display = "flex";
    document.getElementById("countdown").style.display = "flex";
    circleCounter();
    applyMargin()
    document.getElementById("circle").addEventListener("mouseenter", mouseEntered);
}

if (localStorage.getItem("scoresList") === null) {
    localStorage.setItem("scoresList", 0)
}
else {
    scores = JSON.parse(localStorage.getItem("scoresList"));
}

document.getElementById("start").addEventListener("click", () => {
    container.removeChild(start);
    container.removeChild(tutorial_box)
    container.removeChild(read_more)
    container.removeChild(header)
    play();
});

document.getElementById("read_more").addEventListener("click", () => {
    if (tutorialDisplay == false) {
        tutorials.forEach( (tutorial) => {
            tutorial.style.display = "initial"
        })
        document.getElementById("tutorial-box").style.display = "flex"
        tutorialDisplay = true
        read_more.innerHTML = ">Click to hide<"
    }
    else {
        tutorials.forEach( (tutorial) => {
            tutorial.style.display = "none"
        })
        tutorialDisplay = false
        document.getElementById("tutorial-box").style.display = "none"
        read_more.innerHTML = ">Click to show Instruction<"
    }
})

counter.style.fontSize = "x-large";
counter.style.fontWeight = "bold";
counter.style.fontFamily = "Raleway, sans-serif";

countdown.style.fontSize = "x-large";
countdown.style.fontWeight = "bold";
countdown.style.fontFamily = "Raleway, sans-serif";

circle = circle.getContext("2d");
circle.beginPath();
circle.arc(150, 75, 75, 0, 2 * Math.PI);
circle.fillStyle = "green"
circle.fill();

document.getElementById("countdown").style.display = "none";
document.getElementById("circle").style.display = "none";
document.getElementById("counter").style.display = "none";
document.getElementById("tutorial-box").style.display = "none"

container.style.flexDirection = "column";
container.style.padding = "10px 10px 10px 10px";
