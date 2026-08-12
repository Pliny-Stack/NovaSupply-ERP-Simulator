import random

import pandas as pd

from config.config import Config

from utils.id_generator import IDGenerator

class ReturnGenerator:

    def __init__(self):

        self.sales = pd.read_csv(
            "output/bronze/FactSales.csv"
        )

        self.return_reasons = [
            "Damaged Product",
            "Wrong Product",
            "Defective Product",
            "Customer Changed Mind",
            "Expired Product",
            "Incorrect Quantity",
            "Product Not as Expected"
        ]

        self.return_statuses = [
            "Approved",
            "Pending",
            "Rejected"
        ]

        self.restock_statuses = [
            "Restocked",
            "Damaged",
            "Disposed"
        ]

    def _generate_return(self, return_key):

        sale = self.sales.sample(1).iloc[0]

        sales_key = sale["SalesKey"]
        customer_key = sale["CustomerKey"]
        product_key = sale["ProductKey"]
        warehouse_key = sale["WarehouseKey"]

        quantity_sold = int(sale["QuantitySold"])

        quantity_returned = random.randint(1, quantity_sold)

        unit_price = float(sale["UnitPrice"])

        refund_amount = round(quantity_returned * unit_price, 2)

        sale_date = pd.to_datetime(sale["SaleDate"])

        return_date = sale_date + pd.Timedelta(days=random.randint(1, 30))

        return_status = random.choices(self.return_statuses, weights=[85, 10, 5])[0]

        return_reason = random.choice(self.return_reasons)

        if return_status == "Approved":
            restock_status = random.choices(self.restock_statuses, weights=[75, 15, 10])[0]
        else:
            restock_status = "Pending"

        return {
            "ReturnKey": return_key,
            "ReturnID": IDGenerator.generate("RET", return_key),
            "SalesKey": sales_key,
            "CustomerKey": customer_key,
            "ProductKey": product_key,
            "WarehouseKey": warehouse_key,
            "ReturnDate": return_date,
            "QuantityReturned": quantity_returned,
            "UnitPrice": unit_price,
            "RefundAmount": refund_amount,
            "ReturnReason": return_reason,
            "ReturnStatus": return_status,
            "RestockStatus": restock_status,
        }

    def generate(self):
        returns = []
        for return_key in range(1, Config.NUM_RETURNS + 1):
            returns.append(self._generate_return(return_key))
        return pd.DataFrame(returns)