let prices = [10, 24, 40, 56, 87];
console.log("Display each element");
for (let i = 0; i < prices.length; i++) {
  console.log(prices[i]);
}

console.log();
console.log("Backwards option");
for (let i = prices.length - 1; i >= 0; i--) {
  console.log(prices[i]);
}
//remember the for condition in the middle has to be true to continue.
console.log();
console.log('Display each element but with for("element"  of  "array")  option');
// for( of ) selects each element array and sum +1 to the index  every time he enter in the for loop so we call each price
for (price of prices) {
  console.log(price);
}
