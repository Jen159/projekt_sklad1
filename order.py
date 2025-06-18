class Order:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.items = []

    def add_item(self, name, quantity):
        if self.warehouse.remove_product(name, quantity):
            self.items.append((name, quantity))
        else:
            print(f"Produkt {name} nebyl přidán do objednávky.")

    def summary(self):
        print("\nObjednávka obsahuje:")
        for name, qty in self.items:
            print(f"{qty} ks {name}")