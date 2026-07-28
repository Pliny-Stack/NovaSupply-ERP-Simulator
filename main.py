from generators.transactions.inventory_generator import InventoryGenerator


def main():

    print("Generating Inventory...")

    generator = InventoryGenerator()

    inventory = generator.generate()

    inventory.to_csv(
        "output/bronze/FactInventory.csv",
        index=False
    )

    print("✅ FactInventory exported successfully!")

    print(inventory.head())

    print()

    print(inventory.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Rows:", len(inventory))

    print(
        "Duplicate Inventory Keys:",
        inventory["InventoryKey"].duplicated().sum()
    )

    duplicate_pairs = inventory.duplicated(
        subset=["WarehouseKey", "ProductKey"]
    ).sum()

    print(
        "Duplicate Warehouse/Product combinations:",
        duplicate_pairs
    )

    print("\nMissing Values:")

    print(inventory.isnull().sum())


if __name__ == "__main__":
    main()