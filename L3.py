# #LIST AND TUPLES
# #LIST
# list=[34,23,11,532,24]
# print(list)
# print(type(list))
# list2=["Arjun",34,12.42]
# list2[1]=32     #lists are mutable unlike strings
# print(list2)

#list slicing is same like strings

# #WAP to ask the user the 3 favourite movies and store them in a list

# movies=[]
# mov=input("Enter for 1st movie: ")      #better way movies.append(input("ENter for 1st movie: "))
# movies.append(mov)
# mov=input("Enter for 2nd movie: ")
# movies.append(mov)
# mov=input("Enter for 3rd movie: ")
# movies.append(mov)




# #WAP to check if a list contains a palindrome of elements
# list1=[1,2,1]
# list1_copy=list1.copy()

# if(list1==list1_copy):
#     print("It's a palindrome")
# else:
#     print("Not a palindrome")



#WAP to count no. of students with the "A " grade in a given tuple
grade_tuple=("C","D","A","A")
print(grade_tuple.count("A"))


