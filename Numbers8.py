# Object Oriented Programming
# this Programme is of accept the number from user and display it on console.
# it contains two functions or method under class Numbers, which is named as
# Accept and display. it has first parameter as self because it is instance method
# and instance methoad have first parameter as self.
# define a new function Summation in class Numbers. the function gives addition of n
# numbers.
# define a new function Avarage in class Numbers. the function gives avarage of n
# numbers.
# define a new function maximum in class Numbers. the function gives maximum number
# among n number.
# define a new function minimum in class Numbers. the function gives minimum number
# among n number.
# moved Accept method call in init method.
# define a two new function named as __ChakePrime and DisplayPrime in class Numbers. the function gives
# prime numbers among n number.
# the __ChakePrime function is a helper function only those function used it which
# are in class numbers.not allowed to call outside of class ,hence it is a hidden function

class Numbers:  # creating a class named as Numbers.
    def __init__(self):
        self.Size = 0  # instance variable
        self.Arr = list()  # instance variable
        self.Accept()

    def Accept(self):  # instance method
        print("Enter how many elements you want : ")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0  # for indicates the value will be integer.
        for i in range(0, self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):  # instance method
        print("Elements from list are : ")
        for i in range(0, self.Size):
            print(self.Arr[i])

    def Summation(self):  # instance method
        Sum = 0
        for i in range(0, self.Size):
            Sum = Sum + self.Arr[i]

        return Sum

    def Average(self):  # instance method
        Sum = 0
        for i in range(0, self.Size):
            Sum = Sum + self.Arr[i]

        return (Sum / self.Size)

    def Maximum(self):  # instance method
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]

        return Max

    def Minimum(self):  # instance method
        Min = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] < Min):
                Min = self.Arr[i]

        return Min

    def __CheckPrime(self, No):   # instance method
        i = 0
        Flag = True

        for i in range(2, int(No / 2) + 1):
            if (No % i == 0):
                Flag = False
                break

        return Flag

    def DisplayPrime(self):   # instance method

        for i in range(0, self.Size):
            if (self.__CheckPrime(self.Arr[i]) == True):
                print("{} is a prime number".format(self.Arr[i]))


def main():

    obj = Numbers()  # creating a object of class Numbers.
    obj.Display()  # call of method

    Output = obj.Summation()  ## call of method
    print("Summation of all elements is : ", Output)

    Output = obj.Average()  # call of method
    print("Average of all elements is : ", Output)

    Output = obj.Maximum()  # call of method
    print("Largest element is : ", Output)

    Output = obj.Minimum()  # call of method
    print("Smallest element is : ", Output)

    obj.DisplayPrime()    # call of method


if __name__ == "__main__":
    main()





    
