class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name, count):
        if item_name not in self.items or self.items[item_name] < count:
            return f"Cannot remove {count} {item_name}"

        self.items[item_name] -= count
        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{count} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
fresh_shop.add_item("Bananas")
print(fresh_shop.items)
fresh_shop.add_item("Bananas")
print(fresh_shop.remove_item("Bananas", 1))
