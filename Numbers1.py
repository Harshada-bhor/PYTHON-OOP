# Object Oriented Programming
# this Programme is of accept the number from user and display it on console.
# it contains two functions or method under class Numbers, which is named as
# Accept and display. it has first parameter as self because it is instance method
# and instance methoad have first parameter as self.

class Numbers:  # creating a class named as Numbers.
    def __init__(self):
        self.Size = 0   # instance variable
        self.Arr = list()    # instance variable

    def Accept(self):   # instance method
        print("Enter how many elements you want : ")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0   # for indicates the value will be integer.
        for i in range(0, self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):   # instance method
        print("Elements from list are : ")
        for i in range(0, self.Size):
            print(self.Arr[i])


def main():
    obj = Numbers() # creating a object of class Numbers.
    obj.Accept()    # call of method
    obj.Display()   # call of method


if __name__ == "__main__":
    main()





    
    
