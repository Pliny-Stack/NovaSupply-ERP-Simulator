import random

import pandas as pd

from faker import Faker

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


class CustomerGenerator:

    def __init__(self):
        self.fake = Faker()
        self.customer_types = [
            "Retail",
            "Wholesale",
            "Distributor",
            "Corporate",
            "Government"
        ]
        self.customer_segments = [
            "Bronze",
            "Silver",
            "Gold",
            "VIP"
        ]
        self.statuses = [
            "Active",
            "Inactive",
            "Suspended"
        ]

    def _generate_customer(self, customer_key):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}@"
            f"{random.choice(EMAIL_DOMAINS)}"
        )

        phone = generate_phone()

        region, state, city = generate_location()
        customer_name = f"{first_name} {last_name}"
        company_name = ""

        customer_type = random.choice(self.customer_types)

        if customer_type != "Retail":
            company_name = (
                f"{random.choice(['Nova', 'Prime', 'Royal', 'Fresh', 'Urban', 'Health'])} "
                f"{random.choice(['Stores', 'Supermarket', 'Pharmacy', 'Distribution', 'Ventures'])}"
            )

        if customer_type == "Retail":
            credit_limit = random.randint(100000, 500000)
        elif customer_type == "Wholesale":
            credit_limit = random.randint(2000000, 10000000)
        elif customer_type == "Distributor":
            credit_limit = random.randint(10000000, 30000000)
        elif customer_type == "Corporate":
            credit_limit = random.randint(20000000, 50000000)
        else:
            credit_limit = random.randint(5000000, 25000000)

        registration_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR + Config.NUMBER_OF_YEARS - 1
        )

        return {
            "CustomerKey": customer_key,
            "CustomerID": IDGenerator.generate("CUST", customer_key),
            "CustomerType": customer_type,
            "CustomerSegment": random.choice(self.customer_segments),
            "CustomerName": customer_name,
            "CompanyName": company_name,
            "Email": email,
            "Phone": phone,
            "Status": random.choices(self.statuses, weights=[90, 8, 2])[0],
            "Region": region,
            "State": state,
            "City": city,
            "CreditLimit": credit_limit,
            "RegistrationDate": registration_date,
        }

    def generate(self):
        customers = []

        for customer_key in range(1, Config.NUM_CUSTOMERS + 1):
            customers.append(
                self._generate_customer(customer_key)
            )

        return pd.DataFrame(customers)
