// class = a blueprint for creating objects 
//         define what properties and methods
//         have use a constructor for unique properties

class player{
    score=0;
    
    pause(){
        console.log(`you paused the game`)

    }
    exit(){
        console.log(`you exit the game`)
    }
}
const player1=new player();
player1.score=+1
console.log(player1.score)
