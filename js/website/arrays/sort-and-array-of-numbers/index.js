let grades=['f', 'd','a', 'g','t','z','k']
grades =grades.sort()
grades.forEach(print)
function print(element){
    console.log(element)
}
console.log(grades)

//hacer una funcion que elimine y añada elementos al array
// sort lo que hace es ordenar los elementos de menor a mayor, esto lo hace con una funcion x - y donde x es un elemento del array e y es el elemento sucesor a x, teniendo 
//esto en cuenta sort lo que hace es que si la funcion sort retorna un numero negativo, el parametro x sera menor por lo tanto ira primero e y ira segundo, 
// si la funcion x-y es positiva se dira que x es mayor que y por lo tanto x ira despues de y por lo tanto hay un swap
// despues de esto el parametro "y" se comparara con su sucesor y asi hasta que los elementos esten ordenados, 
let grades2= [2,4,1,5,12,10]
 
grades2 =grades2.sort(ascendingSort)
grades2.forEach(print)

grades2=grades2.sort(descendingsort)
grades2.forEach(print)

grades=grades2.map(sum)
grades2.forEach(print)

function sum(x){
    // x+=1 dont work, why ??
    return x+=1
}
function ascendingSort(x,y){
   
    return x-y;
    // if x-y:
    // 1. < 0 --> x comes first
    // 2.  0 --> same number
    // 3. > 0 --> y comes first
}
function descendingsort(x,y){
    return y-x;
     // if x-y:
    // 1. < 0 --> x comes first
    // 2.  0 --> same number
    // 3. > 0 --> y comes first
}
function print(element){
    console.log(element)
}




/* let array=[12,2,45,2,5,675,100,239]
function threeDigits(x){
    return x>99
}
array2=array.filter(threeDigits)
array2.forEach( x => console.log(x))
array2.sort(x)
x=function ascendingSort(x,y){
    return x-y
}
array2.forEach( x => console.log(x)) */