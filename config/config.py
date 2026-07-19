"""
Configuration file for NovaSupply ERP Simulator

Author: Okoro Uche
Project: NovaSupply ERP Simulator
Version: 1.0
"""

from dataclasses import dataclass


@dataclass
class Config:

    # ---------------------------------
    # General
    # ---------------------------------

    RANDOM_SEED = 42

    COMPANY_NAME = "NovaSupply Logistics Ltd"

    START_YEAR = 2021

    NUMBER_OF_YEARS = 5

    # ---------------------------------
    # Master Data
    # ---------------------------------

    PRODUCTS = 2500

    SUPPLIERS = 500

    CUSTOMERS = 50000

    EMPLOYEES = 100

    WAREHOUSES = 75

    CARRIERS = 25

    PROMOTIONS = 100

    # ---------------------------------
    # Transaction Data
    # ---------------------------------

    SALES = 500000

    PURCHASE_ORDERS = 150000

    INVENTORY_RECORDS = 300000

    SHIPMENTS = 200000

    RETURNS = 50000

    # ---------------------------------
    # Export Settings
    # ---------------------------------

    EXPORT_CSV = True

    EXPORT_PARQUET = False

    OUTPUT_FOLDER = "output/bronze"

    # ---------------------------------
    # Data Quality Settings
    # ---------------------------------

    DUPLICATE_RATE = 0.005

    MISSING_VALUE_RATE = 0.02

    INVALID_RECORD_RATE = 0.01