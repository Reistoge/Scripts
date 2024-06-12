const txtn1 = document.getElementById("n1");
const txtn2 = document.getElementById("n2");
const Operador = document.getElementById("operador");
const Boton = document.getElementById("boton");
const Resultado = document.getElementById("resultado");
Boton.addEventListener("click", calculadora);

function calculadora() {
  const num1 = parseFloat(txtn1.value);
  const num2 = parseFloat(txtn2.value);
  const operador = Operador.value;
  if (
    (operador == "/" ||
      operador == "+" ||
      operador == "-" ||
      operador == "*") &&
    !isNaN(num1) &&
    !isNaN(num2)
  ) {
    /*  */
    /* switch(operador){
            case '+':
                resultado.innerText=num1+num2;
            case '-':
                resultado.innerText=num1-num2;
            case '/':
                resultado.innerText=num1/num2;
            case '*':
                resultado.innerText=num1*num2
        } */

    switch (operador) {
      case "+":
        resultado = num1 + num2;
        break;

      case "-":
        resultado = num1 - num2;
        break;

      case "/":
        resultado = num1 / num2;
        break;

      case "*":
        resultado = num1 * num2;
        break;
    }

    Resultado.innerText = "=" + resultado;
  } else {
    resultado.innerText = "Calculo imposible";
  }
}
