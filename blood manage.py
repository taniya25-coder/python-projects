import json
import os

FILE_NAME = "blood_data.json"
BLOOD_TYPES = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")


def read_amount(prompt):
    try:
        amount = int(input(prompt))
        if amount < 0:
            print("Amount cannot be negative.")
            return None
        return amount
    except ValueError:
        print("Please enter a valid whole number.")
        return None


def load_data():
    default_stock = {blood_type: 10 for blood_type in BLOOD_TYPES}
    if not os.path.exists(FILE_NAME):
        save_data(default_stock)
        return default_stock

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
        return {blood_type: int(data.get(blood_type, 0)) for blood_type in BLOOD_TYPES}
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return default_stock


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)





def main():
    data = load_data()
    while True:
        print("\n=== Blood Bank Management System ===")
        print("1. Check Blood Stock")
        print("2. Add Blood Stock")
        print("3. Remove Blood Stock")
        print("4. Search Blood Stock")
        print("5. Low Stock Alert")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nCurrent Blood Stock", data)

        elif choice == "2":
            blood = input("Enter blood type: ")
            if blood not in data:
                print("Invalid blood type")
                continue
            amount = read_amount("Enter amount to add: ")
            if amount is not None:
                data[blood] += amount
                save_data(data)
                print(f"Added successfully: {amount}")

        elif choice == "3":
            blood = input("Enter blood type: ")
            if blood not in data:
                print("Invalid blood type")
                continue
            amount = read_amount("Enter amount to remove: ")
            if amount is not None:
                if amount > data[blood]:
                    print("Not enough stock available.")
                else:
                    data[blood] -= amount
                    save_data(data)
                    print(f"Removed successfully: {amount}")

        elif choice == "4":
            blood = input("Enter blood type: ").strip().upper()
            if blood in data:
                print(f"Stock for {blood}: {data[blood]}")
            else:
                print("Invalid blood type")

        elif choice == "5":
            low_quantity = 5
            low_stock = {
                blood: amount for blood, amount in data.items()
                if amount < low_quantity
            }
            if low_stock:
                for blood, amount in low_stock.items():
                    print(f"Stock for {blood} is low: {amount}")
            else:
                print("No blood type is low on stock.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":  #agr m program ko direct run kru to ye main() function ko call krde 
    main()