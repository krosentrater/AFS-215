import pytest
from ClassName import ClassName

@pytest.fixture
def fixtureitem():
    fixtureitem = ClassName()
    return fixtureitem

def testCanCallClassName():
    ClassName()

def testCanAddItem(fixtureitem):
    # cn = ClassName()
    # assert cn.addItem('one') == ['one']
    assert fixtureitem.addItem('one') == ['one']

def testCanSearchItem(fixtureitem):
    # cn = ClassName()
    # cn.searchItems('')
    fixtureitem.searchItems('one')

def testCanSeeList(fixtureitem):
    # cn = ClassName()
    # list = cn.seeList()
    # print(list)
    print(fixtureitem.seeList())