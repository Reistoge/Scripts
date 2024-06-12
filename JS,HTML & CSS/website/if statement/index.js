// if statement = a basic form of decision makeing
//                if a condition is true, then do something
//                if not, then dont do it!.


let age =66;
//important; the order of the if statement does matter , first check if age>=18, then check if age<0 and so on,
//           in this case the message shown will be you are an adult because age is >=18, they dont show you are a senior
//           because they are already a true if statement (THE FIRST).
//           the order of the statements depends on the context but in this case you should put the in descendant order.


if(age>=18){
    console.log('you are and adult!')
}
else if(age<0){
    console.log('you have not been born yet')

}
else if(age>=65){
    console.log('you are a senior')
}
else{
    console.log('you are not a child!')
}   

let online;
online=true;
if(online=true){
    console.log('You are online')
}
else {
    console.log('You are not online.')
}