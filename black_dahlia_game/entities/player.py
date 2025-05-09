class Player:
    def __init__(self):
        self.name = "Detective"
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        return self.inventory
