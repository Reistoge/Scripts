//get =binds an object property to a function
//     when that property is "accesed"
// set = binds an object to a function
//      when that property is "assigned" to a value

class Car{
    constructor(power, gas){
        // ahora las propiedades del objecto estan
        // protegidas ya que estamos manipulando o tomando acciones segun el cambio de los parametros
        this._gas=gas

        this._power=power    //¿why i have to change the name value " _ " ? R: para diferenciar parametro de property

        //the same thing as doing with get
        //this._power=power+`hp`
    }

    

    //¿porque solo cuando cambias el nombre en get la variable queda undefined si estas llamando abajo el nombre del parametro que defines?
    //  R: porque en un principio el parametro power es parte del constructor si tu lo llamas estaria indefinido no tienes acceso en cambio si llamas a con get esta ejecutara todo el trozo de codigo, si al return tu le colocas cualquier otra cosa eso pasara cuando 
    //  llames a power parametro si llamas a ._ no cambiara nada ya que no es parte del get en este caso
    get power(){

        // si tu llamas a power pasara esto:
        return `${this._power}hp`
        // (si llamas o accedes a _power no pasara esto)
    }
    //si tu llamas a gas pasara esto:
    get gas(){
        return `${this._gas}L (${this._gas /50*100}%)`
    }

    // set funciona cuando le cambiamos el valor
    //si tu le cambias el valor a la propiedad gas pasara esto.
    set gas(value){
        if(value > 50){
            value=50
        }
        if(value <0){
            value=0
        }
        this._gas=value;
    }
    


}
//get siempre se aplica una vez tu llamas a la variable es como si llamaras y antes de salir pasa por get

// En este caso set no se aplicara a gas por "set" solo se ejecuta cuando el property es 
//modificado despues de haber sido declarado osea cuando se cambia cuando lo "seteas denuevo"
let car =new Car(400,-200)

car.gas=-100

console.log(car.power)
console.log(car.gas)
console.log(car._gas)
