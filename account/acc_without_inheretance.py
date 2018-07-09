#Attributes of bank account
#Initial state

#The 'account' directory is the package
#The 'acc.py' script is the module
#In acc.py module, 'Account' is the class
# account.acc.Account is the object


class Account:

    def __init__(self, filepath):
        self.filenm=filepath  #Set filepath as an instance parameter so that it can be reused in other methods
        with open(filepath, 'r') as file:
            self.balance=int(file.read())  #balance is defined as an attribute, and value intiialised

    def withdraw(self, amount):
        self.balance=self.balance - amount #Don't update the file yet. Do on the memory param

    def deposit(self, amount):
       self.balance=self.balance + amount #Don't update the file yet. Do on the memory param

    def commit(self): #Commit the new balance to file
        with open(self.filenm, 'w') as file: #Open the file using instance parameter
            file.write(str(self.balance))
            print("save self.balance")
        
account=Account(r"C://Users//vmp2303//Dropbox//Val_Work//Python//Training//demo//account//balance.txt")   #python will automatically also pass the account object to the class
print(account)   #To see the object
print("Account balance = %s" % account.balance)
#withdrawal_amount=100
#account.withdraw(withdrawal_amount)
#print("Balance after withdrawing %s is %s" % (withdrawal_amount, account.balance))
#account.commit()

deposit_amount=400
account.deposit(deposit_amount)
print("Balance after depositing %s is %s" % (deposit_amount, account.balance))
account.commit()
