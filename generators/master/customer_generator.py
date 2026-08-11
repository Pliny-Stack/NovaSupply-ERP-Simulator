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


    def _generate_employee(self, employee_key):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        full_name = f"{first_name} {last_name}"

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}@novasupply.com"
        )

        phone = generate_phone()

        department = random.choice(self.departments)

        job_title = random.choice(
            self.job_titles[department]
        )

        if "Officer" in job_title:
            salary = random.randint(180000, 350000)

        elif "Supervisor" in job_title:
            salary = random.randint(350000, 600000)

        elif "Manager" in job_title:
            salary = random.randint(700000, 1500000)

        elif "Analyst" in job_title:
            salary = random.randint(300000, 550000)

        else:
            salary = random.randint(200000, 400000)

        hire_date = DateGenerator.generate_date(
            Config.START_YEAR,
            Config.START_YEAR + Config.NUMBER_OF_YEARS - 1
        )

        status = random.choices(
            self.statuses,
            weights=[90, 7, 3]
        )[0]

        return {

        "EmployeeKey": employee_key,

        "EmployeeID": IDGenerator.generate(
            "EMP",
            employee_key
        ),

        "FirstName": first_name,

        "LastName": last_name,

        "FullName": full_name,

        "Department": department,

        "JobTitle": job_title,

        "Email": email,

        "Phone": phone,

        "HireDate": hire_date,

        "Salary": salary,

        "Status": status

    }

    