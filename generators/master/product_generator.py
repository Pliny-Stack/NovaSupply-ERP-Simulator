import random
import pandas as pd

from faker import Faker

from config.config import Config
from config.product_catalog import PRODUCT_CATALOG
from config.package_sizes import PACKAGE_SIZES

from utils.id_generator import IDGenerator
from utils.date_generator import DateGenerator
from utils.pricing import PricingEngine







class ProductGenerator:

    def __init__(self):

        self.fake = Faker()

        random.seed(Config.RANDOM_SEED)
        Faker.seed(Config.RANDOM_SEED)

        self.brands = [
            "FreshLife",
            "Urban Foods",
            "PureHarvest",
            "Prime Choice",
            "NatureBest",
            "HomeSelect",
            "Golden Basket",
            "Crystal Springs",
            "Family Essentials",
            "EverFresh"
        ]

        

    def _generate_product(self, product_key):
        # Select Category
        category = random.choice(list(PRODUCT_CATALOG.keys()))

        # Select Subcategory
        subcategories = PRODUCT_CATALOG[category]
        subcategory = random.choice(list(subcategories.keys()))

        # Select Base Product
        products = subcategories[subcategory]
        base_product = random.choice(products)

        # Select Brand
        brand = random.choice(self.brands)

        # Package Size
        package_size = random.choice(PACKAGE_SIZES[subcategory])

        # Product Name
        product_name = f"{brand} {base_product} {package_size}"

        # Cost
        unit_cost = round(random.uniform(100, 5000), 2)

        # Margin
        margin = round(random.uniform(0.15, 0.40), 2)

        # Selling Price
        selling_price = PricingEngine.calculate_price(
            unit_cost,
            margin
        )

        # Shelf Life
        if category == "Food":
            shelf_life = random.randint(30, 365)
            is_perishable = True
        else:
            shelf_life = random.randint(365, 1095)
            is_perishable = False

        return {

        "ProductKey": product_key,

        "ProductID": IDGenerator.generate(
    "PRD",
    product_key
),

        "Category": category,

        "SubCategory": subcategory,

        "Brand": brand,

        "BaseProduct": base_product,

        "ProductName": product_name,

        "PackageSize": package_size,

        "UnitCost": unit_cost,

        "SellingPrice": selling_price,

        "Margin": margin,

        "ShelfLifeDays": shelf_life,

        "IsPerishable": is_perishable,

        "LaunchDate": DateGenerator.generate_date(
            2019,
            2025
        ),

        "Status": "Active"
    }

    def generate(self):
        products = []

        for product_key in range(1, Config.NUM_PRODUCTS + 1):
            products.append(self._generate_product(product_key))

        return pd.DataFrame(products)