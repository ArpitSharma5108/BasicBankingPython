import json
import os

DATA_FILE = "bank_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_account(data):
    username = input("Enter new username: ")
    if username in data:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    data[username] = {'password': password, 'balance': 0}
    print(f"Account for {username} created successfully!")

def login(data):
    username = input("Username: ")
    password = input("Password: ")
    if username in data and data[username]['password'] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username or password.")
        return None

def deposit(data, username):
    amount = float(input("Enter amount to deposit: "))
    data[username]['balance'] += amount
    print(f"${amount} deposited. New balance: ${data[username]['balance']}")

def withdraw(data, username):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= data[username]['balance']:
        data[username]['balance'] -= amount
        print(f"${amount} withdrawn. New balance: ${data[username]['balance']}")
    else:
        print("Insufficient balance.")

def check_balance(data, username):
    print(f"Current balance: ${data[username]['balance']}")

def main():
    data = load_data()
    logged_in_user = None

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Logout")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            create_account(data)
        elif choice == '2':
            logged_in_user = login(data)
        elif choice == '3':
            if logged_in_user:
                deposit(data, logged_in_user)
            else:
                print("Please login first.")
        elif choice == '4':
            if logged_in_user:
                withdraw(data, logged_in_user)
            else:
                print("Please login first.")
        elif choice == '5':
            if logged_in_user:
                check_balance(data, logged_in_user)
            else:
                print("Please login first.")
        elif choice == '6':
            logged_in_user = None
            print("Logged out.")
        elif choice == '7':
            save_data(data)
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()