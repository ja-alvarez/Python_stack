class User:
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.account = BankAccount(name=name, int_rate=0.02, balance=0)

class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.username = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")
            self.balance -= 5
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            self.balance = self.balance
        return self

    def display_account_info(self):
        print("User:", self.username, ",", "Balance: $", self.balance)
        return self  # account_number* to be added if we include several bank accounts

    def transfer_money (self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.balance +=amount
            print("This transaction was successfully completed.")
        else:
            print("Rejected transaction! Insufficient funds.")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
michael = User("Michael Choi", "michael@python.com")

#accounts info: balance = 0
guido.account.display_account_info()
monty.account.display_account_info()
michael.account.display_account_info()

guido.account.deposit(100).withdraw(50).yield_interest().display_account_info()
#guido's current balance = 51.
guido.account.transfer_money(monty.account,60).display_account_info() #rejected, not enough money.
guido.account.transfer_money(monty.account,50).display_account_info() #Approved, $50 added to Monty's account
monty.account.display_account_info()