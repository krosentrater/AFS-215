const User = require('./User');

const guest1 = new User(8, 2, 'Yuki', 25);
const guest2 = new User(10, 10, 'Cloud', 27);

console.log('*****Guest 1*****:')
console.log(guest1.userInfo());
console.log(guest1.add());
console.log(guest1.sub());
console.log(guest1.div());
console.log(guest1.mult());
console.log(guest1.str());
console.log("\n")

console.log('*****Guest 2*****:')
console.log(guest2.userInfo());
console.log(guest2.add());
console.log(guest2.sub());
console.log(guest2.div());
console.log(guest2.mult());
console.log(guest2.str());