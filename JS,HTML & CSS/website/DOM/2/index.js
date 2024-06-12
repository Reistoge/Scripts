 
 
// when you selects more than one element, the variable becomes an array
// if you want to call one element you can call as the same as an array index element
// but if you use the .style or others methods on the array it wont work
// you have to select each object of the array element this is using a for each or for in
// also you can call all the element with [] but its more convenient using the other methods
// arrays store the elements as info, it cant select all the element

let title=document.getElementById('myTitle')
let fruits=document.getElementsByName('fruits')
let desserts=document.getElementsByClassName('desserts')
let vegetables=document.getElementsByTagName("li")
let element= document.querySelector('#myLabel')
let elements=document.querySelectorAll('[for]')
//query selector select the element if you specify his type and name
// is the same way as you select the elements in css, id=#name, clas=.name, attributes=[]

title.style.backgroundColor='skyblue'
// for of selects the variables, for in selects the value varaibles
for(element of elements){
    element.style.backgroundColor='red'
}

fruits.forEach((fruit)=>{
        if(fruit.checked){
            console.log(fruit.value)
            title.innerHTML+=': '+fruit.value
        }
})
for(vegetable of vegetables){
    vegetable.style.backgroundColor='#f16f'
} 
vegetables[1].style.backgroundColor='lightgreen'
desserts[1].style.backgroundColor='#04f0ff'

element.style.backgroundColor='red'
element.style.fontSize='40px'
    
