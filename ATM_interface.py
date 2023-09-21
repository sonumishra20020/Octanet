class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.transactions = []
        self.users = {'Sonu123': {'pin': '5656', 'balance': 1000},
                      'Mishra99': {'pin': '9876', 'balance': 1000}}  #  users and pin with initiating balance

        self.current_user = None


    #for checking authentication
    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id]['pin'] == pin:
            self.current_user = user_id
            self.balance = self.users[user_id]['balance']
            print(f"Welcome !!, {user_id}! Do Your Transactions.")
            return True
        else:
            print("Invalid user ID or Wrong PIN. Please try again.")
            return False

    #for balance check
    def check_balance(self):
        print(f"Your balance is {self.balance}")


    #for money deposit
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        self.users[self.current_user]['balance'] = self.balance
        print(f"{amount} is deposited in your account. Your new balance is {self.balance}")

    #for money withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn {amount}")
            self.users[self.current_user]['balance'] = self.balance
            print(f"{amount} is withdrawn from your account. Your new balance is {self.balance}")
        else:
            print("Insufficient Balance!!")


    #for money transfer
    def transfer(self, amount, recipient_name):
        self.recipient_name = recipient_name
        if recipient_name and amount <= self.balance:
            confirmation = input(f"Do you want to transfer {amount} to {recipient_name}? (yes/no): ")
            if confirmation.lower() == 'yes':
                self.balance -= amount
                self.transactions.append(f"Transferred {amount} to {recipient_name}")
                print(f"{amount} transferred to {recipient_name}")
            else:
                print("Transfer canceled.")
        elif not recipient:
            print("Recipient not found.")
        else:
            print("Insufficient Balance!!")
    #for showing history
    def transaction_history(self):
        print("\n================== Your Transaction History ================")
        for transaction in self.transactions:
            print(transaction)

    def menu(self):
        while True:
            if self.current_user is None:
                user_id = input("Enter user ID: ")
                pin = input("Enter PIN: ")
                self.authenticate_user(user_id, pin)
                if self.current_user is None:
                    continue

            print("\n==============Please select any option from given menu below =============")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Quit")

            Button = input("Press any button (1/2/3/4/5/6): ")

            if Button == '1':
                self.check_balance()
            elif Button == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif Button == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif Button == '4':
                amount = float(input("Enter amount to transfer: "))
                recipient_name = input("Enter recipient's user ID: ")
                if recipient_name:
                    self.transfer(amount, recipient_name)
                else:
                    print("Recipient not found.")
            elif Button == '5':
                self.transaction_history()
            elif Button == '6':
                print("Thank you for using the ATM. Have a nice day!!!")
                self.current_user = None
                break
            else:
                print("Invalid Option. Please try again.")


# Create an instance of the ATM class
atm = ATM()

# Start the ATM interface
atm.menu()
