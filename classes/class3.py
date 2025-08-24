# class 3 

# concatenTION METHOD

# str1 = "raheel"
# str2 = "siddique"
# friendName = 'junaid'
# using + method 

# str1+str2

# using f strring method 

# f" my name is {str1} {str2} and my friend name is {friendName}"


# string formatting method 

# "{0}{1}".format(str1,str2)


# create a string using all formatting methods that print your first name and last name with some extra added sentence that describe u ?


# first_name = "Raheel"
# last_name = "Siddique"
# middle_name = "Hafiz"
# friend_name = "junaid"
#  method 1  for concatenation + method 
# print("my name is "+first_name+" " + last_name + " "+ "my friend name is "+ friend_name)

# method 2 using format string (f"")

# print(f"my name is {first_name} {last_name} and my friend name is {friend_name}")

# method 3 .format 

# print("{0} {1} {2}".format(first_name, middle_name,last_name))


# user input (means user se input lena)

# first_name = input("Enter your first name: ")
# middle_name = input("Enter your middle name: ")
# last_name = input("Enter your last name: ")

# print(first_name+" " + middle_name+" " +last_name)

# ab ye method hmesha strring me deta he value to hme agar number me convet krna he to init method use hoga 



# Conditional statemnt 
# id elif else 
# syntax 
# if <condition>:
#     <body>
# else:
#     <body> 


# passed = True
# if passed:
#     print("you are passed")
# else:
#     print('you are failed')


# if else 
# make a program that tell if you are eligible for certificate or not based on pass/fail 
# test = True
# if test:
#     print('you are eligble')
# else:
#     print("you are not eligble")


# elif 
# marks= int(input("enter your marks"))
# if marks>=90:
#     print("Excellent")
# elif marks>=80:
#     print("Good")
# elif marks>=70:
#     print("poor")
# else:
#     print("failed")
    
    
# nested if 

# shop_open = True
# if(shop_open):
#   basmatic_rice = bool(input("what is next?"))   
# if(basmatic_rice==True):
#     print("buy 1 kg")
# else:
#     print("buy nothing")
        
        
# write a program to check wheter a person is eligible for voting or not(ACCEPT age from user)
# if AGE IS GREATER THAN 17 ITS ELIGIBLE OTHEROWSE NOT 
# age = int(input("type your age: "))
# if age >=17:
#     print("you are elgigible for voting")
# else:
#     print("you are not elgigible for voting")
    
# grade = int(input("input your grade"))
# if grade >=17:
#     print("you are eligble for voting")
# else:
#     print("you are not eligble for voting") 

# write a program to check its even or odd 

# num1 = int(input("enter number"))
# if num1%2==0:
#     print('even')
# else:
#     print('odd')
    
# write a program to displayb m1 "hello" if a number entered by user is multiple,otherwise print "bye"
# num1 = int(input("enter number"))
# if num1%5==0:
#     print("hello")
# else:
#     print("bye")    

# Operator 
# NOT: not true 
# AND DONO CONDITION KA TRUE HONA ZARORI HE 
# OR: KOI AK CONDITION BHI TRUE HOGAI TO THK HE 

# WRITE  A PROGRAM A SCHOOL HAS FOLLWING RULES FOR GRADING SYSTEM 
# 1) bellow 25- f
# 2)  25 to 45-E
# 3) 45 to 50-D
# 4) 50 to 60-C
# 5) 60 to 80-B 
# 6) above 80-A

# marks = int(input("Enter your marks: "))

# if marks > 0 and marks <= 100:
#     if marks > 80:
#         print("Grade: A")
#     elif marks > 60 and marks <= 80:
#         print("Grade: B")
#     elif marks > 50 and marks <= 60:
#         print("Grade: C")
#     elif marks > 45 and marks <= 50:
#         print("Grade: D")
#     elif marks > 25 and marks <= 45:
#         print("Grade: E")
#     else:
#         print("Grade: F")
# else:
#     print("Invalid input. Please enter marks between 1 and 100.")

# methods of any type 

# methods of string 
# 'Raheel'.count("e")
# positive slicing 
# str = 'Raheel'
# str[0] 
# str[0:4]  slicing

# negatove slicing 
# str[-17:-4]  slicing

#  'raheel'.upper()
#  'raheel'.lower()
#  'raheel'.capitalize() also .title 

# methods of number 

# (20).

# len
# print(len('Raheel'))

# strip spaces remove krta he or unwanted character 

# print("   Raheel".strip())


# replace replace krta he 

# print("Raheel".replace("Raheel","Junaid"))



# charcter ki index find krne k lye 
# print("Raheel".find("e"))

# index Same as find() lekin agar nahi mila to error deta hai


# startsWith is charcater se start horaha ya nh 

# print("Raheel".startswith('j'))

# endsWith is charcater se start horaha ya nh 

# print("Raheel".startswith('j'))



