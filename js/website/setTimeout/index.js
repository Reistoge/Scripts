// setTimeout()= invokes a function after a number of miliseconds
//               asynchronous function (doesnt pause execution)


 
//           function   (ms)          parameters
let x=setTimeout(firstMessage,5000,'Parameter x', 'Parameter y' )
let y=setTimeout(secondMessage,10000,'Parameter a', 'Parameter b' )
let z=setTimeout(thirdMessage,20000,'Parameter c', 'Parameter d' )
 
function firstMessage(x,y) {
  alert(`Five seconds delay function after program initialize. ${x}, ${y} `);
}
function secondMessage(a,b) {
  alert(`Ten seconds delay function after program initialize. ${a}, ${b}`);
}
function thirdMessage(c,d) {
  alert(`twenty seconds delay function after program initialize. ${c}, ${d}`);
}
//this will stop the timer.
document.getElementById('mybutton').onclick= function(){
    clearTimeout(x)
    clearTimeout(y)
    clearTimeout(z)

    alert('You stop and clear the three function timer')
}