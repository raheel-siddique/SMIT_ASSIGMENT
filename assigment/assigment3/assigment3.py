# 1. Program to count vowels in a string and display

# str=input('enter your name')
# vowelsWords='aeiouAEIOU'
# vowelsCount=0
# vowelsChar=[]

# for char in str:
#     if char in vowelsWords:
#         vowelsCount+=1
#         vowelsChar.append(char)
# print(vowelsCount, vowelsChar)


# 2. Program to count uppercase, lowercase, digits, whitespace

# str=input("enter your name")
# countUpper=0
# countLower=0
# countDigit=0
# countSpaces=0

# for chr in str:
#     if chr.isupper():
#      countUpper+=1
#     elif chr.islower():
#      countLower+=1
#     elif chr.isdigit():
#      countDigit+=1
#     elif chr.isspace():
#      countSpaces+=1
# print("uppercase count", countUpper)
# print("lowercase count", countLower)
# print("digits count", countDigit)
# print("spaces count", countSpaces)



# 3. Swap first and last characters
  
# str=input('enter your name')
# firstChar=str[-1]
# lastChar=str[0]
# newStr=''
# newStr=firstChar+str[1:-1]+lastChar
# print(newStr)

# short method 

# newStr=str[-1]+str[1:-1]+str[0]
# print(newStr)

# 4. Reverse string without reverse() method

# revStr=str[::-1]
# print(revStr)

# 5. Shift string one position left
# shiftedStr=str[1:]+str[0]
# print(shiftedStr)

# 6. Print initials of full name
# initial=""
# parts=str.split(" ")

# for prs in parts:
#     print(prs[0].upper())
#     initials+=prs[0].upper()+". "
# print(initial)

# without using split method 

# initial=''
# initial+=str[0].upper()+". "

# for i in range(1,len(str)):
#     if str[i-1]==" ":
#      initial+=str[i].upper()+". "
     
# print(initial)


# 7. Palindrome check
# rev=''
# for strings in str:
#     rev=strings+rev
# if rev.lower()==str.lower():
#     print('palindrome')
# else:
#     print('not')


# 8. Print pattern
# word='SHIFT'
# for i in range(len(word)):
#     print(word[i:]+word[:i])
    
    
# 9. Password validation

# password=input('enter password')

# hasUpper=False
# hasLower=False
# hasDigit=False

# for pwd in password:
#     if pwd.isupper():
#         hasUpper=True
#     if pwd.islower():
#         hasLower=True
#     if pwd.isdigit():
#         hasDigit=True
# if len(password)>8  and hasUpper and hasLower and hasDigit:
#     print('password is saved')
# else:
#     print('password is invalid')
#     if not hasUpper:
#      print('please put upper case charachter here')
#     if not hasLower:
#      print('please put lower case charachter here')  
#     if not hasDigit:
#      print('please put digit here')    
    
