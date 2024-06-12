// array.reduce()= reduces an array to a single value

let prices=[5,10,15,20,25]
let total=prices.reduce(checkOut)

console.log(`the total is: $${total}`)
function checkOut(total, element){
    console.log(total)
    return total + element
}