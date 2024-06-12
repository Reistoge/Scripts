// 2D arrays = an array of arrays
let fruits=['apple', 'banana', 'watermelon']
let vegetables=['tomatoes','carrots', 'onions']
let meats=['chicken', 'eggs', 'fish']

let groceryList=[fruits, vegetables,meats]
console.log(groceryList[1][2])
groceryList[1][1]='potatoes'
//?????????
for(let a of groceryList){
    for(let b of a){
        console.log(b)
    }
}
//??????