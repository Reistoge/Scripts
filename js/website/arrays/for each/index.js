// array.forEach()= executes a provided callback function once for each array element


let students=['spongebob', 'patrick', 'squidward']
students.forEach(capitalize)
students.forEach(print)
//porque puedo colocar cualquier nombre de parametro ??
function capitalize(element, index,array){
    array[index]=element[0].toUpperCase()+element.substring(1)
}
console.log(students[0])

function print(x){
    console.log(x)
}