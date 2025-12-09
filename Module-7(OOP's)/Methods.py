''' Question: Create a class called Account 

Declare some class variables (e.g., bank_name,IFSC).

Declare some instance variables (e.g., account_holder, balance).

Implement the following methods:

deposit(amount) → to add money to the account.

withdraw(amount) → to deduct money if sufficient balance exists.

check_balance() → to display the current balance.

class method as display bankname and IFSC'''

class Account:
    bank_name='SBI'
    ifsc='2345678sbi'
    def __init__(self,acc_no,acc_holder_name,bal):
        self.acc_no=acc_no
        self.acc_holder_name=acc_holder_name
        self.bal=bal
    
    def printDetails(self):
        print(self.
    @staticmethod
    def hello():
        print('hello')
a=Account(23456789,'xyz',3000)
a.printDetails()
Account.hello()