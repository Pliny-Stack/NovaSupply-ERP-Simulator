
from generators.master.supplier_generator import SupplierGenerator


def main():

    print("Generating suppliers...")

    generator = SupplierGenerator()

    suppliers = generator.generate()

    print(suppliers.head())

    suppliers.to_csv(
        "output/bronze/DimSupplier.csv",
        index=False
    )

    print("\nSupplier file exported successfully!")


if __name__ == "__main__":
    main()