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
    return pd.read_csv(
        os.path.join(BRONZE_FOLDER, filename)
    )


def check(name, condition, failures):
    count = int(condition.sum())

    status = "PASS" if count == 0 else "FAIL"

    print(f"{name}: {status} ({count} violations)")

    if count > 0:
        failures.append((name, count))


def validate_business_rules():

    print("\nNOVASUPPLY BUSINESS RULE VALIDATION")
    print("=" * 65)

    failures = []

    # ==========================================
    # LOAD DATA
    # ==========================================

    print("\nLoading tables...")

    sales = load_table("FactSales.csv")
    purchases = load_table("FactPurchaseOrder.csv")
    inventory = load_table("FactInventory.csv")
    shipments = load_table("FactShipment.csv")
    returns = load_table("FactReturns.csv")

    print("Tables loaded successfully.")

    # ==========================================
    # SALES
    # ==========================================

    print("\nSALES RULES")
    print("-" * 65)

    check(
        "QuantitySold > 0",
        sales["QuantitySold"] <= 0,
        failures
    )

    check(
        "UnitPrice > 0",
        sales["UnitPrice"] <= 0,
        failures
    )

    check(
        "Revenue calculation",
        (
            sales["Revenue"].round(2)
            != (
                sales["QuantitySold"]
                * sales["UnitPrice"]
            ).round(2)
        ),
        failures
    )

    check(
        "Cost calculation",
        (
            sales["Cost"].round(2)
            != (
                sales["QuantitySold"]
                * sales["UnitCost"]
            ).round(2)
        ),
        failures
    )

    check(
        "GrossProfit calculation",
        (
            sales["GrossProfit"].round(2)
            != (
                sales["Revenue"]
                - sales["Cost"]
            ).round(2)
        ),
        failures
    )

    # ==========================================
    # PURCHASE ORDERS
    # ==========================================

    print("\nPURCHASE ORDER RULES")
    print("-" * 65)

    check(
        "QuantityOrdered > 0",
        purchases["QuantityOrdered"] <= 0,
        failures
    )

    check(
        "QuantityReceived >= 0",
        purchases["QuantityReceived"] < 0,
        failures
    )

    check(
        "QuantityReceived <= QuantityOrdered",
        purchases["QuantityReceived"]
        > purchases["QuantityOrdered"],
        failures
    )

    check(
        "TotalCost calculation",
        (
            purchases["TotalCost"].round(2)
            != (
                purchases["QuantityOrdered"]
                * purchases["UnitCost"]
            ).round(2)
        ),
        failures
    )

    order_dates = pd.to_datetime(
        purchases["OrderDate"]
    )

    expected_dates = pd.to_datetime(
        purchases["ExpectedDeliveryDate"]
    )

    check(
        "ExpectedDeliveryDate >= OrderDate",
        expected_dates < order_dates,
        failures
    )

    # ==========================================
    # INVENTORY
    # ==========================================

    print("\nINVENTORY RULES")
    print("-" * 65)

    check(
        "QuantityOnHand >= 0",
        inventory["QuantityOnHand"] < 0,
        failures
    )

    check(
        "ReservedQuantity >= 0",
        inventory["ReservedQuantity"] < 0,
        failures
    )

    check(
        "AvailableQuantity >= 0",
        inventory["AvailableQuantity"] < 0,
        failures
    )

    check(
        "AvailableQuantity calculation",
        (
            inventory["AvailableQuantity"]
            != (
                inventory["QuantityOnHand"]
                - inventory["ReservedQuantity"]
            )
        ),
        failures
    )

    check(
        "InventoryValue calculation",
        (
            inventory["InventoryValue"].round(2)
            != (
                inventory["QuantityOnHand"]
                * inventory["UnitCost"]
            ).round(2)
        ),
        failures
    )

    check(
        "ReservedQuantity <= QuantityOnHand",
        inventory["ReservedQuantity"]
        > inventory["QuantityOnHand"],
        failures
    )

    # ==========================================
    # SHIPMENTS
    # ==========================================

    print("\nSHIPMENT RULES")
    print("-" * 65)

    check(
        "QuantityShipped > 0",
        shipments["QuantityShipped"] <= 0,
        failures
    )

    shipment_dates = pd.to_datetime(
        shipments["ShipmentDate"]
    )

    shipment_expected = pd.to_datetime(
        shipments["ExpectedDeliveryDate"]
    )

    shipment_actual = pd.to_datetime(
        shipments["ActualDeliveryDate"]
    )

    check(
        "ExpectedDeliveryDate >= ShipmentDate",
        shipment_expected < shipment_dates,
        failures
    )

    check(
        "ActualDeliveryDate >= ShipmentDate",
        (
            shipment_actual.notna()
            & (
                shipment_actual
                < shipment_dates
            )
        ),
        failures
    )

    # ==========================================
    # RETURNS
    # ==========================================

    print("\nRETURN RULES")
    print("-" * 65)

    check(
        "QuantityReturned > 0",
        returns["QuantityReturned"] <= 0,
        failures
    )

    check(
        "UnitPrice > 0",
        returns["UnitPrice"] <= 0,
        failures
    )

    check(
        "RefundAmount calculation",
        (
            returns["RefundAmount"].round(2)
            != (
                returns["QuantityReturned"]
                * returns["UnitPrice"]
            ).round(2)
        ),
        failures
    )

    # ==========================================
    # FINAL RESULT
    # ==========================================

    print("\n" + "=" * 65)

    if not failures:

        print("ALL BUSINESS RULE CHECKS PASSED")
        print("=" * 65)

    else:

        print("BUSINESS RULE VALIDATION FAILED")
        print("-" * 65)

        for name, count in failures:
            print(
                f"{name}: {count} violations"
            )

        print("=" * 65)


if __name__ == "__main__":
    validate_business_rules()