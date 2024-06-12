//my way

document.getElementById('increaseBtn').onclick=function(){  
   
    document.getElementById('countLabel').innerHTML++ 
 
}
document.getElementById('decreaseBtn').onclick=function(){  
   
    document.getElementById('countLabel').innerHTML-- 
 
}
document.getElementById('resetBtn').onclick=function(){  
   
    document.getElementById('countLabel').innerHTML=0
 
}
 
 
//which one is better and why ??
 
/* brocode way
let count;

document.getElementById('increaseBtn').onclick=function(){  
    count++
    document.getElementById('countLabel').innerHTML=count 
 
}
document.getElementById('decreaseBtn').onclick=function(){  
    count--
    document.getElementById('countLabel').innerHTML=count 
 
}
document.getElementById('resetBtn').onclick=function(){  
    count=0
    document.getElementById('countLabel').innerHTML=count
 
}
*/