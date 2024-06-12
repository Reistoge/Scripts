document.getElementById("submitButton").onclick = function () {
  let temp;
  if (document.getElementById("celsiusLabel").checked) {
    temp = document.getElementById("textBox").value;
    temp = Number(temp);
    temp = toCelsius(temp);
    document.getElementById("tempLabel").innerHTML = temp + '°C';
  } 
  else if (document.getElementById("farenheitLabel").checked) {
    temp = document.getElementById("textBox").value;
    temp = Number(temp);
    temp = toFarenheit(temp);
    document.getElementById("tempLabel").innerHTML = temp+' °F';
  } 
  else {
    document.getElementById("tempLabel").innerHTML =
      "You have to specify a unit";
  }
};

function toCelsius(temp) {
  return (temp - 32) * (5 / 9);
}
function toFarenheit(temp) {
  return (temp * 9) / 5 + 32;
}
//REMEMBER INPUT FIELDS HAVE A VALUE AND ALL THE LABELS AND P HAVE A INNERHTML 