const Greet = require('./Greet');

const three = new Greet(3);
const seven = new Greet(7);
const both = new Greet(21);
const not = new Greet(2);
const cond = new Greet('not a number');

console.log(three.greeting());
console.log(seven.greeting());
console.log(both.greeting());
console.log(not.greeting());
console.log(cond.greeting());