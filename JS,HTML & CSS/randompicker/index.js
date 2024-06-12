


let button=document.getElementById('mybutton')
let frame1=document.getElementById('frame1')
let vehicles=[
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
    'image11',
    'image12',
    'image13',
    'image14',
    'image15',
    'image16',
    'image17',
    'image18',
    'image19',
    'image20',
    'image21',
    'image22',
    'image23',
    'image24',
    'image25',
    'image26',
    'image27',
    'image28',
    'image29',
    'image29',
    'image30',
    'image31',
    'image32',
    'image33',
    'image34',
    'image35',
    'image36',
    'image37',
    'image38',
    'image39',
    'image40',
    'image41'


]
selectRandomIndex()
function selectRandomIndex(){
    let randomIndex1=Math.floor(Math.random()*vehicles.length)
    console.log(vehicles[randomIndex1])
    return randomIndex1;
}
button.onclick = function(){
    let index= selectRandomIndex()
 
    frame1.src=`./vehicles/${vehicles[index]}.jpg` 
    

}
/////

let button2=document.getElementById('mybutton2')
let frame2=document.getElementById('frame2')
let images2=[
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
    'image11',
    'image12',
    'image13',
    'image14',
    'image15',
     
  


]
selectRandomIndex2()
function selectRandomIndex2(){
    let randomIndex2=Math.floor(Math.random()*images2.length)
    console.log(images2[randomIndex2])
    return randomIndex2;
}
button2.onclick = function(){
    let index2= selectRandomIndex2()
 
    frame2.src=`./Tires/${images2[index2]}.jpg` 
    

}



////
let button3=document.getElementById('mybutton3')
let frame3=document.getElementById('frame3')
let images3=[
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
    'image11',
    'image12',
    'image13',
    'image14',
    'image15',
    

]
selectRandomIndex3()
function selectRandomIndex3(){
    let randomIndex3=Math.floor(Math.random()*images3.length)
    console.log(images3[randomIndex3])
    return randomIndex3;
}
button3.onclick = function(){
    let index3= selectRandomIndex2()
 
    frame3.src=`./Gliders/${images3[index3]}.jpg` 
    

}

////////
let button4=document.getElementById('characterButton')
let frame4=document.getElementById('frame4')
let images4=[
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
    'image11',
    'image12',
    'image13',
    'image14',
    'image15',
    'image16',
    'image17',
    'image18',
    'image19',
    'image20',
    'image21',
    'image22',
    'image23',
    'image24',
    'image25',
    'image26',
    'image27',
    'image28',
    'image29',
    'image29',
    'image30',
    'image31',
    'image32',
    'image33',
    'image34',
    'image35',
    'image36',
    'image37',
    'image38',
    'image39',
    'image40',
    'image41',
    'image42',
    'image43',
    'image44',
    'image45'
    

]
selectRandomIndex4()
function selectRandomIndex4(){
    let randomIndex4=Math.floor(Math.random()*images4.length)
    console.log(images4[randomIndex4])
    return randomIndex4;
}

button4.onclick=function(){
    frame4.src=`./characters/${images4[selectRandomIndex4()]}.jpg` 

}







