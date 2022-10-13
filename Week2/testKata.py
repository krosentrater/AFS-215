
def PepsiCoke(value):
    if (value % 5 == 0) and (value % 3 == 0):
        return "PepsiCoke"
    elif (value == 1):
        return 1
    elif (value == 2):
        return 2
    elif (value == 3):
        return "Pepsi"
    elif (value == 5):
        return "Coke"
    elif (value % 3 == 0):
        return "Pepsi"
    elif (value % 5 == 0):
        return "Coke"

def testCanCallPepsiCoke():
    PepsiCoke(0)

def testCanCallPepsiCoke():
    assert PepsiCoke(15) == "PepsiCoke"

def testCanCallOne():
    assert PepsiCoke(1) == 1

def testCanCallTwo():
    assert PepsiCoke(2) == 2

def testCanCallPepsi():
    assert PepsiCoke(3) == "Pepsi"

def testCanCallCoke():
    assert PepsiCoke(5) == "Coke"

def testCanCallMult3():
    assert PepsiCoke(6) == "Pepsi"

def testCanCallMult5():
    assert PepsiCoke(10) == "Coke"
