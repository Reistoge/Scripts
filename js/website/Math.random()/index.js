let a;
let b
let c
document.getElementById("numberBtn").onclick = function (){
    a=Math.floor((Math.random() * 6) + 1)
    document.getElementById('number').innerHTML=a
    b=Math.floor((Math.random() * 6) + 1)
    document.getElementById('number2').innerHTML=b
    c=Math.floor((Math.random() * 6) + 1)
    document.getElementById('number3').innerHTML=c
    //the Math.random() returns a number between 0 and 1, so the number a is 0 < x < 1 if we multiply by 6 the number will be 0*6<x*6<6*1 and sum 1 will be 0*6+1=1 < x*6+1 < 1*6+1=7, 1 < x < 7 
    //we apply the Math.floor() to say that the number will always approximate to the nearest int less than x.(when the number is 6.9 the number will be 6 simulating the dice)
}    
 