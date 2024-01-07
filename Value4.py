#Object Oriented Programming.
#A Programme of chaking perfect number .
# A number given from user and find addition of factors of this number. and chake this number
# is perfect or not.
# also create a new function name as CheckPrime to chake given number is Prime or not.
# in this programme use different or another form of of checkPrime function.


class Value:    #creating a class named as value.

    def __init__(self, Data):
        self.No = Data  # instance variable

    def SumFactors(self):
        Sum = 0

        for i in range(1, int((self.No / 2) + 1)):
            if (self.No % i == 0):
                Sum = Sum + i

        return Sum

    def CheckPerfect(self): # instance method
        Ans = self.SumFactors()

        if (self.No == Ans):
            return True
        else:
            return False

    def CheckPrime(self):   #instance method
        i = 0

        for i in range(2, int(self.No / 2) + 1):
            if (self.No % i == 0):
                break

        if (i == int(self.No / 2)):
            return True
        else:
            return False


def main():
    print("Please enter number")
    A = int(input())

    obj = Value(A)  # creating a object of class value

    Ret = obj.CheckPerfect()
    if (Ret == True):
        print("{} is a perfect number".format(A))
    else:
        print("{} is not a perfect number".format(A))

    Ret = obj.CheckPrime()
    if (Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))


if __name__ == "__main__":
    main()