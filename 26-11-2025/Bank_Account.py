class Bank_Account:
    def __init__(self, CustomerName, AccountNumber, BankName, AccountBalance):
        self.CustomerName = CustomerName
        self.AccountNumber = AccountNumber
        self.BankName = BankName
        self.AccountBalance = AccountBalance

    def display(self):
        print(self.CustomerName)
        print(self.AccountNumber)
        print(self.BankName)

    def deposit(self, amount):
        self.AccountBalance = self.AccountBalance + amount

    def withdraw(self, amount):
        self.AccountBalance = self.AccountBalance - amount

#Creating Bank objects
a1=Bank_Account("John", "IT874654", "HDFC", 50000)
a2=Bank_Account("John", "IT874654", "HDFC", 50000)
#depositing amount
a1.deposit(int(input("Enter amount to deposit:")))
print(a1.AccountBalance)

a2.withdraw(int(input("Enter amount to withdraw:")))
print(a2.AccountBalance)

