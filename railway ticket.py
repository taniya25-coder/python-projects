import json
import os

FILE_NAME = "railway_ticket.json"


def load_data():
    """Load ticket records, returning an empty database if necessary."""
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
        if "tickets" not in data or not isinstance(data["tickets"], list):
            data["tickets"] = []

        print("\n====Railway Tickets===")
        print("1.Booking")
        print("2.View status")
        print("3.Exiting")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Passenger name: ")
            source = input("From: ")
            destination = input("To: ")
            date = input("Travel date: ")

            ticket = {
                "id": len(data["tickets"]) + 1,
                "passenger": name,
                "source": source,
                "to": destination,
                "date": date,
                "status": "Booked",
            }
            data["tickets"].append(ticket)
            save_data(data)
            print(f"Ticket booked successfully. Ticket ID: {ticket['id']}")


        elif choice == "2":
            if not data["tickets"]:
                print("No tickets found.")
                continue
            for ticket in data["tickets"]:
                print(
                    f"ID: {ticket['id']} - {ticket['passenger']} , "
                    f"{ticket['source']} to {ticket['to']} | "
                    f"{ticket['date']} - {ticket['status']}"
                )
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()