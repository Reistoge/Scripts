//arrays = think of it as a variable
//         that can store multiple values
//         ARRAYS ALWAYS START ON THE INDEX 0.
let fruits = ["apple", "orange", "banana"];

// fruits[2]='coconut' // rename the index number 2 of the array
fruits.push("lemon"); // add an element
fruits.pop(); // removes last element
fruits.unshift("watermelon"); // adds an element to the beginning
fruits.shift(); // removes an element from the beginning

let length = fruits.length; // counts the number of elements in the array.
let index = fruits.indexOf("watermelon"); //shows you the index of the element in this case is -1 because the element was deleted
console.log(index);
console.log(lenght);
console.log(fruits);
