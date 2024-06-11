// console.time()=starts a timer you can use to track how long an operation
//                takes give each timer a unique name

// how to assign the response time that is shown in the console to a value ???.
console.time("response Time")

setTimeout(()=> {console.log('Hello');}, 3000)
 

console.timeEnd("response Time")


   

