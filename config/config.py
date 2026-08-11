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

    NUM_PRODUCTS = 2500

    NUM_SUPPLIERS = 500

    NUM_CUSTOMERS = 50000

    NUM_EMPLOYEES = 100

    NUM_WAREHOUSES = 75

    NUM_CARRIERS = 25

    NUM_PROMOTIONS = 100

    # ---------------------------------
    # Transaction Data
    # ---------------------------------

    NUM_SALES = 500000

    NUM_PURCHASE_ORDERS = 150000

    NUM_INVENTORY_RECORDS = 300000

    NUM_SHIPMENTS = 200000

    NUM_RETURNS = 50000
    NUM_EMPLOYEES = 100

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