// variable scope =where a variabl is accesible

//let = variable are limited to block scope{} 

//var = variable are limited to a fnction(){}

// global variable = is declared outside any function
// (if global, var will change browser's window properties, so we use let to global. )


let name ='bro'

dosomething();
function dosomething(){
    for(var i=1; i <3;i++){
        //console.log(i) here you wont have problems
    }
}
// console.log(i) 
// this will give a uncaught reference error because 'i' can escape of a function.
// var can escape from a function and let can escape from a function and a {}
// let cant esacpe from a if, else, for, etc, if is created inside of them.