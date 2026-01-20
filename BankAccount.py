class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Error: Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

    def transfer(self, recipient_account, amount):
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Error: Insufficient funds for transfer.")
            return
        self.withdraw(amount)
        recipient_account.deposit(amount)
        print(f"Transfer of ${amount:.2f} successful.")


def create_account(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Error: Account number already exists.")
        return
    initial_balance = float(input("Enter initial deposit amount: $"))
    if initial_balance < 0:
        print("Error: Initial deposit amount must be non-negative.")
        return
    accounts[account_number] = BankAccount(account_number, initial_balance)
    print("Account created successfully.")


def deposit_money(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    amount = float(input("Enter deposit amount: $"))
    accounts[account_number].deposit(amount)


def withdraw_money(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    amount = float(input("Enter withdrawal amount: $"))
    accounts[account_number].withdraw(amount)


def check_balance(accounts):
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    accounts[account_number].check_balance()


def transfer_money(accounts):
    sender_account_number = input("Enter sender account number: ")
    if sender_account_number not in accounts:
        print("Error: Sender account does not exist.")
        return
    recipient_account_number = input("Enter recipient account number: ")
    if recipient_account_number not in accounts:
        print("Error: Recipient account does not exist.")
        return
    amount = float(input("Enter transfer amount: $"))
    accounts[sender_account_number].transfer(accounts[recipient_account_number], amount)


def main():
    accounts = {}

    while True:
        print("\nMenu:")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check account balance")
        print("5. Transfer money between accounts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            transfer_money(accounts)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
