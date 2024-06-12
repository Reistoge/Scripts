// function expression = function without a name (anonymous function)
//                       avoid polluting the global scope with names
//                       write it, then forget about it

const greeting = function(){
    console.log('jelou')
}
greeting()
let count=0;

document.getElementById('increaseBtn').onclick=function(){
    count+=1
    document.getElementById('myLabel').innerHTML=count  

}
document.getElementById('decreaseBtn').onclick=function(){
    count-=1
    document.getElementById('myLabel').innerHTML=count  
}

