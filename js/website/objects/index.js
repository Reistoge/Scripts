//objects = a group of properties and methods
//          properties =what an object has 
//          methods = what an object can do 
//          use . to acces properties/methods
const car ={
    model:'Mustang',
    color:'Red',
    year:2023,
    
    drive: function(){
        console.log('you drive the car')

    },
    brake: function(){
        console.log('you step on the brakes')
    }

//the difference between and object and a map is is that map is iterable and objects not ?? 

}
car.drive()


