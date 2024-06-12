//super= refers to parent class.
//       commoly invoked to constructor of a parent class.
class animal{
 
    constructor(name, age){
        this._name=name
        this._age=age
    }
    eat(){
        console.log(`the ${this.name} is eating`)
    }
    sleep(){
        console.log(`the ${this.name} is sleeping`)

    }

}
class rabbit extends animal{

 
    constructor(rabbitName, rabbitAge, runSpeed){
        super(rabbitName,rabbitAge)
        this._runSpeed=runSpeed
    }
    run(){
        console.log(`the ${this.name} is running`)
    }

}
class fish extends animal{
 
    constructor(fishName, fishAge,swimSpeed){
        super(fishName,fishAge)
        this._swimSpeed=swimSpeed
    }
   
    swim(){
        console.log(`the ${this.name} is swimming`)
    }

}
class hawk extends animal{
 
 
    constructor(hawkName, hawkAge, flySpeed){
        super(hawkName,hawkAge)
        this._flySpeed=flySpeed
    }
    fly(){
        console.log(`the ${this.name} is flying`)
    }
}
let rabbit1=new rabbit('carlos', 12, '40km/h')
console.log(rabbit1)
//"super" manda los parametros hacia el contrstuctor de la clase extendida, recuerda 
// que tambien debes mandarlos en los parametros de los contrsctor childs y parents