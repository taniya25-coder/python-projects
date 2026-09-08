import json
import os

FILE_NAME = "hotel_manage.json"


def load_data():
    
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data 
    except (json.JSONDecodeError, OSError):
        return {}


def save_data(data):
    """Persist records as readable JSON."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    data = load_data()
    while True:
        print("===Hotel Management===")
        print("1.Booking")
        print("2.Price")
        print("3.Services")
        print("4.Checkout")
        print("5.exit")

        choice = input("enter choice: ")
        if choice == "1":
            name = input("enter name: ")
            days = int(input("enter how much days will you stay: "))
            members = int(input("enter how much members do you have: "))
            if True:  # replace with actual room availability check
                print("Room is booked")
            else:
                print("Room is not available")
    

        elif choice == "2":
            print("Price")
            print("Single room =Rs1500/night")
            print("Double room =Rs3000/night")
            print("Luxury room =Rs5000/night")

        elif choice == "3":
            print("Services")
            print("1.Food & Snacks - Rs800")
            print("2.Laundary & Dry cleaning - Rs300")
            print("3.Spa and wellness center - Rs1000")
            print("4.Airport & Cab - Rs1800")

            service = input("enter which service do you want: ")
            print("Service is added successfully")

        elif choice == "4":
            print("Checkout")
            name = input("enter name: ")
            print(f"Thank you {name}, checkout complete.")

        elif choice == "5":
            print("Exiting...")
            return

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
