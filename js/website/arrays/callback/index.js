// callback = a function passed as an argument
//            to another function.

//          Ensures that a function is not going to run before a task is completed.
//          Help us develop asynchronous code.
//          (when one function has to wait for another function)
//          that helps us avoid error and potential problems
//          Ex. Wair for a file to load



//??????
sum(2, 3, displayDOM);
// the parameters are: 2 numbers and a function.
// basically is use a function as a parameter 
function sum(x, y, callBack) {
  let result = x + y;
  callBack(result);
}
function displayConsole(output) {
  console.log(output);
}

function displayDOM(output) {
  document.getElementById("myLabel").innerHTML = output;
}
