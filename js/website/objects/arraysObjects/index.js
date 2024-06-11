// Is a good practice becasue yo have organized your objects into an array.



class Car{
    constructor(model, year, color){
        this._model=model
        this._year=year
        this._color=color
        
    }
    drive(){
        console.log(`You drive the ${this._model}`)
    }

}
car1=new Car('Lambo', 2020, 'Black')
car2=new Car('Ferrari', 2023, 'Red')
car3=new Car('Corvette', 2018, 'Gold')


Cars=[car1,car2,car3]

secondway()
//two ways to do it. 
function firstway(){

    for(const car of Cars){
        console.log(car._model, car._color, car._year)
}
}
function secondway(){
    Cars.forEach(car => {console.log(car._model, car._year, car._model)})
}

    
