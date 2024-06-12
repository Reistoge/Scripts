console.log("hola !!!");
const n1 = document.getElementById("numero1");
const n2 = document.getElementById("numero2");
const button = document.getElementById("button");
const ans = document.getElementById("answer");
const op = document.getElementById("operador");
const random1txt=document.getElementById('random1')
const random2txt=document.getElementById('random2')


button.onclick = function () {
  let n1Value = parseFloat(n1.value);
  let n2Value = parseFloat(n2.value);
  let opValue = op.value;
  if((opValue=='/'||opValue=='+'|| opValue =='*'||opValue =='-') && !isNaN(n1Value) && !isNaN(n2Value)){
    switch (opValue) {
        case "/":
          ans.innerText = n1Value / n2Value;
          break;
        case "+":
          ans.innerText = n1Value + n2Value;
          break;
        case "-":
          ans.innerText = n1Value - n2Value;
          break;
        case "*":
          ans.innerText = n1Value * n2Value;
          break;
    }  
  }
  else{
    ans.innerText='calculo imposible'
  }


    
}
let random1=0;
let random2=0;
let entre=0;
random1=Math.floor(Math.random()*10)
random2=Math.round((Math.random()*20)+10)
entre=Math.round((Math.random()*(random2-random1))+random1)
console.log(random1)
console.log(random2)
console.log(entre)
random1txt.innerText=random1
random2txt.innerText=random2
document.getElementById('boton2').onclick=function(){
    if (document.getElementById('intento').value==entre) {
        document.getElementById('respuesta').innerHTML='Adivinaste !!!'
        document.getElementById('comentario').innerHTML='Recarga la pagina para jugar de nuevo !!'
    }
    else{
        document.getElementById('respuesta').innerHTML='Sigue intentando'

        if(document.getElementById('intento').value < entre){
            document.getElementById('comentario').innerText='Intenta con uno más grande'
        }
        else if(document.getElementById('intento').value > entre){
            document.getElementById('comentario').innerText='Intenta con uno más pequeño'
        }


    }
}

  
  
  




