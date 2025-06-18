from product import Product

class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity):
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = Product(name, quantity)
        print(f"Přidáno: {quantity} ks {name}")

    def remove_product(self, name, quantity):
        if name in self.inventory and self.inventory[name].quantity >= quantity:
            self.inventory[name].quantity -= quantity
            print(f"Odebráno {quantity} ks {name}")
            return True
        else:
            print(f"Nedostatek zásob pro: {name}")
            return False

    def show_inventory(self):
        print("\nAktuální stav skladu:")
        for product in self.inventory.values():
            print(product)
