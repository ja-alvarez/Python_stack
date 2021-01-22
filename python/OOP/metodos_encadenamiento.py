class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print("User: ", self.name, ", ", "Balance: $", self.account_balance)
        return self

    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance +=amount
        return self

guido = User("Guido van Rossum") #instancia de objeto
monty = User("Monty Python")
michael = User("Michael Choi")

guido.make_deposit(150).make_deposit(50).make_deposit(300).make_withdrawal(450).display_user_balance()
monty.make_deposit(300).make_deposit(100).make_withdrawal(100).make_withdrawal(150).display_user_balance()
michael.make_deposit(400).make_withdrawal(100).make_withdrawal(70).make_withdrawal(200).display_user_balance()

guido.transfer_money(michael,50).display_user_balance()
michael.display_user_balance()