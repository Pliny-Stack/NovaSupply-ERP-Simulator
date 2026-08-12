import os
import pandas as pd


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

BRONZE_FOLDER = os.path.join(
    PROJECT_ROOT,
    "output",
    "bronze"
)


def load_table(filename):
    path = os.path.join(
        BRONZE_FOLDER,
        filename
    )

    return pd.read_csv(path)


def check_unique(df, column):
    return df[column].is_unique


def check_relationship(
    child_df,
    child_column,
    parent_df,
    parent_column
):
    return child_df[child_column].isin(
        parent_df[parent_column]
    ).all()


def validate_relationships():

    print("\nNOVASUPPLY RELATIONSHIP VALIDATION")
    print("=" * 60)

    # ==============================
    # LOAD TABLES
    # ==============================

    print("\nLoading tables...")

    customers = load_table("DimCustomer.csv")
    products = load_table("DimProduct.csv")
    suppliers = load_table("DimSupplier.csv")
    warehouses = load_table("DimWarehouse.csv")
    employees = load_table("DimEmployee.csv")

    inventory = load_table("FactInventory.csv")
    purchase_orders = load_table(
        "FactPurchaseOrder.csv"
    )
    shipments = load_table(
        "FactShipment.csv"
    )
    sales = load_table("FactSales.csv")
    returns = load_table("FactReturns.csv")

    print("Tables loaded successfully.")

    # ==============================
    # DIMENSION KEY UNIQUENESS
    # ==============================

    print("\nDimension Key Uniqueness")
    print("-" * 60)

    dimensions = [
        ("DimCustomer", customers, "CustomerKey"),
        ("DimProduct", products, "ProductKey"),
        ("DimSupplier", suppliers, "SupplierKey"),
        ("DimWarehouse", warehouses, "WarehouseKey"),
        ("DimEmployee", employees, "EmployeeKey"),
    ]

    all_passed = True

    for name, df, key in dimensions:

        result = check_unique(df, key)

        print(
            f"{name}.{key}:",
            "PASS" if result else "FAIL"
        )

        if not result:
            all_passed = False

    # ==============================
    # FACT → DIMENSION RELATIONSHIPS
    # ==============================

    print("\nFact → Dimension Relationships")
    print("-" * 60)

    relationships = [

        (
            "FactSales.CustomerKey",
            sales,
            "CustomerKey",
            customers,
            "CustomerKey"
        ),

        (
            "FactSales.ProductKey",
            sales,
            "ProductKey",
            products,
            "ProductKey"
        ),

        (
            "FactSales.WarehouseKey",
            sales,
            "WarehouseKey",
            warehouses,
            "WarehouseKey"
        ),

        (
            "FactSales.EmployeeKey",
            sales,
            "EmployeeKey",
            employees,
            "EmployeeKey"
        ),

        (
            "FactInventory.ProductKey",
            inventory,
            "ProductKey",
            products,
            "ProductKey"
        ),

        (
            "FactInventory.WarehouseKey",
            inventory,
            "WarehouseKey",
            warehouses,
            "WarehouseKey"
        ),

        (
            "FactPurchaseOrder.SupplierKey",
            purchase_orders,
            "SupplierKey",
            suppliers,
            "SupplierKey"
        ),

        (
            "FactPurchaseOrder.ProductKey",
            purchase_orders,
            "ProductKey",
            products,
            "ProductKey"
        ),

        (
            "FactPurchaseOrder.WarehouseKey",
            purchase_orders,
            "WarehouseKey",
            warehouses,
            "WarehouseKey"
        ),

        (
            "FactShipment.SupplierKey",
            shipments,
            "SupplierKey",
            suppliers,
            "SupplierKey"
        ),

        (
            "FactShipment.WarehouseKey",
            shipments,
            "WarehouseKey",
            warehouses,
            "WarehouseKey"
        ),

        (
            "FactReturns.CustomerKey",
            returns,
            "CustomerKey",
            customers,
            "CustomerKey"
        ),

        (
            "FactReturns.ProductKey",
            returns,
            "ProductKey",
            products,
            "ProductKey"
        ),

        (
            "FactReturns.WarehouseKey",
            returns,
            "WarehouseKey",
            warehouses,
            "WarehouseKey"
        ),
    ]

    for (
        name,
        child_df,
        child_column,
        parent_df,
        parent_column
    ) in relationships:

        result = check_relationship(
            child_df,
            child_column,
            parent_df,
            parent_column
        )

        print(
            f"{name}:",
            "PASS" if result else "FAIL"
        )

        if not result:
            all_passed = False

    # ==============================
    # FACT → FACT RELATIONSHIPS
    # ==============================

    print("\nFact → Fact Relationships")
    print("-" * 60)

    fact_relationships = [

        (
            "FactShipment.PurchaseOrderKey",
            shipments,
            "PurchaseOrderKey",
            purchase_orders,
            "PurchaseOrderKey"
        ),

        (
            "FactReturns.SalesKey",
            returns,
            "SalesKey",
            sales,
            "SalesKey"
        ),
    ]

    for (
        name,
        child_df,
        child_column,
        parent_df,
        parent_column
    ) in fact_relationships:

        result = check_relationship(
            child_df,
            child_column,
            parent_df,
            parent_column
        )

        print(
            f"{name}:",
            "PASS" if result else "FAIL"
        )

        if not result:
            all_passed = False

    # ==============================
    # INVENTORY GRAIN
    # ==============================

    print("\nInventory Grain Validation")
    print("-" * 60)

    duplicate_inventory_pairs = (
        inventory
        .duplicated(
            subset=[
                "WarehouseKey",
                "ProductKey"
            ]
        )
        .sum()
    )

    inventory_passed = (
        duplicate_inventory_pairs == 0
    )

    print(
        "WarehouseKey + ProductKey:",
        "PASS" if inventory_passed else "FAIL"
    )

    print(
        "Duplicate inventory pairs:",
        duplicate_inventory_pairs
    )

    if not inventory_passed:
        all_passed = False

    # ==============================
    # FINAL RESULT
    # ==============================

    print("\n" + "=" * 60)

    if all_passed:

        print(
            "ALL RELATIONSHIP CHECKS PASSED"
        )

    else:

        print(
            "SOME RELATIONSHIP CHECKS FAILED"
        )

    print("=" * 60)


if __name__ == "__main__":
    validate_relationships()