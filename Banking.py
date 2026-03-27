class Account:
    
    def __init__(self, email: str, password: str, bal: float = 0.0):
        self.email = email
        self.name = email.split("@")[0]   # username
        self.password = password
        self.balance = bal

    def deposit(self, amt: float):
        if amt > 0:
            self.balance += amt

    def withdraw(self, amt: float) -> bool:
        if 0 < amt <= self.balance:
            self.balance -= amt
            return True
        return False

    def get_balance(self) -> float:
        return self.balance


class Banking:
    def __init__(self):
        self.accounts = {}   # key = username

    # Create account
    def create(self):
        email = input("Enter Email: ")

        username = email.split("@")[0]

        if username in self.accounts:
            print("Username already exists! Try different email.\n")
            return

        print(f"Your username is: {username}")

        password = input("Set your password: ")

        try:
            bal = float(input("Initial Balance: "))
            self.accounts[username] = Account(email, password, bal)
            print("Account created successfully!\n")
        except ValueError:
            print("Invalid balance input.\n")

    # Login using USERNAME
    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        acc = self.accounts.get(username)

        if acc and acc.password == password:
            print(f"Welcome, {username}!\n")
            return acc
        else:
            print("Invalid username or password.\n")
            return None

    def dep(self):
        acc = self.login()
        if acc:
            try:
                amt = float(input("Amount to deposit: "))
                if amt > 0:
                    acc.deposit(amt)
                    print("Deposit successful!\n")
                else:
                    print("Amount must be positive.\n")
            except ValueError:
                print("Invalid amount.\n")

    def wd(self):
        acc = self.login()
        if acc:
            try:
                amt = float(input("Amount to withdraw: "))
                if acc.withdraw(amt):
                    print("Withdrawal successful!\n")
                else:
                    print("Insufficient balance or invalid amount.\n")
            except ValueError:
                print("Invalid amount.\n")

    def bal(self):
        acc = self.login()
        if acc:
            print(f"Current Balance: {acc.get_balance():.2f}\n")

    def run(self):
        menu = {
            "1": self.create,
            "2": self.dep,
            "3": self.wd,
            "4": self.bal,
            "0": exit,
        }

        while True:
            print("Menu:")
            print("1) Create Account")
            print("2) Deposit")
            print("3) Withdraw")
            print("4) Check Balance")
            print("0) Quit")

            choice = input("Enter choice: ")

            action = menu.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.\n")


if __name__ == "__main__":
    app = Banking()
    app.run()