import random

import pandas as pd

from config.config import Config

from utils.id_generator import IDGenerator
from utils.date_generator import DateGenerator


class ShipmentGenerator:

    def __init__(self):

        self.purchase_orders = pd.read_csv(
            "output/bronze/FactPurchaseOrder.csv"
        )

        self.suppliers = pd.read_csv(
            "output/bronze/DimSupplier.csv"
        )

        self.warehouses = pd.read_csv(
            "output/bronze/DimWarehouse.csv"
        )


        self.carriers = [
    "GIG Logistics",
    "DHL",
    "ABC Transport",
    "God Is Good Motors",
    "UPS",
    "FedEx",
    "Red Star Express"
]


        self.statuses = [
            "In Transit",
            "Delivered",
            "Delayed",
            "Cancelled"
        ]

    def _generate_shipment(self, shipment_key):
        purchase_order = self.purchase_orders.sample(
            1
        ).iloc[0]

        purchase_order_key = purchase_order["PurchaseOrderKey"]

        supplier_key = purchase_order["SupplierKey"]

        warehouse_key = purchase_order["WarehouseKey"]

        order_date = pd.to_datetime(
            purchase_order["OrderDate"]
        )

        quantity_ordered = int(
            purchase_order["QuantityOrdered"]
        )

        quantity_shipped = random.randint(
            1,
            quantity_ordered
        )

        shipment_date = order_date + pd.Timedelta(
            days=random.randint(1, 7)
        )

        expected_delivery_date = (
            shipment_date
            + pd.Timedelta(days=random.randint(2, 14))
        )

        status = random.choices(
            self.statuses,
            weights=[10, 75, 10, 5]
        )[0]

        if status == "Delivered":

            actual_delivery_date = (
                expected_delivery_date
                + pd.Timedelta(
                    days=random.randint(-2, 3)
                )
            )

        elif status == "Delayed":

            actual_delivery_date = (
                expected_delivery_date
                + pd.Timedelta(
                    days=random.randint(3, 10)
                )
            )

        else:

            actual_delivery_date = None

        shipping_cost = round(
            random.uniform(5000, 150000),
            2
        )

        carrier = random.choice(
            self.carriers
        )

        return {
            "ShipmentKey": shipment_key,

            "ShipmentID": IDGenerator.generate(
                "SHIP",
                shipment_key
            ),

            "PurchaseOrderKey": purchase_order_key,

            "SupplierKey": supplier_key,

            "WarehouseKey": warehouse_key,

            "ShipmentDate": shipment_date,

            "ExpectedDeliveryDate": expected_delivery_date,

            "ActualDeliveryDate": actual_delivery_date,

            "QuantityShipped": quantity_shipped,

            "ShippingCost": shipping_cost,

            "Carrier": carrier,

            "Status": status
        }

    def generate(self):

        shipments = []

        for shipment_key in range(
    1,
    Config.NUM_SHIPMENTS + 1
):

            shipments.append(
                self._generate_shipment(
                    shipment_key
                )
            )

        return pd.DataFrame(shipments)