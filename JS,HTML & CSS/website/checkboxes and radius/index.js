document.getElementById('button').onclick=function(){

    const checkbox= document.getElementById('checkbox')
    const visaRds=document.getElementById('VisaRds')
    const paypalRds= document.getElementById("PaypalRds")
    const mastercardRds= document.getElementById("MastercardRds")
    
     
        if(checkbox.checked){
            console.log('You are subscribed!')
        }
        else{
            console.log('You are not subscribed')
        }
        if(visaRds.checked){
            console.log('you are paying with Visa!')
        }
        if(mastercardRds.checked){
            console.log('you are paying with MasterCard!')
        }
        if(paypalRds.checked){
            console.log('you are paying with PayPal!')
        }
        else{
            console.log('You have to select a payment option')
        }
        
} 

 
 