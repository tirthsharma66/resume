class BankAccount:

    # Constructor
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    # Check balance
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    # Display account details
    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")


# Main Program
print("===== Welcome to Bank Management System =====")

name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")

# Create object
account = BankAccount(name, acc_no)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        account.display_details()

    elif choice == '5':
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice! Please try again.")