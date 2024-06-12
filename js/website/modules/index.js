// the idea behind a module is that its a file reusable
// we can import sections of pre-written code to use whenever we want
// Great for any general utility values and functions
// Helps to make your code more reusable and maintanable
// think of modules as separate chapters of a book


// to import the variables or functions depends on the api or program do you use
// to import from node you have to create a package.json file and write {type:module} inside of them
// also in node you have to specify the file with his extension



// to import the variables to browser, in the index.html you have to put in the script brackets the type:module
// and its not necessary to put the entire extension
// so to have it in both (node js and browser) you have to:
// 1. create a package.json file inside of your directory
// 2. in the package.json file write { "type": "module" }
// 3. in your html the script bracket should look like this:
//      <script src="index.js" type="module" defer></script>

import {PI, getArea, getCircumference} from "./math_utils.js"
console.log(PI) 
console.log(getArea(12))
console.log(getCircumference(12))
