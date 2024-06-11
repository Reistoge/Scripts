// arrow function= compact alternative to a traditional function expression
//          =>
// parameters, arrow, function
// with this technique you dont have to create function or variables to execute code. 
const greeting = (username) => console.log(`hello ${username}`);
greeting("Ferran");

//when you have more than 1 parameter or when we have to use the return you have to use the curly braces
// you can delete the curly braces and the return ad stills works but idk what happens, its do the same so asume that returns the value without curly braces


const percent = (x, y) => { return (x / y) * 100}
console.log(percent(2, 3) + "%");


let grades = [100, 50, 90, 60, 80, 70];
// parameters, arrow, function
grades=grades.sort((x,y) => x-y)
grades.forEach((x)=> console.log(x) )

grades=grades.sort((x,y)=> {return y-x})
grades.forEach((x)=> console.log(x) )

//arrow functions by default returns values.