import random
import pandas as pd

from config.config import Config

from utils.id_generator import IDGenerator
from utils.date_generator import DateGenerator

class SalesGenerator:

    def __init__(self):

        self.customers = pd.read_csv(
            "output/bronze/DimCustomer.csv"
        )

        self.products = pd.read_csv(
            "output/bronze/DimProduct.csv"
        )

        self.warehouses = pd.read_csv(
            "output/bronze/DimWarehouse.csv"
        )

        self.employees = pd.read_csv(
            "output/bronze/DimEmployee.csv"
        )

        self.inventory = pd.read_csv(
            "output/bronze/FactInventory.csv"
        )
    def _generate_sale(self, sales_key):
        inventory_record = self.inventory.sample(1).iloc[0]

        warehouse_key = inventory_record["WarehouseKey"]
        product_key = inventory_record["ProductKey"]

        customer = self.customers.sample(1).iloc[0]
        employee = self.employees.sample(1).iloc[0]

        available_quantity = int(inventory_record["QuantityOnHand"])

        quantity_sold = random.randint(1, max(1, min(available_quantity, 20)))

        product = self.products[self.products["ProductKey"] == product_key].iloc[0]

        unit_cost = float(product["UnitCost"])

        unit_price = round(unit_cost * random.uniform(1.10, 1.40), 2)

        revenue = round(quantity_sold * unit_price, 2)

        cost = round(quantity_sold * unit_cost, 2)

        gross_profit = round(revenue - cost, 2)

        sale_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR + Config.NUMBER_OF_YEARS - 1,
        )

        return {
            "SalesKey": sales_key,
            "SalesID": IDGenerator.generate("SALE", sales_key),
            "CustomerKey": customer["CustomerKey"],
            "ProductKey": product_key,
            "WarehouseKey": warehouse_key,
            "EmployeeKey": employee["EmployeeKey"],
            "SaleDate": sale_date,
            "QuantitySold": quantity_sold,
            "UnitPrice": unit_price,
            "UnitCost": unit_cost,
            "Revenue": revenue,
            "Cost": cost,
            "GrossProfit": gross_profit,
        }

    def generate(self):
        sales = []

        for sales_key in range(
            1,
            Config.NUM_SALES + 1
        ):
            sales.append(
                self._generate_sale(
                    sales_key
                )
            )

        return pd.DataFrame(sales)
