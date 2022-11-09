const expect = require('chai').expect;
const Array = require('./Array.js');

it('Can Call Function?', function(){
    // let item = new Array();
    expect(item.newItem(true)).to.equal(true)
})

it('Add New Item', function(){
    // let item = new Array();
    expect(item.newItem(1)).to.deep.equal([1]);
});

it('View Array Items', function(){
    // let item = new Array();
    let item1 = item.newItem(1);
    let item2 = item.newItem(2);
    expect(item.viewItems()).to.deep.equal([1, 2]);
});

it('Remove Specific Item', function(){
    // let item = new Array();
    let item1 = item.newItem(1);
    let item2 = item.newItem(2);
    let item3 = item.newItem(3);
    expect(item.deleteItem(2)).to.deep.equal([1, 3]);
});

it('Search For Item', function(){
    // let item = new Array();
    let item1 = item.newItem('one');
    let item2 = item.newItem('two');
    let item3 = item.newItem(3);
    expect(item.searchArray('one')).to.equal(true);
});

beforeEach(function(){
    item = new Array();
});

before(function(){
    console.log('***Testing Starting***')
});

afterEach(function(){
    console.log('***Test Complete***')
})

after(function(){
    console.log('***Testing is Complete***')
})