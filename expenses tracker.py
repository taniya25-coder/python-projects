#Expenses Tracker
expenses = []
print("Welcome to expense tracker")
while True:
    print("---list---")
    print("1. Add expenses")
    print("2. View expense")
    print("3. Total money spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add expense
    if choice == "1":
        date = input("On which date you spend money")
        Thing = input("On which thing you spend money")
        Amount = input("Enter the amount")
        expenses.append({
            "date": date,
            "Thing": Thing,
            "Amount": Amount
        })
        print("Expenses added succesfully")
        
        #View expense
    elif choice=="2":
        if len(expenses)==0:
            print("No expenses added")
        else:
            print("your all expense")
            count = 1
            for expense in expenses:
                print(f"{count} -> {expense['date']}, {expense['Thing']}, {expense['Amount']}")
                count += 1
     #Total money spending
    elif choice=="3":
        total = 0
        for expense in expenses:
            total += int(expense["Amount"])
        print(f"Total spending money: {total}")
    elif choice=="4":
        print("Thank you")
        break
    else:
        print("Invalid statement")




    
    
