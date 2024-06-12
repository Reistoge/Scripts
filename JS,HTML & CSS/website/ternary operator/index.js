// ternary operator=Shortcut for an 'if/else statement' takes 3 operands
//                  1. a condition with ?
//                  2. expression if True
//                  3. expression if False

// condition ? exprIfTrue : exprIfFalse

// with ternary operator

let hungry=checkHungry(120)
console.log(hungry)
function checkHungry(time){
    return time > 240 ? true : false
}


//without ternary operator
let adult =checkAge(21)
console.log(adult)
function checkAge(age) {
    if(age>=18){
        return true
    }
    else{
        return false
    }
}
