from generators.transactions.shipment_generator import ShipmentGenerator


def main():

    print("Generating Shipments...")

    generator = ShipmentGenerator()

    shipments = generator.generate()

    print(shipments.head())

    print("\nRows:", len(shipments))

    print("\nColumns:")
    print(shipments.columns.tolist())

    print("\nValidation Results")
    print("-" * 40)

    print(
        "Duplicate Shipment Keys:",
        shipments["ShipmentKey"].duplicated().sum()
    )

    print(
        "Duplicate Shipment IDs:",
        shipments["ShipmentID"].duplicated().sum()
    )

    print("\nMissing Values:")
    print(shipments.isnull().sum())

    print("\nQuantity Validation:")
    print(
        "Invalid quantities:",
        (shipments["QuantityShipped"] <= 0).sum()
    )

    print("\nShipping Cost Validation:")
    print(
        "Invalid shipping costs:",
        (shipments["ShippingCost"] <= 0).sum()
    )

    delivered = shipments[
        shipments["ActualDeliveryDate"].notna()
    ]

    print(
        "Actual delivery before shipment:",
        (
            delivered["ActualDeliveryDate"]
            < delivered["ShipmentDate"]
        ).sum()
    )

    shipments.to_csv(
    "output/bronze/FactShipment.csv",
    index=False
)

print("✅ FactShipment exported successfully!")


if __name__ == "__main__":
    main()


