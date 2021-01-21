#make_withdrawal (self, cantidad) : haz que este método disminuya el saldo del usuario en la cantidad especificada

#display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el
# terminal
#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150

#BONIFICACIÓN: transfer_money (self, other_user, cantidad) : haz que este método disminuya el saldo del
# usuario en la cantidad y agrega esa cantidad al saldo de otro other_user

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_withdrawal (self, amount):
        self.account_balance -= amount

    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance (self):
        print("User: ", self.name, ", ", "Balance: $", self.account_balance)

    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance +=amount

guido = User("Guido van Rossum") #instancia de objeto
monty = User("Monty Python")
michael = User("Michael Choi")

guido.make_deposit(150)
guido.make_deposit(50)
guido.make_deposit(300)
guido.make_withdrawal(450)
guido.display_user_balance()

monty.make_deposit(300)
monty.make_deposit(100)
monty.make_withdrawal(100)
monty.make_withdrawal(150)
monty.display_user_balance() #ctrl+d

michael.make_deposit(400)
michael.make_withdrawal(100)
michael.make_withdrawal(70)
michael.make_withdrawal(200)
michael.display_user_balance()

guido.transfer_money(michael,50)
guido.display_user_balance() #ctrl+d
michael.display_user_balance()