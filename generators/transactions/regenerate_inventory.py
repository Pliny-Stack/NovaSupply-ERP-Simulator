from generators.transactions.inventory_generator import InventoryGenerator
from config.config import Config


def main():

    print("Regenerating FactInventory...")
    print("-" * 40)

    generator = InventoryGenerator()

    inventory = generator.generate()

    print(f"Rows generated: {len(inventory):,}")

    output_path = (
        f"{Config.OUTPUT_FOLDER}/FactInventory.csv"
    )

    inventory.to_csv(
        output_path,
        index=False
    )

    print(f"Saved to: {output_path}")
    print("FactInventory regeneration complete!")


if __name__ == "__main__":
    main()