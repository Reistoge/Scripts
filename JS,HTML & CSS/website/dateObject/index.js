//The date object is used to work with dates and times

//let date =new Date(0);     //this shows the inital date
let date = new Date(); //current date.
//let date=new Date(10000000)  // this adds in milisecond to the initial dateTime.
//1.year 2.month (0,11) 3.day 4.hour 5.minutes 6.seconds 7.miliseconds
//let date=new Date(2023,3,11,14, 23,24,50)
//let date=new Date("january 1, 2023 00:00:00")

/////////////
// get the property values of the date object to assign or use it.
/* 
let year=date.getFullYear()
let month=date.getMonth() + 1
let day=date.getDay()
let hours = date.getHours()
let minutes = date.getMinutes()
let seconds = date.getSeconds()
let ms = date.getMilliseconds()
*/
///////////////////

//////////////
// set the property values of the date object
/* date.setFullYear(2004)
date.setMonth(7)
date.setDate(23)
date.setHours(14)
date.setMinutes(30)
date.setSeconds(20)
date.setMilliseconds(10)
*/
///////

// date = date.toLocaleString(); // formats the current date to locale
document.getElementById('myLabel').innerHTML= formatTime(date)
 
function formatDate(date){
  let year=date.getFullYear()
  let month=date.getMonth()
  let day =date.getDate()

  return `${day}/${month}/${year}`
  
}

function formatTime(date){
  let hours=date.getHours()
  let minutes=date.getMinutes()
  let seconds=date.getSeconds()
  let amOrPm=hours<=12? 'am': 'pm';
  hours = (hours%12)|| 12
  
  return `${hours}:${minutes}:${seconds} ${amOrPm}`
}







/* 
let x=3
let example= 3-x || 24
console.log(example)
 */

 
