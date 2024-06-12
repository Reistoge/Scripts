// await = makes an async function wait for a Promise
async function loadFile() {
  let fileloaded = false;
  if (fileloaded) {
    return "file loaded";
  } else {
    throw "File NOT loaded";
  }
}
async function startProcess(){

    try{
        let message =await loadFile()
        console.log(message)
    }
    catch(error){
        console.log(error)
    }
}
startProcess()