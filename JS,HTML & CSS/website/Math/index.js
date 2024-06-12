//js Math.() 
  
let x=3.5
let a=3
let b=4
let c=5
let maximun
let minimun
let pi;
//redondeo normal
//  x=Math.round(x) 

//redondeo pero siempre al int cercano menor al numero
//  x=Math.floor(x)

//redondeo pero siempre al int cercano mayor al numero
//  x=Math.ceil(x)

//elevar al cuadrado
//  x=Math.pow(x,2)

//raiz cuadrada
//  x=Math.sqrt(x)

//valor absoluto
//  x=Math.abs(x)

//asignar pi
//  pi=Math.PI

//asignar o obtener el maximo/minimo entre variables.
//  maximun=Math.max(a,b,c)
//  minimun=Math.min(a,b,c)

console.log(pi)
console.log(x)
console.log(maximun)
console.log(minimun)

//get the hypotenuse of a triangle.
// window prompt option.
/*
let a;
let b;
let c;
a= (window.prompt('enter side a'))
b= (window.prompt('enter side b'))
a=Number(a)
b=Number(b)
c=Math.sqrt(Math.pow(a, 2)+Math.pow(b, 2))
console.log(a + ' ' +typeof a)
window.alert(c) 
*/
// html element option.
document.getElementById("myButton").onclick=function(){
    let a=document.getElementById('aTextBox').value
    a=Number(a)
    let b=document.getElementById('bTextBox').value
    b=Number(b)

//option 1 create a variable 
     document.getElementById('cTextBox').innerHTML='Hypotenuse is ' + Math.sqrt(Math.pow(a, 2)+Math.pow(b, 2))

//option 2
//    let c= (Math.sqrt(Math.pow(a, 2)+Math.pow(b, 2)))
//    document.getElementById('cTextBox').innerHTML = 'side c equals to '+c

} 
