## Object Oriented Programming
## A Programme which contains one class named as Numbers.
## That class contains one instance variables as value.
## Initialise instance variable as 0.0 in init method .
## there are four instance methods inside class as ChkPrime(), ChkPerfect(),
# Sumfactors(), factors()
## ChkPrime() method will returns true if number is prime otherwise returns false
## ChkPerfect() method will returns true if number is perfect otherwise returns false
## Sumfactors() method will return addition of all factors. Use this method in any
# another method as a helper method if required.
## factors() method will display all factors of instance variable
## After designing the above class call all instance methods by creating multiple objects



class Numbers:

    def __init__(self, A):
        self.value = A

    def Factors(self):
        print("factors are : ")
        for i in range(1, self.value, 1):
            if self.value % i == 0:
                print(i)
            i = i + 1

    def SumFactors(self):
        Sum = 0

        for i in range(1, int((self.value / 2) + 1)):
            if (self.value % i == 0):
                Sum = Sum + i
        print("sum of factors",Sum)

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if (self.value == Ans):
            return True
        else:
            return False

    def CheckPrime(self):
        i = 0
        Flag = True

        for i in range(2, int(self.value / 2) + 1):
            if (self.value % i == 0):
                Flag = False
                break

        return Flag


def main():
    print("Please enter number")
    A = int(input())

    obj = Numbers(A)

    obj.Factors()

    obj.SumFactors()

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