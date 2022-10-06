# Get “1” to print when passed a 1
# Get “2” to print when passed a 2
# Get “Pepsi” to print when passed a 3
# Get “Coke” to print when passed a 5

# Modify code for steps 3/4 so that your code can do this:
    # Get “Pepsi” when passed a 6 (a multiple of 3)
    # Get “Coke” when passed a 10 (a multiple of 5)
    # Get “PepsiCoke” when passed a 15 (a multiple of 3 and 5)

def kata(value):
    if (value == 1):
        print("1")
    elif (value == 2):
        print("2")
    elif (value % 5 == 0) and (value % 3 == 0):
        print("PepsiCoke")
    elif (value % 3 == 0):
        print("Pepsi")
    elif (value % 5 == 0):
        print("Coke")
    else:
        raise Exception("Input has no return.")
