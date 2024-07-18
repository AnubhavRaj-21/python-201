# f=open("demo.txt","r")
# data=f.read()
# #data=f.read(5) reads only initial 5 charcters
# print(data)

#with open("sample.txt","r")

# #-----deleting----------
# import os
# #os.remove(filename)

# # # ------------------QUESTIONS--------------------

# #Question 1
# """Create a new file "practice.txt" using python.
# Add the following data to it

# Hi everyone
# we are learning file I/O
# using java
# I love programming in Java
# """

# with open ("question1.txt","w") as f:
#     f.write("Hi everyone\nwe are learing file I/O\nusing Java.\n")
#     f.write("I love programming in Java")


# #Question 2
# """Write a function that replace learning with java with python"""
# with open ("question1.txt","r") as f:
#     data=f.read()

# new_data=data.replace ("Java","Python")
# print(new_data)

# with open ("question1.txt","w") as f:
#         f.write(new_data)



# #Questioon 3
# #Search if the word learing exist in file or not
# word="learing"
# with open ("question1.txt","r") as f:
#     data=f.read()
#     if data.find(word)!=-1:
#         print("Found")
#     else:
#         print("Not found")


#

