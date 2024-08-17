#------------------private methods and attributes--------------------------

# class person:
#     __name="anonymous"      #--->private attribute
    
#     def __hello(self):      #--->private methods
#         print("Hello person")

#     def welcome(self):
#         self.__hello()

# p1=person()
# p1.welcome()
#---------------------------------------------------------------------------



#------------------------Inheritance----------------------------------
#multi-level inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car started....")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand

# class fortuner(toyotacar):
#     def __init__(self,type):
#         self.type=type

# car1=fortuner("diseal")
# car1.start()

#-----------------------

# #multiple inheritance
# class A:
#     varA=print("welcome to class A")

# class B:
#     varB=print("Welcome to class B")

# class C (A,B):
#     varC=print("Welcome to class C")

# c1=C()
# c1.varA()
# c1.varB()
# c1.varC()

#----------------------------------------------------------------------



#----------static method----------------------------------
# class car:
#     def __init__(self,type):
#         self.type=type


#     @staticmethod
#     def start():
#         print("car started....")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self,name,type):
#         self.name=name
#         super.__init__(type)


#----------------------------------------------------------------------


# #--------------------class method---------------------------
# class Person:

#     name="Anonymous"

#     def changeName(self,name):
#         self.__class__="Rahul"
#         self.name=name
#         #person.name="Rahul"

# p1=Person()
# p1.changeName("Rahul kumar")
# print(Person.name)
# print(p1.name)

# --------------------------
# class Person:

#     name="Anonymous"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=Person()
# p1.changeName("Rahul kumar")
# print(Person.name)
# print(p1.name)


#--------------------------------------------------------------

#------------------Property method----------------------------
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         self.percentage=str((self.phy+self.maths+self.chem)/3) +" %"


#     def calcPercentage(self):
#         self.percentage=str((self.phy+self.maths+self.chem)/3) +" %"

# stu1= student(98,99,23)
# print(stu1.percentage)

# stu1.phy=78
# #here even if we change the marks percentage is still the same
# #we need to call calcPercentage()
# print(stu1.percentage)

#--------------
# #better way

# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths

#     @property
#     def calcPercentage(self):
#         return str((self.phy+self.maths+self.chem)/3) +" %"

# stu1= student(98,99,23)
# print(stu1.percentage)

# stu1.phy=78
# #here even if we change the marks percentage is still the same
# #we need to call calcPercentage()
# print(stu1.percentage)

#------------------------------------------------------------------


#-------------------POLYMORPHISM-------------------------

#----------------Operator_Overloading----------
"""creating a class to do operations complex numbers (via operator overloading)"""

# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     # # without operator overloading--------
#     # def add(self,num2):
#     #     newReal=self.real+num2.real
#     #     newImg=self.img+num2.img
#     #     return complex(newReal,newImg)



#     #with operator overloading(and dunder function)
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return complex(newReal,newImg)
    
#     def __sub__(self,num2):
#         newReal=self.real-num2.real
#         newImg=self.img-num2.img
#         return complex(newReal,newImg)


# num1 = complex(3,7)
# num2 = complex(1,4)

# # num3=num1.add(num2)
# num3=num1+num2
# num4=num1-num2
# num3.showNumber()
# num4.showNumber()


#----------------------------------------------------------------

#--------------Questions------------------------------------

"""
Define a circle class to create a circle of radius r using the constructor
Define Area() method of the class to calculate area
Define Perimeter() method of the class
"""
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# circle1=Circle(21)
# print(circle1.perimeter())

"""
Define a Employee class with attributes role,department & salary.
This class also a showdetail() method

Create an Engineer class that inherits properties from Employee
and has additional attributes name and age.
"""

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showdetail(self):
#         print("role: ",self.role)
#         print("department", self.department)
#         print("salary: ",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer","IT","1,00,000")

# em1=Employee("Doctor","dentist",50000)
# em1.showdetail()
# engineer1=Engineer("Anubhav",23)
# engineer1.showdetail()

"""
create a class called Order which stores item&price
Use dunder function __gt()__[greater than] to convey that:
order1>order2(if price of order 1>order 2)
"""
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price>order2.price

         
odr1=Order("Chips",30)
odr2=Order("tea",10)

print( odr1 > odr2)