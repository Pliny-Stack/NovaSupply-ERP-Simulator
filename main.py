from generators.master.employee_generator import EmployeeGenerator


def main():

    print("Generating Employee Dimension...")

    generator = EmployeeGenerator()

    employees = generator.generate()

    print(employees.head())

    print()

    print(employees.info())

    print("\nValidation Results")
    print("-" * 40)

    print("Rows:", len(employees))

    print(
        "Duplicate Employee Keys:",
        employees["EmployeeKey"].duplicated().sum()
    )

    print(
        "Duplicate Employee IDs:",
        employees["EmployeeID"].duplicated().sum()
    )

    print("\nMissing Values:")
    print(employees.isnull().sum())

    employees.to_csv(
    "output/bronze/DimEmployee.csv",
    index=False
)

print("✅ DimEmployee exported successfully!")


if __name__ == "__main__":
    main()

