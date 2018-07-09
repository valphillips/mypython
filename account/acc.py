

class Account:
    """This class creates generic account objects"""
    def __init__(self, filepath):  ##The constructor method
        self.filenm=filepath #Instance variable - shared by the object instance
        with open(filepath, 'r') as file:
            self.balance=int(file.read())  

    def withdraw(self, amount):
        self.balance=self.balance - amount 

    def deposit(self, amount):  #Class method
       self.balance=self.balance + amount 

    def commit(self): 
        with open(self.filenm, 'w') as file:
            file.write(str(self.balance))
            print("save self.balance")


class Cheque(Account):  #Create Cheque as a subclass of Account  (Inheretance)
    """This class generates cheque account objects """
    type="checking_acc"  #Class variable - available to all instances of the class
    
    def __init__(self, filenm, fee):
        Account.__init__(self, filenm)  # call the init function of the Account class to create minimal object
        self.fee=fee #instance variable - shared by the object instance

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

transfer_amount=110

#Instantiate the class
jacks_cheque=Cheque(r"C://Users//vmp2303//Dropbox//Val_Work//Python//Training//demo//account//jack_balance.txt",1)
print(jacks_cheque.balance)
jacks_cheque.transfer(transfer_amount)
print("Cheque Account balance after transferring %s = %s" % (transfer_amount, jacks_cheque.balance)
)
jacks_cheque.commit()
print(jacks_cheque.type)


johns_cheque=Cheque(r"C://Users//vmp2303//Dropbox//Val_Work//Python//Training//demo//account//john_balance.txt",1)
print(johns_cheque.balance)
johns_cheque.transfer(transfer_amount)
print("Cheque Account balance after transferring %s = %s" % (transfer_amount, johns_cheque.balance)
)
johns_cheque.commit()
print(johns_cheque.type)

print(johns_cheque.__doc__)  #Print the docstring defined for this class
account=Account("balance.txt")
print(account.__doc__)
