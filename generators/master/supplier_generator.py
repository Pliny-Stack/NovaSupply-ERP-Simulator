from faker import Faker
import random
import pandas as pd

from config.config import Config

fake = Faker()


class SupplierGenerator:

    def __init__(self):
        random.seed(Config.RANDOM_SEED)
        Faker.seed(Config.RANDOM_SEED)

    def generate(self):

        supplier_types = [
            "Manufacturer",
            "Distributor",
            "Importer"
        ]

        categories = [
            "Food",
            "Beverages",
            "Healthcare",
            "Personal Care",
            "Household",
            "Electronics"
        ]

        suppliers = []

        for supplier_id in range(1, Config.SUPPLIERS + 1):

            suppliers.append({

                "SupplierKey": supplier_id,

                "SupplierName": fake.company(),

                "SupplierType": random.choice(supplier_types),

                "Category": random.choice(categories),

                "ContactPerson": fake.name(),

                "Email": fake.company_email(),

                "Phone": fake.phone_number(),

                "LeadTimeDays": random.randint(2, 30),

                "SupplierRating": round(random.uniform(3.0, 5.0), 2)

            })

        return pd.DataFrame(suppliers)