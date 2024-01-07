#Object Oriented Programming.
#A Programme of chaking perfect number .
# A number given from user and find addition of factors of this number. and chake this number
# is perfect or not.
# also create a new function name as CheckPrime to chake given number is Prime or not.
# in this programme use different or another form of of checkPrime function.

class Value:

    def __init__(self, Data):
        self.No = Data

    def SumFactors(self):
        Sum = 0

        for i in range(1, int((self.No / 2) + 1)):
            if (self.No % i == 0):
                Sum = Sum + i

        return Sum

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if (self.No == Ans):
            return True
        else:
            return False

    def CheckPrime(self):
        i = 0
        Flag = True

        for i in range(2, int(self.No / 2) + 1):
            if (self.No % i == 0):
                Flag = False
                break

        return Flag


def main():
    print("Please enter number")
    A = int(input())

    obj = Value(A)

    Ret = obj.CheckPrime()
    if (Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))


if __name__ == "__main__":
    main()