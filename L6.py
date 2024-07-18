#-------------------FUNCTIONS-------------------
# def calcSum(a,b):
#     return a+b
 
# def print():
#     print("h")

# def odd_even(n):
#     if n%2==0:
#         return (n,"is evne")
#     else:
#         return (n,"is odd")
    
# print(odd_even(4))




#-------------------RECURSION-------------------
# def show(a):
#     if a==0:
#         return 0
#     show(a-1)
#     print(a)
    
# show(5)


#------------------Question-----------------------
# #Question 1
# #Calculate the sum of first n natural numbers
# def natural(n):
#     if(n==0):
#         return 0
#     return n+natural(n-1)

# print(natural(5))


#Question 2
#print all elements in a list
def printer(a,idex):
    if(idex==len(a)):
        return 
    print(a[idex])
    printer(a,idex+1)


printer([1,2,3,4,5,6,7,8,9],0)