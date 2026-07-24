from faker import Faker
import pandas as pd
import random

from config.config import Config
from utils.id_generator import IDGenerator


class SupplierGenerator:
    """Generates supplier master data."""

    def __init__(self):
        self.fake = Faker()
        random.seed(Config.RANDOM_SEED)
        Faker.seed(Config.RANDOM_SEED)

        self.supplier_types = [
            "Manufacturer",
            "Distributor",
            "Importer"
        ]

        self.categories = [
            "Food",
            "Beverages",
            "Healthcare",
            "Personal Care",
            "Household",
            "Electronics"
        ]

    def _generate_supplier(self, supplier_id: int) -> dict:
        """Generate one supplier record."""

        return {
    "SupplierKey": supplier_id,
    "SupplierID": IDGenerator.generate("SUP", supplier_id),
    "SupplierName": self.fake.company(),
    "SupplierType": random.choice(self.supplier_types),
    "Category": random.choice(self.categories),
    "ContactPerson": self.fake.name(),
    "Email": self.fake.company_email(),
    "Phone": self.fake.phone_number(),
    "LeadTimeDays": random.randint(2, 30),
    "SupplierRating": round(random.uniform(3.0, 5.0), 2),
}

    def generate(self) -> pd.DataFrame:
        """Generate the supplier dimension."""

        suppliers = [
            self._generate_supplier(i)
            for i in range(1, Config.SUPPLIERS + 1)
        ]

        return pd.DataFrame(suppliers)