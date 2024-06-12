//static= belongs to the class, not the objects.
//        properties: useful for caches, fixed-config
//        methods: useful for utility functions


class car{

    static numberOfCars=0 // this variable belong to the class not to the objects so to use it you have to call it with "car."

    // The constructor is a method that inicializa every time you create a "new" object and this method asing parameters just like a function
    // is the bridge that connects the new object with the class parameters, you create a new object of a class, that parameters goes to the
    // contructor and the constructor asign the parameters in the same order of a function.
    
    //if you want to create a property and assign to a parameter you have to use the "this", this acces to the property of the recent created object   
    constructor(models, xd){

        // in this case the properties created were model and bruh, models and xd are just parameters of the method .
        this.model=models
        this.bruh=xd
        car.numberOfCars+=1


    }

    // the startrace function belongs to the class not to the objects created
    static startRace(){
        console.log('3...2...1...GO!')
        console.log(this.numberOfCars)

    }
    
}
car1=new car('ferrari', 123)
console.log(car1.model, car1.bruh)

car1=new car('not ferrari', 'not defined')
console.log(car1.model, car1.bruh)
car.startRace()

//inside of a class using "this" method refers to the object or the class ? 