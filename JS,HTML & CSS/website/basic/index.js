// a variable is a container for storing data
// A variable behaves as if it was the value that contains

/* 
    Two steps:
    1.Declaration (var, let, const)
    2.Assignment (= assignment operator)

*/

/* #1 types of variables and using it */

/*

//string
let firstName = "Bro"; 
//Number
let age = 21; 
//Boolean
let student = true; 

//using variables
// - here you can use + and commas -

console.log("Hello", firstName);
console.log("You are", age, "years old");
console.log("enrolled:", student);
console.log("hello", firstName, "you are " + age + " years old");

// - here you can use just +, if you use commas the variable will not be shown -  

document.getElementById("p1").innerHTML = "Hello " + firstName;
document.getElementById("p2").innerHTML = "you are " + age + " years old";
document.getElementById("p3").innerHTML = "Enrolled: " + student;

*/

/* #2: How to accept user input*/

// 2.1 EASY WAY with a window prompt (not practical, less visual)

//SYNTAX (DISCOMMENT ABOVE THE CHANGES)

/* let username= window.prompt('Whats your name ?');
console.log(username); */

/*
    2.2 DIFFICULT WAY HTML textbox

    1. create a variable who contains the value of the input:text element (username)
    2. call the button element and give a .onlick event and assign function
    3. inside the function asign the username variable to the .value of the input:text
    4. use the variable.

*/
//SYNTAX (DISCOMMENT ABOVE TO SEE CHANGES)

/* 
let username;
document.getElementById("myButton").onclick = function a() {
  username = document.getElementById("textBox").value;
  document.getElementById("label1").innerText = "Hi " + username + " ! ";
};
*/

/*  
    in inputs elements the text inside of them is his value property, 
    dont use innertext or innerhtml for capture his text inside.  
*/

// #3 type conversions = change the datatype of a value to another
//                       (strings, numbers, booleans)

/* 
let age = window.prompt("How old are you");
console.log(typeof age);
age = Number(age);
age += 1;
console.log('happy birthday! you are', age, "years old" )
*/ 

/* 
let x;
let y;
let z;
let a

a=Number('12')
x = Number("pizza");
y = String(3.14);
z = Boolean("pizza");

//the Number() String() and Boolean() change the type of the variable
//typeof allows us to show/get the type of the value 

console.log(a, typeof a)
console.log(x, typeof x);
console.log(y, typeof y);
console.log(z, typeof z); 
*/


 
