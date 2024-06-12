// function = define a code once, use it many times.
//            to perform some code, call the function name.

startProgram();
function startProgram() {
  let username = "bro";
  let age = 21;
  happybirthday(username, age)
}

happybirthday(a,b);
function happybirthday() {
  console.log(`happy birthday ${a}`);
  console.log(`you are ${b} years old`);
}
