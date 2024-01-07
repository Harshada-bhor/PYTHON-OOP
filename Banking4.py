# Object Oriented Programming,
# Programme of Banking Application.
# create a class named as Bank_Account.
# in these class define two class variable and one init method like constructor and
# instance methods.
# under init method there are instance variable and instance methods are Creating and
# display bank account information.
# also define one class method which display Bank information.
# also define one static method which display KYC information.
# define two instance method deposit and withdraw deposit will be credit amount to a
# bank account and deposit will be debit amount from bank account.


# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name ,ROI_On_FD
# Class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------- Your Account informartion is as below --------")
        print("Name of Account Holder : ", self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ", self.Address)
        print("Current Amount in account : ", self.Amount)

    @classmethod    #decorator of class method
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ", cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ", cls.ROI_On_FD)

    @staticmethod   # decorator of static method
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Goverment of India you have to submit below documnets")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")

    def Deposit(self, value):
        self.Amount = self.Amount + value

    def Withdraw(self, value):
        self.Amount = self.Amount - value


def main():
    Bank_Account.DisplayKYCInfo()   #call of static method

    print("Name of bank : ", Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed deposit : ", Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInformation()   #call of class method

    User1 = Bank_Account()  #creating 1st object of class Bank_Account
    User2 = Bank_Account()  #creating 2nd object of class Bank_Account

    print("Createing the first account")
    User1.CreateAccount()

    print("Createing the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(500)
    User2.Deposit(1200)

    print("Amount of {} after deposit is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after deposit is {}: ".format(User2.Name, User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)

    print("Amount of {} after withdraw is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after withdraw is {}: ".format(User2.Name, User2.Amount))


if __name__ == "__main__":
    main()

    
    
