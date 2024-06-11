//this = reference to a particular object
//       the object depends on the inmediate context

const car1={
    model:'Mustang',
    color:"Red",
    year:2023,
    drive: function(){
        console.log(`you drive the ${this.model}`)
        // this are the same thing because this refers to the 
        console.log(`you drive the ${car1.model}`)

    }
}
car1.drive()
console.log(this)