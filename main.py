from generators.master.customer_generator import CustomerGenerator


def main():

    print("Generating Customer Dimension...")

    generator = CustomerGenerator()

    customers = generator.generate()

    customers.to_csv(
        "output/bronze/DimCustomer.csv",
        index=False
    )

    print("✅ Customer Dimension exported successfully!")

    print("\nSample Data")
    print(customers.head())

    print("\nDataset Information")
    print(customers.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Rows:", len(customers))

    print(
        "Duplicate Customer IDs:",
        customers["CustomerID"].duplicated().sum()
    )

    print(
        "Duplicate Customer Keys:",
        customers["CustomerKey"].duplicated().sum()
    )

    print("\nMissing Values")
    print(customers.isnull().sum())


if __name__ == "__main__":
    main()


    from generators.master.warehouse_generator import WarehouseGenerator


def main():

    print("Generating Warehouse Dimension...")

    generator = WarehouseGenerator()

    warehouses = generator.generate()

    print(warehouses.head())

    print(warehouses.info())


if __name__ == "__main__":
    main()