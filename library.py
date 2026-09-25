

students = []
books = []

while True:
    print("===College and library management===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Add Book")
    print("5. View Books")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ")

    if choice == '1':
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        section = input("Enter Section: ")

        student = {
            "name": name,
            "course": course,
            "section": section,
            "attendance": "Not Marked"
        }
        students.append(student)
        print("Student added successfully!")

    elif choice == '2':
        print("\n--- Student List ---")
        print("Total Students:", len(students))

        if len(students) == 0:
            print("No students found.")
        else:
            count = 1
            for s in students:
                print(
                    "Name:", s["name"],
                    "Course:", s["course"],
                    "Section:", s["section"],
                    "Attendance:", s["attendance"]
                )
                count += 1

    elif choice == '3':
        print("\n--- Mark Attendance ---")
        if len(students) == 0:
            print("No students available.")

            num = int(input("Enter student number to mark present/absent: "))
            if 1 <= num <= len(students):
                status = input("Enter Status (Present/Absent): ")
                students[num - 1]["attendance"] = status
                print("Attendance marked successfully!")
            else:
                print("Invalid student number.")

    elif choice == '4':
        b_name = input("Enter Book Name: ")
        book = {
            "title": b_name,
            "status": "Available"
        }
        books.append(book)
        print("Book added!")

    elif choice == '5':
        print("\n--- Book List ---")
        if len(books) == 0:
            print("No books found.")


    elif choice == '6':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice")
