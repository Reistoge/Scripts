// switch = statement that examines a value for a match against many
//          case clauses, more efficient that many "else if" 
//          instead of 5 else if, is more efficient to use the switch
//          statement.
let grade ='A';
switch (grade){
    case 'A':
        console.log('you did great!');
        break;
    case 'B':
        console.log('you did good!')
        break
    case 'C':
        console.log('you did okay!')    
        break
    case 'D':
        console.log('you passed ... barely')
        break
    case 'F':
        console.log('YOU FAILED')
        break
    default:
        console.log(grade+' is not a grade!')

}
// you can also use true and false statement with switch


let grade2 =20;
switch (true){
    case grade2>=90:
        console.log('you did great!');
        break;
    case grade2>=75:
        console.log('you did good!')
        break
    case grade2>=55:
        console.log('you did okay!')    
        break
    case grade2>=40:
        console.log('you passed ... barely')
        break
    case grade2<40:
        console.log('YOU FAILED')
        break
    default:
        console.log(grade2+' is not a grade!')
        
// remember to put the cases in descendent value, thi prevents errors.



}