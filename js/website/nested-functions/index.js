// nested functions = functions inside other functions
//                    outer functions have acces to inner functions 
//                    inner functions are "hidden" from outside 
//                    used in closures.
let userName='Bro'
let userInbox
// functions inside functions can only be used/called inside of the principal function.
// this adds security to the code.
function login(){
    displayUserName()
    displayUserInbox()
    function displayUserName(){
        console.log(`Welcome ${userName}`)
    
    }
    function displayUserInbox(){
        console.log(`you have ${userInbox} new messages`)
    }
}

