class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)

        
acc1 = Account("111", "abc")

print(acc1.acc_no)
print(acc1.reset_pass())


#Private Attr
class Person:
    __name = "Harsh"
    
    def __hello(self):
        print("Hello Person")
        
    def welcome(self):
        self.__hello()
        
p1 = Person()
print(p1.welcome())


class Car:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car started!")
    
    @staticmethod
    def stop():
        print("Car stopped!")
        
class BMWCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = BMWCar("M5", "Hybrid")
print(car1.type)


#Practice
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
         
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 99, 97)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


   
