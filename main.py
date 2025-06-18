from warehouse import Warehouse
from order import Order

# vytvoření skladu a přidání zásob
warehouse = Warehouse()
warehouse.add_product("Hřebíky", 100)
warehouse.add_product("Šrouby", 50)
warehouse.add_product("Matice", 200)

warehouse.show_inventory()

# vytvoření objednávky
order = Order(warehouse)
order.add_item("Hřebíky", 30)
order.add_item("Matice", 150)
order.add_item("Šrouby", 100)

order.summary()
warehouse.show_inventory()


