## Object Oriented Programming
## A Programme which contains one class named as Arithmatic.
## That class contains two instance variables as value1 and value2.
## Initialise instance variable as 0.0 in init method .
## there are five instance methods inside class as Accept(), Addition(),
# Substraction(), multiplication(),Division()
## Accept method will accept value of value1 and value2 from User
## Addition() method will perform addition of value1 and value2 and return result.
## substraction() method will perform substraction of value1 and value2 and return result.
## multiplication() method will perform multiplication of value1 and value2 and return result.
## division() method will perform division of value1 and value2 and return result.
## After designing the above class call all instance methods by creating multiple objects


class Arithmatic():

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        print("Enter a first value")
        self.value1 = int(input())
        print("Enter a second value")
        self.value2 = int(input())

    def Addition(self):
        Addition = self.value1 + self.value2
        return Addition

    def Substraction(self):
        Substraction = self.value1 - self.value2
        return Substraction

    def Multiplication(self):
        Multiplication = self.value1 * self.value2
        return Multiplication

    def Division(self):
        Division = self.value1 / self.value2
        return Division

def main():
    obj = Arithmatic()
    obj.Accept()
    Output = obj.Addition()
    print("Addition is :",Output)

    Output = obj.Substraction()
    print("Substraction is :", Output)

    Output = obj.Multiplication()
    print("Multiplication is :", Output)

    Output = obj.Division()
    print("Division is :", Output)

if __name__ == "__main__":
    main()