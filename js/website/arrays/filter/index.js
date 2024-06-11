// array.filter()=creates a new array with all elemets that pass the test provided by a function


let ages=[12,34,23,15,18,45,9,64]

let adults=ages.filter(CheckAge)

adults.forEach(print)

function CheckAge(element){
    return element >=18
}
function print(element){
    console.log(element)
}