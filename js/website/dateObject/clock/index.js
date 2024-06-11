const mylabel=document.getElementById('myLabel')
setInterval(update,1000)
function update(){
    let date = new Date()
    mylabel.innerHTML= formatTime(date)
 


    function formatTime(date){
        let hours=date.getHours()
        let minutes=date.getMinutes()
        let seconds=date.getSeconds()
        //let ms=date.getMilliseconds()
        let amOrPm=hours<=12? 'AM' : 'PM';
        hours=(hours%12) || 12

        hours=formatZeroes(hours)
        minutes=formatZeroes(minutes)
        seconds=formatZeroes(seconds)
        return `${hours}:${minutes}:${seconds} ${amOrPm}`
    }
    function formatZeroes(time){
        time=time.toString();
        return time.length < 2 ? '0'+ time: time;
        
    }
    

}
$
