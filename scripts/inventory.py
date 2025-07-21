class Inventory():
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.pop(item)
    
    def get_items(self):
        return self.items

class Item():
    def __init__(self, name, value=0, weight=0):
        self.name = name
        self.value = value
        self.weight = weight