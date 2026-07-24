from generators.master.product_generator import ProductGenerator


def main():

    print("Generating Product Dimension...")

    generator = ProductGenerator()

    products = generator.generate()

    products.to_csv(
        "output/bronze/DimProduct.csv",
        index=False
    )

    print("✅ DimProduct exported successfully!")

    print(products.head())

    print(products.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Duplicate Product IDs:",
          products["ProductID"].duplicated().sum())

    print("Duplicate Product Keys:",
          products["ProductKey"].duplicated().sum())

    print("\nMissing Values:")
    print(products.isnull().sum())

    print("\nRows:", len(products))


if __name__ == "__main__":
    main()

    