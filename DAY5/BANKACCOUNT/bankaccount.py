class BankAccount:
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("INVALID BALANCE AMOUNT")
account=BankAccount(500,"Dinix")
print(account.get_balance())
account.set_balance(600)
print("Total after adding",account.get_balance())
