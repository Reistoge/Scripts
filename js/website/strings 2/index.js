let userName='Ferran Rojas'
let phoneNumber='21.642.668-1'
console.log(userName.length)
console.log(userName.charAt(0))

// lastIndexOf() shows us the last index of that letter in the string, if the character 
// is not repeated in the string this will be the same as charAt()
console.log(userName.lastIndexOf('a'))

//trim allows you delete all empty spaces before or after any characters.
userName=userName.trim()

userName=userName.toUpperCase()
userName=userName.toLowerCase()
//replace all of that characters in that string to another one.
phoneNumber=phoneNumber.replaceAll('.', '/')
console.log(phoneNumber)
console.log(userName)