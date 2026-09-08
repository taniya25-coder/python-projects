import json
import os

FILE_NAME = "school_manage.json"


def load_data():
    """Load the school's records, returning an empty database if necessary."""
    if not os.path.exists(FILE_NAME):
        return {"students": [], "teachers": []}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {"students": [], "teachers": []}
    except (json.JSONDecodeError, OSError):
        return {"students": [], "teachers": []}


def save_data(data):

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)





def list_records(data, category):
    records = data.get(category, [])
    if not records:
        print("No records found.")
        return
    for record in records:
        print(f"{record['id']}: {record['name']}")


def main():
    data = load_data()
    while True:
        print("\n=== School Management ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Teacher")
        print("4. List Teachers")
        print("5. Attendace")
        print("6. Fees")
        print("7. Salary")
        print("8. Check total students and teachers")
        print("9. Check school performace")
        print("10. Activities")
        print("11. exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Add Students")
            record = {data, "students"}
            name = input("Enter student name: ")
            print("Class")
            class_name = input("Enter class name: ")
            print("Added successfully")

        elif choice == "2":
            print("List Students")
            list_records(data, "students")

        elif choice == "3":
            print("Add Teacher")
            record = {data, "teachers"}
            name = input("Enter teacher name: ")
            print("Subject")
            subject = input("Enter subject: ")
            print("Added successfully")

        elif choice == "4":
            print("List Teachers")
            list_records(data, "teachers")

        elif choice == "5":
            print("Attendance")
            student_name = input("Enter student name: ")
            if any(record["name"] == student_name for record in data["students"]):
                print(f"Attendance marked for {student_name}.")
            else:
                print(f"No record found for {student_name}.")

                teacher_name = input("Enter teacher name: ")
                if any(record["name"] == teacher_name for record in data["teachers"]):
                    print(f"Attendance marked for {teacher_name}.")
                else:
                    print(f"No record found for {teacher_name}.")

        elif choice == "6":
                 print("Fees")
                 student_name = input("Enter student name: ")
                 amt= input("Enter amount: ")
                 if any(record["name"] == student_name for record in data["students"]):
                    print(f"Fees recorded for {student_name} = {amt}.")
                 else:
                    print(f"No record found for {student_name}.")

        elif choice == "7":
                print("Salary")
                teacher_name = input("Enter teacher name: ")
                amt= input("Enter amount: ")
                if any(record["name"] == teacher_name for record in data["teachers"]):
                    print(f"Salary recorded for {teacher_name} = {amt}.")
                else:
                    print(f"No record found for {teacher_name}.")

        elif choice == "8":
                 print("Check Records")
                 print("1. Check total students")
                 print("2. Check total teachers")
                 total_students = len(data["students"])
                 total_teachers = len(data["teachers"])
                 print(f"Total Students: {total_students}")
                 print(f"Total Teachers: {total_teachers}")

        elif choice == "9":
                print("Result of school")
                result = input("Enter result: ")
                if result> 80:
                    print("School is performing well")
                elif result> 60:
                    print("School is performing average")
                elif result> 40:
                    print("School is performing below average")
                else:
                    print("School is poorly performing")

        elif choice == "10":
            print("Activities")
            activities = input("Were games and functions celebrated? (yes/no): ")
            if activities == "yes":
                print("School helps to make students thoughtful and creative.")
            else:
                print("No activities were recorded.")

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    if __name__ == "__main__":  #agr m program ko direct run kru to ye main() function ko call krde 
     main()
               
                                    

                                        


