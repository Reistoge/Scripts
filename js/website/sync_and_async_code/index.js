//synchronous code = In an ordered sequence.
//                   step-by-step linear instructions 
//                   (start now, finish now)


//asynchronous code =Out of sequence.
//                   Ex. Acces a database
//                       fetching a file 
//                       task that take time 
//                      (start now, finish sometime later)


console.log('Start now')
console.log('End')

setTimeout(()=>console.log(`thanks for waiting`), 4000)
