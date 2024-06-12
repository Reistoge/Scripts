// setInterval()= invokes a function repedtly after a number miliseconds
//                  asynchronous function, doesnt pause execution program
//                FUNCTION, MILISECONDS, PARAMETERS 
let x=0
let interval=setInterval(countUp, 1000)
function countUp(){
    x+=1
    console.log(x)
    if(x>=10){
        clearInterval(interval)
        //clearInterval reed variables.
    }
}
// can you erase variables while executing code ?
//create and erase a object