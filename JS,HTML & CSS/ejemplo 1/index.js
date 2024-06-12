/*  MANERAS DE HACERLO */
 
/* 
const txtn1=document.getElementById("n1")
const txtn2=document.getElementById("n2")
const boton=document.getElementById("boton")
const boton2=document.getElementById("inputBoton")
const resp=document.getElementById("respuesta")
boton.addEventListener("click", calculator)
*/

//1st option
/* function calculator(){
   let op1=parseFloat(txtn1.value)
   let op2=parseFloat(txtn2.value)
   let resultado=op1+op2
   resp.innerText=resultado
   
} */

//2nd option
/* function calculator(){
    let op1=parseFloat(txtn1.value)
    let op2=parseFloat(txtn2.value)
    resp.innerText=op1+op2
    
} */

//3rd option
/* 
function calculator(){
   resp.innerText=parseFloat(txtn1.value)+ parseFloat(txtn2.value)
    
} 
*/


//4th option
/* 

This way does not need the lines that call the variables of the other 3.

  document.getElementById("boton").onclick = function() {

  let txtn1 = document.getElementById("n1").value;
  let txtn2 = document.getElementById("n2").value;
  let resp = document.getElementById("respuesta");
  resp.innerText=parseFloat(txtn1)+parseFloat(txtn2)
};

 */