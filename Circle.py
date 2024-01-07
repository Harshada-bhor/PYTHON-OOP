## Object Oriented Programming
## A Programme which contains one class named as Circle.
## Demo class contains one class variable as PI which is initialise to 3.14 .
## That class contains three instance variables as Radius, Area, Circumference.
## Initialise instance variable as 0.0 in init method .
## there are four instance methods inside class as Accept(), CalculateArea(),
# CalculateCircumference(), Display()
## Accept method will accept value of Radius from User
## CalculateArea() method will calculate area of circle and store it into
# instance variable Area.
## CalculateCircumference() method will calculate circumference of circle and store it
# into instance variable Circumference
## And Display() method will display value of all the instance variables as Radius
#,Area, Circumference.
## After designing the above class call all instance methods by creating multiple objects

class Circle():
    PI = 3.14

    def __init__(self):
        self.Area = 0.0
        self.Radius = 0.0
        self.Circumference = 0.0

    def Accept(self,radius):
      
        self.Radius = radius

    def CalculateArea(self,radius):
        self.Area =  Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self,radius):
        self.Circumference = 2 * Circle.PI * self.Radius

    @classmethod
    def DisplayGivenInformation(cls):
        print("Value of PI is : ", cls.PI)

    def Display(self):
        print("Radius of circle:",self.Radius)
        print("Area of circle:", self.Area)
        print("Circumference of circle:", self.Circumference)


def main():

    obj = Circle()

    obj.DisplayGivenInformation()

    radius = float(input("Enter a value of radius :"))
    
    obj.Accept(radius)
    obj.CalculateArea(radius)
    obj.CalculateCircumference(radius)
    obj.Display()

if __name__ == "__main__":
    main()