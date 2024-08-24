#Class and Object
class Car:
    color = "Grey"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)


#Practice
class Car:
    brand_name = "BMW"
    
    #default constructor 
    # def __init__(self):
    #     pass

    #parametrized constructor 
    def __init__(self, model, color):  
        self.model = model
        self.color = color
    
    def welcome(self):
        print("welcome", self.brand_name)
    
car1  = Car("5 series", "Grey")
print(car1.model, car1.color)
print(Car.brand_name)
car1.welcome()


#Non-Static Methods

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is: ", sum/3)
    
s1 = Student("Harsh", [98, 99, 97])
s1.get_avg()

s1.name = "Tony"
s1.get_avg()


#Static Methods

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod   
    def hello():
        print("Hello")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is: ", sum/3)
    
s1 = Student("Harsh", [98, 99, 97])
s1.get_avg()
s1.hello()

#Practice 1
class Account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no
        
        #Debit Method
    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())
        
        #Credit method    
    def credit(self, amount):
        self.bal += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())
            
        #Final balance
    def get_balance(self):
        return self.bal
           
        
acc1 = Account(10000, 12345)
acc1.debit(8000)
acc1.credit(3500)