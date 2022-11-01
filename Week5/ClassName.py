class ClassName():
    def __init__(self):
        self.list = []

    def addItem(self, item):
        self.list.append(item)
        return self.list


    def searchItems(self, item):
        for items in self.list:
            if items == item:
                return True

    def seeList(self):
        return self.list