//return = returns a value back to the place where you invoked the function
let area
let width
let height
width =window.prompt('enter width')
height=window.prompt('enter height')
area=getarea(width, height)

console.log('the area is:', area)

function getarea(width, height){
  let result=width*height
  return result;

}