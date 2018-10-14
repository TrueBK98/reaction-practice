while(true) {
    var username = prompt("Username must have at least 1 uppercase and 1 lowercase character.\nUsername: ");
    var password = prompt("Password must contain atleast 7 characters.\nPassword: ");
    var retype_password = prompt("Retype Password: ")
    var email = prompt("Email: ");

    if((username != username.toLowerCase()) && (username != username.toUpperCase())) {
        if((password.length >= 7) && (password === retype_password)) {
            if(email.includes("@gmail.com")) {
                console.log("Username:", username);
                console.log("Password:", password);
                console.log("Email:", email);
                break
            }
            else {
                console.log("Email invalid!")
            }
        }
        else {
            console.log("Password invalid!");
        }
    }
    else {
        console.log("Username invalid!")
    }
}


//------------------------------------------------------------------------------------------------------------------


var answer_choices = [1, 2, 3, 4];

answer = prompt("How many legs does a spider have?\n    1. None\n    2. 4 legs\n    3. 8 legs\n    4. 12 legs")
while(true) {
    if(answer in answer_choices) {
        console.log("Your answer:", answer);        
        if(answer === 2) {
            console.log("Correct");
            break
        }
        else {
            console.log("Wrong, the answer is 3: 4 legs");
            break
        }
    }
    else {
        answer = prompt("The answer must be 1, 2, 3 or 4, enter again: ");
    }
}


//------------------------------------------------------------------------------------------------------------------


while(true) {
    var a = prompt("ax^2 + bx +  c = 0\na = ");
    if(a > 0) {
        break
    }
    else {
        console.log("a phải lớn hơn 0");
    }
};
var b = prompt("ax^2 + bx +  c = 0\nb = ");
var c = prompt("ax^2 + bx +  c = 0\nc = ");

var delta = b**2 - 4 * a * c;
if(delta < 0) {
    console.log("Vô nghiệm");
}

else if(delta == 0) {
    console.log("Nghiệm kép");
    console.log("x =", b / 2 * a);
}

else if(delta > 0) {
    console.log("Hai nghiệm");
    console.log("x1 =", (-b + Math.sqrt(delta)) / 2 * a);
    console.log("x2 =", (-b - Math.sqrt(delta)) / 2 * a);
}
