//error: object with a description of something went wrong
// uses: can't open a file, lose conection, user type incorrect input, TypeError

try {
  let x = window.prompt("Enter a number ");
  x = Number(x);
  if (isNaN(x)) throw `that wasn't a number! >:c`;
  // -in this case this "if" will be an error now, the same as if i messed up with a syntax or something else-
  console.log(`${x} is a number :)`)
} catch (error) {
    console.log(`Bruh you fucked it on ${error}`)
}
finally{
    console.log(`this always executes`)
}
