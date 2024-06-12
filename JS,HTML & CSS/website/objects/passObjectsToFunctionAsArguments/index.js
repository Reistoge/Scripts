class Car{
    constructor(model, year, color){
        this._model=model
        this._year=year
        this._color=color
    }
}
const car1= new Car('ferrari', 2020, 'red')
const car2= new Car('corvette', 2023, 'Black')
const car3= new Car('lambo', 2019, 'White')
displayInfo(car1)

displayInfo(car2)

changeColor(car2, 'Green' )

function displayInfo(object){
    console.log(object._model)
    console.log(object._color)
    console.log(object._year)
}
function changeColor(object, Newcolor){
    object.color = Newcolor
    console.log(`You set the new color to "${object.color}"`)

}

 