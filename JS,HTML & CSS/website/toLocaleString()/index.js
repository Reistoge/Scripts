//toLocaleString()=returns a string with a language sensitive representation of of this


// number.toLocaleString(locale, {options});

// 'locale' =specify that language(undefined = default)
// 'options' = object with formatting options
let myNum= 123456.789
// myNum =myNum.tolocaleString("en-US") // USA
// myNum=myNum.toLocaleString("hi-IN") // hindi
// myNum=myNum.toLocaleString("de-DE") // standard german

//myNum=myNum.toLocaleString("en-US", {style:"currency", currency: "USD"}) //for currency
//myNum=myNum.toLocaleString("hi-IN", {style:"currency", currency: "INR"}) //for currency
//myNum=myNum.toLocaleString("de-DE", {style:"currency", currency: "USD"}) //for currency

//myNum=myNum.toLocaleString(undefined, {style:"percent"}) // percent
//myNum=myNum.toLocaleString(undefined,{style:"unit", unit: "celsius"}) // unit measurement
console.log(myNum)