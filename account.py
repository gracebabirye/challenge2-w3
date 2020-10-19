import sys

class BankAccount:
    def __init__(self):
        #initialize global variable balance to be accessed by any method in this class
        self.balance = 0

    def get_balance(self):
        if(self.balance == 'closed'):
            raise ValueError('ValueError')
        return self.balance
                
    def open(self):
        self.balance = 0

    def deposit(self, amount=200):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance == 'closed' or self.balance < amount or amount < 0):
            raise ValueError('ValueError')
        self.balance -= amount

    def close(self):
        self.balance = "closed"

bank = BankAccount()
print("Welcome to Our Bank......")
print(bank.get_balance())

print("Enter Deposit Amount")
input1 =  12 #sys.stdin.readline()


bank.deposit(int(input1))
bank.get_balance()
print("Current Balance is:")
print(bank.get_balance())

