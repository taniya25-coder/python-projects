import json
import os

FILE_NAME = "bank_data.json"

def load_data():
  if not os.path.exists(FILE_NAME):
    return {}
  try:
    with open(FILE_NAME, "r") as f:
      return json.load(f)
  except json.JSONDecodeError:
    return {}

def save_data(data):
  with open(FILE_NAME, "w") as f:
    json.dump(data, f, indent=4)

def main():
  data = load_data()
  while True:
    print("\n===Bank Management System===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    #1. Create Account
    if choice == "1":
      acc_no = input("Enter account number: ")
      if acc_no in data:
        print("Account already exists")
      else:
        name = input("Enter name")
        balance = float(input("Enter initial balance: "))
        data[acc_no] = {"name": name, "balance": balance}
        save_data(data)
        print("Account created successfully")

#2 . Deposit Money
    elif choice == "2":
      acc_no = input("Enter account number: ")
      if acc_no in data:
        amt = float(input("Enter amount to deposit: "))
        if amt > 0:
          data[acc_no]["balance"] += amt
          save_data(data)
          print("Amount deposited successfully")
        else:
          print("Amount must be greater than zero")
      else:
        print("Account does not exist")
    

#3. Withdraw Money
    elif choice == "3":
      acc_no = input("Enter account number: ")
      if acc_no in data:
        amt = float(input("Enter amount to withdraw: "))
        if amt <= 0:
          print("Amount must be greater than zero")
        elif data[acc_no]["balance"] >= amt:
          data[acc_no]["balance"] -= amt
          save_data(data)
          print("Amount withdrawn successfully")
        else:
          print("Insufficient balance")
      else:
        print("Account does not exist")
      

#4. Check Balance
    elif choice == "4":
        acc_no = input("Enter account number: ")
        if acc_no in data:
            print(f"Account Balance: {data[acc_no]['balance']}")
        else:
            print("Account does not exist")

#5. Exit
    elif choice == "5":
        print("Exiting...")
        break
if __name__ == "__main__":  #agr m program ko direct run kru to ye main() function ko call krde
  main()