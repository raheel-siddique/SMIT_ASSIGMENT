	
# 1 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# serviceOfYear=int(input('how long have you been working here?'))
# if serviceOfYear>5:
#     salary=float(input('what is your salary?'))
#     bonus = salary * 5/100
#     print('you are eligible for this bonus', bonus)
# else:
#     print('you are not eligible for this bonus')
    
    
# Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

# age=int(input('put your age'))
# if age>=17:
#     print('please vote')
# else:
#     print('cant vote')
    
    


# Write a program to check whether a number entered by user is even or odd.

# num1=int(input("enter number"))
# if num1%2==0:
#     print("even")
# else:
#     print("odd")
    
    
# Write a program to check whether a number is divisible by 7 or not. Show Answer

# num1=int(input("enter number"))
# if num1%7==0:
#     print("yeah its divisible by 7")
# else:
#     print("not its divisible by 7")
    
# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

# num1=int(input('enter number'))
# if num1%5==0: print('hii') 
# else: print("byyy")

# Write a program to display the last digit of a number.

# num1 = 1008
# lastDigit=num1 % 10
# print(lastDigit)    


# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
# length=int(input("put lenght"))
# breadth=int(input("put breDTH"))
# if length == breadth:
#     print("its square")
# else:
#     print("its recatnage")

# Take two int values from user and print greatest among them.

# num1=int(input("put number 1"))
# num2=int(input("put number 2"))
# if num1>num2:print("the greater number is", num1)
# elif num2>num1:print('the greater number is', num2)
# else:
#     print('both number are equal')
    


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit
# will cost 100. Judge and print total cost for user.

# quantity=12
# perQuantityCost=100
# netCost=perQuantityCost * quantity
# if netCost > 1000:
#     discount = netCost * 10/100
#     netCost=netCost-discount
#     print("netCost::", netCost)
# else:
#     print("netCost::", netCost)
    

# quantity=int(input('Enter the Quanity'))
# perQuanCost=100
# totalCost=perQuanCost * quantity

# if totalCost>1000:
#     discount=totalCost * 10/100
#     finalCost=totalCost-discount
#     print(finalCost)
# else:
#     print(totalCost)
    
#     A school has following rules for grading system:
# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade.


# stdMarks=int(input('enter marks'))
# if stdMarks < 100 and stdMarks > 0:
#     if stdMarks>80:
#         print('A')
#     elif stdMarks <=80 and stdMarks > 60:
#         print('B')
#     elif stdMarks <=60 and stdMarks > 50:
#         print('c')
#     elif stdMarks <=50 and stdMarks > 45:
#         print('d')
#     elif stdMarks <=45 and stdMarks > 25:
#         print('e')
#     elif stdMarks < 25:
#         print('failed')
        
    
# else:
#      print('invalid')
    

        
    	
# 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# Number of classes held

# Number of classes attended.

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.

# numOfClasses=100
# numOfClassesAttend=90
# percentOfClass=(numOfClassesAttend/numOfClasses)*100
# if percentOfClass>=75:
#     print("allow in exam")
# else:
#     print("dont allow in exam")
    

# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly
    
# numOfClasses=100
# numOfClassesAttend=30
# percentOfClass=(numOfClassesAttend/numOfClasses)*100
# medicalReports=False

# if percentOfClass<75 and medicalReports!=True:
#     print('dont allow in exam')
# else:
#     print('allow in exam')
    
    
    
#     Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.


# thisYear=int(input("year"))
# if thisYear%4==0:
#     if thisYear%100==0:
#         if thisYear%400==0:
#             print(thisYear,"its a leap year")
#         else:
#             print(thisYear,"its not a leap year")
#     else:
#             print(thisYear,"its  a leap year")
# else:
#     print(thisYear,"its not  a leap year")
    
    
#     Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR"

# age=int(input("age"))
# gender=input("gender")

# if gender=='female':
#     print("she will work only in urban areas")
# elif gender=='male' and (age>40 and age<=60):
#     print("he will work in urban areas only")
# elif gender=='male' and (age>20 and age<=40):
#     print("he may work in anywher")
# else:
#     print("Error")
    
    

        
            
    