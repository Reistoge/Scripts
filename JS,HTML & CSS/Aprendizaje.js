console.log("oli")
var numero1 =5
var numero2=2
var respuesta = (numero1!=numero2) && (numero1+numero2)  /* si se cumple el primero seguira al segundo en este caso 5!=2 por lo tanto los numeros se suman. */
var respuesta2  = (numero1==numero2) && (numero1+numero2) /* en este caso es false el primero por lo tanto el valor de la var seria false y no sumaria los demas. */
console.log(respuesta)
console.log(respuesta2)

/* NOTA: EL VALOR DE LA VARIABLE VA POR ORDEN SI COLOCAS PRIMERO LA OPERACIÓN Y AL FINAL EL RELACIONAL EL VALOR QUE TOMARA SERÁ EL RELACIONAL, AUNQUE SI TU COLOCAS 
UN RELACIONAL Y DESPUES UNA OPERACION SI EL RELACIONAL DA "FALSE" EL VALOR DE LA VARIABLE PASA A SER FALSE Y OLVIDA LA OPERACION QUE TIENE POR DELANTE, SI DA TRUE PASA A LA OPERACION SIENDO ESTE SU VALOR FINAL. */
/* EL FALSE CORTA LA LA SIGUIENTE ACCIÓN, predomina */
/* esta ve cual es false */

console.log("||")
var respuesta3 = (numero1!=numero2) || (numero1+numero2) /* en este caso el valor que toma la variable es true ya que la primera sera true*/
var respuesta4 = (numero1==numero2) || (numero1+numero2) /* este valor sera la operacion ya este variable es la operacion ya que al ser false continua con la siguiente opción. */
console.log(respuesta3)
console.log(respuesta4)
/* esta ve cual es true, true predomina */
ing1="leche"
ing2="chocolate"
console.log(cafetera(ing1, ing2))


function cafetera(ing1, ing2){
    let batido= ing1+' '+ing2
    console.log(batido)
    return

}
let op1='2'
let op2='4'
let operando="/"
function calculadora(op1, op2, operando){
    if(operando=="/"){
        resultado=op1/op2
        
    }if(operando=="+"){
        resultado= op1+op2
        
    }if(operando=="*"){
        resultado=parseFloat(op1)*parseFloat(op2)
        
    }
    if(operando=="-"){
        resultado=parseFloat(op1)-parseFloat(op2)
        
    }
    if(operando=="%"){
        resultado=parseFloat(op1)%parseFloat(op2)
        
    }
    return resultado
}
console.log(calculadora(op1, op2, operando))
/* js puede dividir numeros que sean strings, no es necesario pasarlo a numeros al menos para hacer operaciones. */