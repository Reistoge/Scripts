// inheritance = a child class can inherit all the methods and properties from another class 

class animal{
    alive=true
    eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }

}
class rabbit extends animal{
    name='rabbit'
    cute=true
    /* 
       eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }
    */
    
    run(){
        console.log(`the ${this.name} is running`)
    }

}
class fish extends animal{
    name='fish'
    /* alive =true */
    cute=false
    /* 
       eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }
    */
   
    swim(){
        console.log(`the ${this.name} is swimming`)
    }

}
class hawk extends animal{
    name='hawk'
    /* alive =true */
    cute=false
    /* 
       eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }
    */
  
    fly(){
        console.log(`the ${this.name} is flying`)
    }
}
// this 3 classes have some comun properties and methods, to reduce code and time the inheritance let us make a classes of classes
// in this case 3 classes have the same sleep and eat function and the same alive property
 
pablo=new rabbit
DonGualo= new fish
red=new hawk

console.log(rabbit)
console.log(fish)
console.log(hawk)

console.log(pablo)
console.log(DonGualo)
console.log(red)

pablo.run()
DonGualo.swim()
red.fly()

// for some reason if you name assign the class to a variable and you console.log  that variable this will log all the class syntax
//class hawk extends animal{
//    name=hawk
    /* alive =true */
//    cute=false
    /* 
       eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }
    */
  
//    fly(){
//        console.log(`the ${this.name} is flying`)
//    }
//}