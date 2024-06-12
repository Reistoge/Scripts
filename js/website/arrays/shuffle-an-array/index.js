let cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
shuffle(cards)
cards.forEach(x=> console.log(x))
console.log(cards.indexOf('A'))

function shuffle(array){
    let currentIndex=array.length
    while(currentIndex!=0){
        let randomIndex=Math.floor(Math.random()*array.length)
        currentIndex--
        let temp = array[currentIndex]
        array[currentIndex]=array[randomIndex]
        array[randomIndex]=temp

    }

    return array
}


