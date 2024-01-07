## Object Oriented Programming
## A Programme which contains one class named as Bookstore.
## Demo class contains one class variable as NoOfBooks which is initialise with 0.
## Demo class contains two instance variable as Name,Author.
## there is one instance methods of class as Display which displays name,Author and
# no of Books.
## Initialise instance variable in init method by accepting the values from user as name
# and author.


class Bookstore():
    NoOfBooks = 0

    def __init__(self,a,b):

        self.Name = a
        self.Auther = b

        Bookstore.NoOfBooks += 1

    def Display(self):
         print(self.Name, "by" , self.Auther , "No Of Books is ",Bookstore.NoOfBooks )

def main():
    obj1= Bookstore("Lenux system programming","Robert love.")
    obj1.Display()
    obj2= Bookstore("C programming" , "Dennis Ritchie.")
    obj2.Display()

if __name__ == "__main__":
    main()