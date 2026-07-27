import random

import pandas as pd

from config.config import Config

from utils.id_generator import IDGenerator

from utils.date_generator import DateGenerator

from utils.reference_data import (
    FIRST_NAMES,
    LAST_NAMES,
    EMAIL_DOMAINS,
    generate_phone,
    generate_location
)

class WarehouseGenerator:

    def __init__(self):

        self.warehouse_types = [
            "Distribution Centre",
            "Regional Warehouse",
            "Fulfilment Centre",
            "Depot"
        ]

        self.statuses = [
            "Active",
            "Maintenance",
            "Closed"
        ]

    def _generate_warehouse(self, warehouse_key):

        region, state, city = generate_location()

        warehouse_type = random.choice(self.warehouse_types)

        warehouse_name = f"{city} {warehouse_type}"

        manager_name = (
            f"{random.choice(FIRST_NAMES)} "
            f"{random.choice(LAST_NAMES)}"
        )

        email = (
            f"{city.lower().replace(' ', '')}@"
            f"{random.choice(EMAIL_DOMAINS)}"
        )

        phone = generate_phone()

        if warehouse_type == "Depot":

            capacity = random.randint(2000, 5000)

        elif warehouse_type == "Regional Warehouse":

            capacity = random.randint(8000, 20000)

        elif warehouse_type == "Distribution Centre":

            capacity = random.randint(20000, 50000)

        else:

            capacity = random.randint(10000, 25000)

        utilization = random.randint(35, 95)

        opening_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR +
            Config.NUMBER_OF_YEARS - 1
        )

        current_inventory = int(
            capacity * utilization / 100
        )

        return {

            "WarehouseKey": warehouse_key,

            "WarehouseID": IDGenerator.generate(
                "WH",
                warehouse_key
            ),

            "WarehouseName": warehouse_name,

            "WarehouseType": warehouse_type,

            "Region": region,

            "State": state,

            "City": city,

            "StorageCapacity": capacity,

            "CurrentUtilization": utilization,

            "ManagerName": manager_name,

            "Phone": phone,

            "Email": email,

            "OpeningDate": opening_date,

            "Status": random.choices(
                self.statuses,
                weights=[95, 4, 1]
            )[0],

            "CurrentInventory": current_inventory,

        }

    def generate(self):

        warehouses = []

        for warehouse_key in range(
            1,
            Config.NUM_WAREHOUSES + 1
        ):
            warehouses.append(
                self._generate_warehouse(
                    warehouse_key
                )
            )

        return pd.DataFrame(warehouses)


if __name__ == "__main__":
    print("\nValidation")
    print("-" * 40)

    generator = WarehouseGenerator()
    warehouses = generator.generate()

    print("Rows:", len(warehouses))

    print(
        "Duplicate Warehouse IDs:",
        warehouses["WarehouseID"].duplicated().sum()
    )

    print(
        "Duplicate Warehouse Keys:",
        warehouses["WarehouseKey"].duplicated().sum()
    )

    print("\nMissing Values")

    print(warehouses.isnull().sum())

    warehouses.to_csv(
    "output/bronze/DimWarehouse.csv",
    index=False
)