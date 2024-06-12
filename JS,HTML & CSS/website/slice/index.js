let fullName
let firstName
let lastName

fullName='Ferran Rojas'


//numbers in commas are the index that the string would be sliced
// in this case the string is gonna be sliced between [0]=F and [6]=n. are the letter next to the 6 index are deleted.
firstName=fullName.slice(0,6)

//in this case the string is sliced in the seventh word all the letters behind the 7letter are deleted
lastName=fullName.slice(7)
console.log(firstName)
console.log(lastName)


let fullName2
let firstName2
let lastName2
fullName2='Pedro Fuenzalida'
firstName2=fullName2.slice(fullName2.indexOf(' ')+1)
console.log(firstName2)
lastName2=fullName2.slice(0,fullName2.indexOf(' '))
console.log(lastName2)


