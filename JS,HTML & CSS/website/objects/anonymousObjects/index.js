// anonymous objects = Objects without a name 
//                     not directly referenced
//                     less syntax. No need for unique names


class Console{
    
    constructor(name, year, model ){
        this._model=model
        this._year=year
        this._name=name
    }

}
//in this case all the new objects are in array so you can reference with his element index
// thus use less syntax and you are creating one variable (the array) instead of creating one for each object.

Handhelds=[new Console('Gameboy', 1989, 'Classic-White'),
      new Console('Gameboy Pocket',1996, 'Grey'),
      new Console('Gameboy Color',1998, 'Blue'),
      new Console('Gameboy Advance',2001, 'Orange'),
      new Console('Gameboy Advance SP',2003, 'Famicom-20th-anniversary'),
      new Console('Nintendo ds',2004, 'Grey'),
      new Console('Gameboy Advance Micro',2005, 'Red'),
]

for(const handheld of Handhelds){
    console.log(handheld._name)
}

Handhelds.forEach(handheld => {console.log(handheld._name, handheld._year, handheld._model)

})

