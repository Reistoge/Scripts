// nested loop = repeat some code a 
//               certain amount of times * amount of times.
 
for( let counter=0; counter<=3; counter++){
    for(let counter2=0; counter2<=5; counter2++){
        console.log(counter2)
    }
}
let symbol =window.prompt('enter a symbol')
let rows =window.prompt('enter the number of rows')
let colums =window.prompt('enter the number of colums')

for(let i=1; i<=colums; i++){

    for(let j=1; j<=rows; j++){
        document.getElementById('myRectangle').innerHTML+=symbol
    }
    document.getElementById('myRectangle').innerHTML+='<br>'

}

