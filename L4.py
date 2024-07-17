# info = {
#     "key": "value",
#     "name": "Anubhav",
#     "learning": "coding",
#     "languages": ["Python","C++","C"],
#     "CP rating": ("Codeforces",1543,"Leetcode","Knight"),
#     "age":1243,
#     "Is_Adult":True,
#     34:349,
#     (34,2131):342
# }

# print(info)
# print(info["name"])
# info["surname"]="raj"

# null_dict={}


# #nested dictionaries
# student= {
#     "name": "Anubhav",
#     "marks": {
#         "chem":90,
#         "maths":100,
#         "physics":97
#     }
# }

# print(student["marks"]["chem"])



# #Dictonaries methods
# student= {
#     "name": "Anubhav",
#     "marks": {
#         "chem":90,
#         "maths":100,
#         "physics":97
#     }
# }
# print(student.keys())
# print(len(student.keys()))
# print(student.items())
# print(student.get("name"))
# student.update({"city": "Kolkata"})



#Note:-when we pass dic["key"] it throws an error while dic.get("key") doesn't ("key" isn't a valid key)


# # sets
# from gc import collect


# nums={1,2,3,3,3,"Hello"}
# print(len(nums))
# print(nums)
# collection=set()    #empty set syntax
# collection.add(1)
# collection.add(2)
# collection.add(4)
# collection.add(7)
# print(collection)
# collection.pop()
# collection.pop()
# print(collection)


# set={1,2,3}
# set2={2,3,4,5}
# print(set.union(set2))
# print(set.intersection(set2))



#-------------------Questions-----------------
# """
# Question1:

# store the following word meanings in a python dictionaries
# table:"a piece of furniture", "list of facts and figures"
# cat:"a small animal"

# """
# dictionaries={
#     "table": ["a piece of furniture"," list of facts"],
#     "cat": "a small animal"
# }


# """
# Question 2:

# U're given a list of subjects for students.Assume one classroom 
# required for one subject calculate the no. of classroom req.
# """

# subject={"python","java","C++","javascript","java","python","java","C++"}
# print("The number of classroom required is: ",len(subject))


# """
# Question 3:

# WAP to enter marks of 3 subjects from the user & store them in a dictionary.
# start with an empty dict and add them 1 by 1.USe subject as key and marks as value.
# """

# marksheet={}
# print("---Please enter the marks of the following subjects---")
# marksheet["maths"]=int(input("Maths: "))
# marksheet["English"]=int(input("English: "))
# marksheet["Physics"]=int(input("Physics: "))



#---------method2-----------
# marks={}
# x=int(input("enter Maths: "))
# marks.update({"Maths":x})
# print(marksheet)

"""
Question 4:

Figure out a way to store 9 and 9.0 as seperate values in a set
"""

set={9,"9.0"}
set2={("int",9),("float",9.0)}
print(set)