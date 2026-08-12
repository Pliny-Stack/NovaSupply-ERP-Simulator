import random

import pandas as pd

from config.config import Config

from utils.date_generator import DateGenerator

class InventoryGenerator:

    def __init__(self):

        self.products = pd.read_csv(
            "output/bronze/DimProduct.csv"
        )

        self.warehouses = pd.read_csv(
            "output/bronze/DimWarehouse.csv"
        )

        self.inventory_counter = 1
    def _generate_inventory_record(self, inventory_key, warehouse_key, product_key):
        quantity = random.randint(50, 2500)

        reserved = random.randint(0, int(quantity * 0.2))

        available = quantity - reserved

        reorder_level = random.randint(25, 200)

        maximum_stock = quantity + random.randint(100, 1500)

        unit_cost = random.randint(500, 50000)

        inventory_value = quantity * unit_cost
        stock_count_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR + Config.NUMBER_OF_YEARS - 1,
        )

        return {
            "InventoryKey": inventory_key,
            "WarehouseKey": warehouse_key,
            "ProductKey": product_key,
            "QuantityOnHand": quantity,
            "ReservedQuantity": reserved,
            "AvailableQuantity": available,
            "ReorderLevel": reorder_level,
            "MaximumStockLevel": maximum_stock,
            "UnitCost": unit_cost,
            "InventoryValue": inventory_value,
            "LastStockCountDate": stock_count_date,
        }

    def generate(self):
        inventory = []

        inventory_key = 1

        for _, warehouse in self.warehouses.iterrows():

            number_of_products = random.randint(300, 800)

            selected_products = self.products.sample(
                number_of_products
            )

            for _, product in selected_products.iterrows():

                inventory.append(

                    self._generate_inventory_record(

                        inventory_key,

                        warehouse["WarehouseKey"],

                        product["ProductKey"]

                    )

                )

                inventory_key += 1

        return pd.DataFrame(inventory)