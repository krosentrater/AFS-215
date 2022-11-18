import pytest
from ToDoList import ToDoList

@pytest.fixture
def todolist():
    todolist = ToDoList()
    return todolist

def testCanCallList(todolist):
    todolist

def testCanAddItem(todolist):
    # link = ToDoList()
    todolist.addItem('Take Out Trash')
    assert todolist.addItem('Take Out Trash') == 'Take Out Trash'

def testCanAddMultipleItems(todolist):
    # link = ToDoList()
    items = ['Wash Dishes', 6, True, {"fence": "broken"}]
    assert todolist.addMultItems(items) == ['Wash Dishes', 6, True, {"fence": "broken"}]

def testRemoveFirstItem(todolist):
    # link = ToDoList()
    items = ['Wash Dishes', 6, True, {"fence": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeFirstItem() == [6, True, {"fence": "broken"}]

def testRemoveLastItem(todolist):
    # link = ToDoList()
    items = ['Wash Dishes', 6, True, {"fence": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeLastItem() == ['Wash Dishes', 6, True]

def testRemoveSpecificItem(todolist):
    # link = ToDoList()
    items = ['Wash Dishes', 6, True, {"fence": "broken"}]
    todolist.addMultItems(items)
    assert todolist.removeSpecificItem(6) == ['Wash Dishes', True, {"fence": "broken"}]