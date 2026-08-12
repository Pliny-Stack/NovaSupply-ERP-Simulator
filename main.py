from generators.transactions.return_generator import ReturnGenerator


def main():

    print("Generating Returns...")

    generator = ReturnGenerator()

    returns = generator.generate()

    print(returns.head())

    print("\nRows:", len(returns))

    print("\nColumns:")
    print(returns.columns.tolist())

    returns.to_csv(
    "output/bronze/FactReturns.csv",
    index=False
)

print("✅ FactReturns exported successfully!")


if __name__ == "__main__":
    main()


