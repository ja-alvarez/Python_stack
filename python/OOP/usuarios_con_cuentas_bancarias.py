class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
            self.balance -= 5
        return self

    def display_account_info(self):
        #print("BankAccount:",",", "Balance: $", self.balance)
        print("User: ", ", ", "Balance: $", self.balance) #from user
#como puedo imprimir el nombre de usuario
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance * self.int_rate
        else:
            self.balance = self.balance
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance (self):
        self.account.display_account_info()

    def transfer_money (self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

#print nombre usuario / cuenta

#Permite al usuario tener varias cuentas; actualiza los metodos para que el usuario pueda especificar
# de cual cuenta ellos quieren depositar o retirar

guido = User("Guido van Rossum")  # instancia de objeto
monty = User("Monty Python")
michael = User("Michael Choi")

guido.display_user_balance()
monty.display_user_balance()
michael.display_user_balance()
guido.make_withdrawal(100)
guido.display_user_balance()
guido.make_deposit(100)
guido.display_user_balance()
monty.make_deposit(11)
monty.display_user_balance()
michael.make_deposit(70)
michael.make_withdrawal(35)
michael.display_user_balance()
print("*"*80)




