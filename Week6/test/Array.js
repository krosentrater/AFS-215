class Value{
    constructor(value){
        this.value = value;
    }
}

module.exports = class Array{
    constructor(){
        this.item = []
    }
    
    newItem = (newValue) => {
        // return true // Can call Function?
        this.item.push(newValue);
        return this.item;
    };

    viewItems = () => {return this.item};

    deleteItem = (delItem) => {
        let index = this.item.indexOf(delItem);
        let obliterated = this.item.splice(index, 1);
        return this.item;
    };

    searchArray = (searchTerm) => {
        let answer = this.item.includes(searchTerm);
        if (answer == true){
            return answer
        } 
        else {
            return 'Item not found.'
        }
    };
}

