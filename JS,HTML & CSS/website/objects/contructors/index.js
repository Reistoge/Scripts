// constructor = a special method of a class, accepts argumentos and assign properties
class Player{
    constructor(name, id, region){
        this.name=name
        this.id=id
        this.region=region   
        
    }
    playerInfo(){
        console.log(this.name, this.id, this.region)

    }

}

player1=new Player('bruh', '#1A233-2234F', 'US')
player1.playerInfo()