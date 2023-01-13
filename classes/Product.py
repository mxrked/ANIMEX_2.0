'''

    This is the Product class for the different products

'''

class Product:
    def __init__(self, itemName, itemPrice):
        self._itemName = itemName
        self._itemPrice = itemPrice

    def set_itemName(self, itemName):
        self._itemName = itemName

    def set_itemPrice(self, itemPrice):
        self._itemPrice = itemPrice

    def get_itemName(self):
        return self._itemName

    def get_itemPrice(self):
        return self._itemPrice



    def __str__(self):
        return f"Item Name: {self._itemName}\nItem Price: ${self._itemPrice}"



test = Product("Test 1", 45.55)
test2 = Product("Test 2", 35.15)
test3 = Product("Test 3", 71.63)
