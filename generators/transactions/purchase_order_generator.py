import random

import pandas as pd

from config.config import Config

from utils.id_generator import IDGenerator
from utils.date_generator import DateGenerator
from datetime import timedelta

class PurchaseOrderGenerator:

    def __init__(self):

        self.products = pd.read_csv(
            "output/bronze/DimProduct.csv"
        )

        self.suppliers = pd.read_csv(
            "output/bronze/DimSupplier.csv"
        )

        self.warehouses = pd.read_csv(
            "output/bronze/DimWarehouse.csv"
        )

        print("Purchase Order Generator")
        print("-------------------------")
        print("Products:", len(self.products))
        print("Suppliers:", len(self.suppliers))
        print("Warehouses:", len(self.warehouses))

    def test(self):
        print("-------------------------")
        print("Products:", len(self.products))
        print("Suppliers:", len(self.suppliers))
        print("Warehouses:", len(self.warehouses))

    def _generate_purchase_order(
        self,
        purchase_order_key,
        supplier,
        warehouse,
        product
    ):

        quantity = random.randint(100, 5000)

        unit_cost = random.randint(500, 50000)

        total_cost = quantity * unit_cost

        order_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR + Config.NUMBER_OF_YEARS - 1
        )

        lead_time = random.randint(3, 30)

        expected_delivery = order_date + timedelta(days=lead_time)

        status = random.choices(
            ["Open", "Received", "Partial", "Cancelled"],
            weights=[10, 75, 10, 5]
        )[0]

        if status == "Received":
            quantity_received = quantity

        elif status == "Partial":
            quantity_received = random.randint(
                1,
                quantity - 1
            )

        else:
            quantity_received = 0

        return {

            "PurchaseOrderKey": purchase_order_key,

            "PurchaseOrderID": IDGenerator.generate(
                "PO",
                purchase_order_key
            ),

            "SupplierKey": supplier["SupplierKey"],

            "WarehouseKey": warehouse["WarehouseKey"],

            "ProductKey": product["ProductKey"],

            "OrderDate": order_date,

            "ExpectedDeliveryDate": expected_delivery,

            "QuantityOrdered": quantity,
            "QuantityReceived": quantity_received,

            "UnitCost": unit_cost,

            "TotalCost": total_cost,

            "Status": status

        }

    def generate(self):

        purchase_orders = []

        purchase_order_key = 1

        for _ in range(Config.NUM_PURCHASE_ORDERS):

            supplier = self.suppliers.sample(1).iloc[0]

            warehouse = self.warehouses.sample(1).iloc[0]

            product = self.products.sample(1).iloc[0]

            purchase_orders.append(

                self._generate_purchase_order(

                    purchase_order_key,

                    supplier,

                    warehouse,

                    product

                )

            )

            purchase_order_key += 1

        return pd.DataFrame(purchase_orders)