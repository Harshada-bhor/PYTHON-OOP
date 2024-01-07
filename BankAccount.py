## Object Oriented Programming
## A Programme which contains one class named as Bank_Account.
## Demo class contains one class variable as ROI which is initialise to 10.5 
## That class contains two instance variables as Name and Amount.
## Inside init method initialise all name and amount variables by accepting the 
# values from user .
## there are four instance methods inside class as Display(), Deposit(),
# Withdraw(), Calculateinterest()
## Deposit() method will accept amount from User and add that amount in class instance
# variable Amount.
## Withdraw() will accept amount to be withdrawn from User and substract that amount
# from class instance variable Amount.
## Calculateinterest() method calculate the interest based on Amount by considering
# rate of interest which is Class variable as ROI.
## and Display method will display value of all the instance variables as 
# Name and Amount.
## After designing the above class call all instance methods by creating multiple objects


class Bank_Account:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def DisplayAccountInfo(self):
        print("-------- Your Account informartion is as below --------")
        print(" Enter Name of Account Holder : ")
        self.Name = input()
        print("Enter initial Amount in account : ")
        self.Amount = int(input())

    def Deposit(self):
        print("Enter a amount you have to deposit")
        value = int(input())
        self.Amount = self.Amount + value

    def Withdraw(self):
        print("Enter a amount you have to withdraw")
        value = int(input())
        self.Amount = self.Amount - value

    def Calculatedinterest(self):
        Interest = self.Amount * Bank_Account.ROI / 100
        print("Interest based on amount :", Interest)

def main():

    print("Rate of Intrest on Fixed deposit : ", Bank_Account.ROI)
    obj = Bank_Account()
    obj.DisplayAccountInfo()

    obj.Deposit()
    print("Amount of {} after deposit is {}: ".format(obj.Name, obj.Amount))

    obj.Withdraw()
    print("Amount of {} after withdraw is {}: ".format(obj.Name, obj.Amount))

    obj.Calculatedinterest()

if __name__ == "__main__":
    main()

    
    
