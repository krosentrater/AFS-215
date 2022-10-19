module.exports = class User{
    constructor(num1, num2, name = "Joe", age = 25){
        this.num1 = num1,
        this.num2 = num2,
        this.name = name,
        this.age = age
    };

    userInfo = () => {return `Hello ${this.name}, you're ${this.age} years old!`};
    add = () => {return this.num1 + this.num2};
    sub = () => {return this.num1 - this.num2};
    mult = () => {return this.num1 * this.num2};
    div = () => {return this.num1 / this.num2};
    str = () => {return this.num1.toString() + this.num2.toString()};
}