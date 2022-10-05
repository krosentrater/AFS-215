class Types:
    def __init__(self):
        self.types = []

    def add_num(self, num):
        if (type(num) != int):
            raise Exception("Entered value is not a number!")
        else:
            self.types.append(num)
    
    def add_string(self, string):
        if (type(string) != str):
            raise Exception("Entered value is not a string!")
        else:
            self.types.append(string)
    
    def add_dic(self, dic):
        if (type(dic) != dict):
            raise Exception("Entered values are not dictionaries!")
        else:
            self.types.append(dic)
    
    def add_tuple(self, tup):
        if (type(tup) != tuple):
            raise Exception("Entered value is not a tuple!")
        else:
            self.types.append(tup)

    def transform(self):
        new_tuple = tuple(self.types)
        return new_tuple


link = Types() # Class link

link.add_num(2) # Add number

link.add_string("Hello") # Add string

dictionary = {'key1':'value1'} # Store dictionary value
link.add_dic(dictionary) # Add dictionary

tupl = ('apple', 88, {"key1":"trial"}) # Store tuple value
link.add_tuple(tupl) # Adds tuple


print('List: ', link.types) # Print List
print('Tuple', link.transform()) # Print Tuple