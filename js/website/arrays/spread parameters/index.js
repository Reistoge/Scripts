// spread parameters = represents an indefinite number of parameters
//                      (packs an argumen into an array)
let a=1
let b=2
let c=3
let d=4
let e=5
let f=6
let g=7

// what happens when i want one function for multiple parameters or a lot of parameters?
// one solution could be create a function for each cuantity of parameters 
function sum(a,b){
    return a+b

}
function sum2(a,b,c){
    return a+b+c;
}
function sum3(a,b,c,d){
    return a+b+c;

}
function sum4(a,b,c,d){
    return a+b+c+d
}

// ????????
// the first two parameters will be x or y but the next will be part of the spread operator, be sure to put the spread after the parameters declared
function sum(x, y, ...numbers){
    let total =0
    for(let number of numbers){
        total+=number
    }
    return total
}
//?????????  