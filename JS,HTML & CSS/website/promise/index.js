//promise = object that encapsulates the result of 
//          an asynchronous operation let asynchronous methods
//          return values like synchronous methods
//          "i promise to return something in the future"
const promise= new Promise((resolve, reject)=>{
    let fileloaded=false;
    if(fileloaded){
        resolve("file loaded")

    }
    else{
        reject("file NOT loaded")
    }

})
promise.then(value=>console.log(value))
.catch(error=> console.log(error))
 


const doAsyncStuffWithPromise=(numero1, numero2) => {
    const resultado=numero1+numero2;
    return new Promise(resolve=>{
        setTimeout(()=>{resolve(resultado)

        }, 5000 )
         
    })
}

doAsyncStuffWithPromise(1,2)
.then(result=>console.log(result))