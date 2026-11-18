#main opration is done  in this file 
#create an object of current account 
from simpleaccount import SimpleAccount #independent class not a child class
from opps_bank import BankAccount
from current_account import Current_account
from savings_account import SavingAccount
#create an object  of saving account
# SimpleAccount=SimpleAccount()   #
# SimpleAccount.method1()
# ca1= Current_account()  #current accout 1
# ca1.dummymethod()

#not possible ,bcoz we cannot create an object of abstract class
# bankacc1=BankAccount()
# bankacc1.deposite_money()

#create an object  of current account
print('----------current account--------------')
ca1=Current_account(1000)   #
# ca1.dummymethod()
ca1.deposite_money(1000) # child get all the features of pareants
ca1.withdraw_amt(1200)

#cannot be done bcoz the varible is encapsulated by parent class
# print(f'balance amt is{ca1.__account_balance}')

#to display the balance use the fun.from the parent class
#ca1.display_balance()

ca1.deposite_money(1700)
#ca1.display_balance()


print('---------------savings account-----------------')

sa1= SavingAccount(10000)
sa1.calculate_intrests(5)
#sa1.display_balance()
# sa1.deposite_money(2000)
# sa1.withdraw_amt(20000)



