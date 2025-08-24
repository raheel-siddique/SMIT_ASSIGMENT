import calendar
# Print Your Name with your Father name and Date of birth using suitable escape sequence charactor

print('Name:\t\t"Raheel Siddique"\nFather Name:\t"Abdul Qadir"\nDOB:\t\t"10-11-2003"')

# Write your small bio using variables and print it using print function

myBio='My Bio'
name="Raheel Siddique"
fatherName="Abdul Qadir Siddique"
dob="10-11-2003"

print("my bio:",myBio)
print("my name:",name)
print("my father name:",fatherName)
print("my DOB:",dob)


# Write a program in which use all the operators we can use in Python
a=10
b=15

# Arithmetic Operators
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a**b)

# Assignment Operators
a-=2
print(a)
a*=2
print(a)

a/=2
print(a)

a%=2
print(a)

a**=2

print(a)

# Comparison Operators

print("a == b:\t\t", a == b)
print("a != b:\t\t", a != b)
print("a > b:\t\t", a > b)
print("a < b:\t\t", a < b)
print("a >= b:\t\t", a >= b)
print("a <= b:\t\t", a <= b)


# Logical Operators
x=True
y=False
print(x and y)
print(x or y)


# Completes the following steps of small task:
# Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# Mention Variable of Total Marks and assign 300 to it
# Calculate Percentage

englishMarks=80
islamiatMarks=99
mathsMarks=90
totalMarks=300
obtainedMarks=englishMarks+mathsMarks+islamiatMarks
percentage=(obtainedMarks/totalMarks)*100
print(f"{round(percentage, 2)}%")


# Part -2 Python Basics (Conditional Statements)

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
serviceOfYear=int(input('how long have you been working here?'))
if serviceOfYear>5:
     salary=float(input('what is your salary?'))
     bonus=salary * (5/100)
     print('your bonus amount is', bonus)
else:
    print('you are not eligible for this bonus')
    
    
# Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

age=int(input("enter your age"))
if age>17:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


# Write a program to check whether a number entered by user is even or odd.
num=(int(input('enter a number')))
if num>=0:
 if num%2==0:
    print('even')
 else:
    print('odd')
else:
    print('invalid number')
    


# Write a program to check whether a number is divisible by 7 or not. Show Answer

num=14

if num%7==0:
    print('yeah its divisible by 7')
else:
    print('no its not divisible by 7')
    

# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

num=int(input('enter a number'))
if num%5==0:
    print("Hello")
else:
    print("Bye")
    
# Write a program to display the last digit of a number.

num=1001
lastDigit=num % 10
print(lastDigit)


# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

lenght = (int(input('enter lenght')))
breadth = (int(input('enter breadth')))
if lenght==breadth:
    print("Square")
else:
    print("Rectangle")

# Take two int values from user and print greatest among them.

num1=int(input('enter number'))
num2=int(input('enter number'))
if num1>num2:
    print('greatest number is', num1)
elif num2>num1:
    print('greatest number is', num2)
else:
    print('both are same')
        


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity=int(input('enter quantity'))
perCost = 100
totalCost=quantity*perCost
if totalCost > 1000:
   discount=totalCost * 10/100
   finalCost=totalCost-discount
   print("your final cost after discount is", finalCost)
else:
    print(totalCost)

# A school has following rules for grading system:
# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade.


stdMarks=int(input('enter marks'))
if stdMarks < 100 and stdMarks > 0:
    if stdMarks>80:
        print('A')
    elif stdMarks <=80 and stdMarks > 60:
        print('B')
    elif stdMarks <=60 and stdMarks > 50:
        print('c')
    elif stdMarks <=50 and stdMarks > 45:
        print('d')
    elif stdMarks <=45 and stdMarks > 25:
        print('e')
    elif stdMarks < 25:
        print('failed')
        
    
else:
     print('invalid')
    

# A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# Number of classes held

# Number of classes attended.

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.


totalClasses=int(input('enter total number of classes'))
attendClasses=int(input('enter attend classes'))


percentageOfClass=(attendClasses/totalClasses)*100

if percentageOfClass>=75:
    print("student is allowed to sit in the exam")
else:
    print("student is not allowed to sit in the exam")
    
    
# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

totalClasses=int(input('enter total number of classes'))
attendClasses=int(input('enter attend classes'))
medicalCause=input('do u have any medical cause?').upper()


# percentageOfClass=(attendClasses/totalClasses)*100

if percentageOfClass>=75 or medicalCause=='Y':
    print("student is allowed to sit in the exam")
else:
    print("student is not allowed to sit in the exam")

# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year=int(input('enter a year'))
if (year%400==0) or (year%4==0 and year%100!=0):
    print('its a leep year')
else:
    print('its not a leep year')

# short approach 
print('leap year' if(calendar.isleap(year)) else 'not a leep year' )


# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR"

age=int(input("enter age"))
gender=input("enter gender").lower()

if gender=='f':
    print('she will work only in urban areas')
elif gender=='m' and (age>=20 and age<=40):
    print('he may work in anywhere')
elif gender=='m' and (age>40 and age<=60):
    print('he will work in urban areas only')
else:
    print('ERROR!')
    

# write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
# uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
    
units = int(input("enter unit"))
if units<=100:
    bill=0
elif units<=300:
    bill=(units-100)*5
else:
    bill=(200*5)+(units-300)*10
print('total bill amount is RS.', bill)

# Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input('enter age of person first'))
age2=int(input('enter age of person second'))
age3=int(input('enter age of person third'))

oldest=max(age1,age2,age3)
youngest=min(age1,age2,age3)

print("Oldest age is:", oldest)
print("Youngest age is:", youngest)

# long method 

age1=int(input('enter age of person first'))
age2=int(input('enter age of person second'))
age3=int(input('enter age of person third'))

oldest=age1
youngest=age1

# check oldest 
if age2>oldest:
    oldest=age2
if age3>oldest:
    oldest=age3
    
# check youngest 

if age2<oldest:
    oldest=age2
if age3<oldest:
    oldest=age3

print("Oldest age is:", oldest)
print("Youngest age is:", youngest)