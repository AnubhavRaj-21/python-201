# class student:
#     name="karan"

# s1=student()
# print(s1.name)
#-------------------------------------------------------------------------------
# #creating a constructor(__init__())

# class student:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#     name="karan"

# s1=student("karan",12)
# s2=student("arjun",78)



#-----------------------------------------------------------------


# #class and instance attributes

# class student:
#     college_name="Heritage" #---->class attributes
#     def __init__(self,fullname,marks):
#         self.name=fullname  #---->object(instance attributes)
#         self.marks=marks
#     name="karan"

# #if obj and class attributes is same then obj attributes>class attributes
# s1=student("karan",12)
# s2=student("arjun",78)

#-----------------------------------------------------------------------
#----------------------------Questions----------------------------
#Create a class that takes name&marks of 3 subjects as arguements
#in constructor. Then create a method to print the average.

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"ur avg score is ",sum/3)    

# s1=student("Anubhav",100,14,543)
# s1.average()
#--------------------------------------------------------------------------

# #static method(decorator)
# class student:
#     @staticmethod
#     def hello():
#         print("hello")

# s1=student
# s1.hello()

#----------------------------------------------------------------------------
#Question
#create account class with 2 attributes ->balance&account no.
#also create methods for debit,credit and printing balance

class bank:
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account

    def credit(self,amount):
        self.balance+=amount
        print("credit of $",amount," successful")
        self.balance()

    def debit(self,amount):
        self.balance-=amount
        print("$",amount, "debited")
        self.balance()

    def balance(self):
        print("Ur balance is $",self.balance)

anubhav=bank(120000,33806)
anubhav.credit(400000)        