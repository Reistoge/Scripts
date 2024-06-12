// map = object that holds key-value pairs of any data type 
let store = new Map([
    ["t-shirt", 20],
    ["jeans", 30],
    ["socks", 10],
    ["underwear", 50], 
    ["bread",]      
])
//puedes añadir un tercer elemento pero en el foreach solo reconocera dos parametros por lo tanto debes añadir en el key un json con los demas elementos.

// how do we call this key values ?
store.get("t-shirt")
store.set("hat", 40 )
store.set("cosa ", 30)
store.delete("hat")
console.log(store.has("underwear"))
console.log(store.size)
// a always is the value, and b always is the key
store.forEach((value,key) => console.log(` ${key} ${value}  `))

// en este caso for each con el map soporta dos parametros si quieres añadir un tercer elemento o más debes añadirlo dentro del map y el segundo debe ser un 
// objeto JSON cosa de que el foreach lo reconozca como segundo parametro pero despues este sea llamado como JSON y poder acceder a los objetos o elementos dentro de este.


//en un array cuando tu llames los parametros de este, el primer parametro se referira al elemento, index, array
let lista = new Array("a", 'b', "c", 'd')
lista.forEach((element, index, array) => console.log(element, index, array))

const car=new Map([
    ["ferrari", 3],
    ["lambo", 4]
])
//you have to put [] after () before declaring the values/keys
console.log(car)