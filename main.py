
from generators.transactions.sales_generator import SalesGenerator


def main():

    print("Generating Sales...")

    generator = SalesGenerator()

    sales = generator.generate()

    print("\nSales Preview")
    print("-" * 40)
    print(sales.head())

    print("\nSales Info")
    print("-" * 40)
    print(sales.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Rows:", len(sales))

    print(
        "Duplicate Sales Keys:",
        sales["SalesKey"].duplicated().sum()
    )

    print(
        "Duplicate Sales IDs:",
        sales["SalesID"].duplicated().sum()
    )

    print("\nMissing Values:")
    print(sales.isnull().sum())

    print("\nRevenue Check:")
    print(
        "Incorrect Revenue:",
        (
            sales["Revenue"].round(2)
            != (sales["QuantitySold"] * sales["UnitPrice"]).round(2)
        ).sum()
    )

    print("\nCost Check:")
    print(
        "Incorrect Cost:",
        (
            sales["Cost"].round(2)
            != (sales["QuantitySold"] * sales["UnitCost"]).round(2)
        ).sum()
    )

    print("\nProfit Check:")
    print(
        "Incorrect Gross Profit:",
        (
            sales["GrossProfit"].round(2)
            != (sales["Revenue"] - sales["Cost"]).round(2)
        ).sum()
    )

    print(sales.head())

    print()

    print(sales.info())
        return sales

if __name__ == "__main__":
    sales = main()

    sales.to_csv(
        "output/bronze/FactSales.csv",
        index=False
    )

    print("✅ FactSales exported successfully!")