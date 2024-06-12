// async= makes a function return a value 
async function loadFile(){
let fileloaded=true;
if (fileloaded){
    return 'file loaded'
}
else{
    throw 'File NOT loaded'
}
}
loadFile().then(value=> console.log(value))
        .catch(error=> console.log(error))