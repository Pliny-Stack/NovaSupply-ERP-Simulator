from generators.transactions.purchase_order_generator import PurchaseOrderGenerator


def main():

    print("Generating Purchase Orders...")

    generator = PurchaseOrderGenerator()

    purchase_orders = generator.generate()

    print(purchase_orders.head())

    print()

    print(purchase_orders.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Rows:", len(purchase_orders))

    print(
        "Duplicate Purchase Order Keys:",
        purchase_orders["PurchaseOrderKey"].duplicated().sum()
    )

    print(
        "Duplicate Purchase Order IDs:",
        purchase_orders["PurchaseOrderID"].duplicated().sum()
    )

    print("\nMissing Values:")
    print(purchase_orders.isnull().sum())
    return purchase_orders


if __name__ == "__main__":
    purchase_orders = main()

    purchase_orders.to_csv(
        "output/bronze/FactPurchaseOrder.csv",
        index=False
    )

    print("✅ FactPurchaseOrder exported successfully!")