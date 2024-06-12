// spread operator = allows an iterable such as an array or 
// ...               string to be expandedin places where zero   
//                   or more arguments are expected
//                   (unpack the elements)


let numbers = [1,2,3,4,5,6,7,8,9]
let maximum=Math.max(numbers)
console.log(maximum)
//in this case maximum is NaN because we are calling the array object not his elements
// so to call all the elements we have to unpack the array, spread operator is the way to do it.
let numbers2 = [1,2,3,4,5,6,7,8,9]
let maximum2=Math.max(...numbers2)
console.log(maximum2)

let class1=['Spongbob', 'Patrick', 'Sandy']
let class2=['Squidward', 'Mr.Krabs', 'Plankton']
//in this case we are gona to push the array object to class1 not his elements, to push only the element we have to use
// the spread operator, 
// class1.push(class2)
class1.push(...class2)
console.log(class1)
console.log(...class1)
