# College Management System

students = []

while True:
    print("===COLLEGE MANAGEMENT===")
    print("1. Add Student")
    print("2. Course")
    print("3. Fees")
    print("4. View Student")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        name = input("Enter Student Name: ")
        student = {"name": name, "course": "Not Added", "fees": "Not Added"}
        students.append(student)
        print("Student added successfully!")
        

    elif choice == '2':
        if len(students) == 0:
            print("Add student")
        else:
            print("\n--- Student List ---")
            c = 1
            for s in students:
                print(f"{s['name']} | Course: {s['course']}")
                c = c + 1
            
            num = int(input("Kiske liye course dalna hai (Student number): "))
            if 1 <= num <= len(students):
                course_name = input("Enter Course Name (e.g., BCA): ")
                students[num - 1]["course"] = course_name
                print("✅ Course updated successfully!")
            else:
                print("❌ Invalid number!")
                
    # 3. FEES
    elif choice == '3':
        if len(students) == 0:
            print("❌ Pehle student add karein!")
        else:
            print("\n--- Student List ---")
            c = 1
            for s in students:
                print(c, ". Name:", s["name"], "| Fees:", s["fees"])
                c = c + 1
            
            num = int(input("Kiske liye fees dalni hai (Student number): "))
            if 1 <= num <= len(students):
                fee_amt = input("Enter Fee Amount: ")
                students[num - 1]["fees"] = fee_amt
                print("✅ Fees updated successfully!")
            else:
                print("❌ Invalid number!")

    # 4. VIEW STUDENT
    elif choice == '4':
        print("\n--- All Students Details ---")
        print("Total Students:", len(students))
        
        if len(students) == 0:
            print("No students found.")
        else:
            c = 1
            for s in students:
                print(c, ". Name:", s["name"], "| Course:", s["course"], "| Fees:", s["fees"])
                c = c + 1

    # 5. EXIT
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
        
    else:
        print("❌ Invalid choice! Enter between 1 to 5.")