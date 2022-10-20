module.exports = class Greet{
    constructor(number){
        this.number = number
    };

    greeting = () => {
        if (typeof this.number != 'number'){
            return "The input is not a valid number.";
        }
        else if (this.number % 7 == 0 && this.number % 3 == 0){
            return "Good Evening";
        }
        else if (this.number % 7 == 0){
            return "Good Afternoon";
        }
        else if (this.number % 3 == 0){
            return "Good Morning";
        }
        else if (this.number % 3 != 0 || this.number % 7 != 0){
            return this.number.toString();
        }
    }
}