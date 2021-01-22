class BankAccount:
    def __init__(self, account_number, int_rate):
        self.account_number = account_number
        self.int_rate = int_rate
        self.balance = 0

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
        print("BankAccount number:", self.account_number, ",", "Balance: $", self.balance)
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance * self.int_rate
        else:
            self.balance = self.balance
        return self.balance



cuentauno = BankAccount(1234, 0.01)  # instancia de objeto
cuentados = BankAccount(5678, 0.01)

cuentauno.deposit(100).deposit(200).deposit(300).withdraw(150)
cuentauno.yield_interest()
cuentauno.display_account_info()

cuentados.deposit(400).deposit(500).withdraw(50).withdraw(100).withdraw(150).withdraw(200)
cuentados.yield_interest()
cuentados.display_account_info()