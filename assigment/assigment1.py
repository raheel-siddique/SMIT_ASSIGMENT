# 1. Program to count vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


# 2. Program to count uppercase, lowercase, digits, whitespace
string = input("Enter a string: ")
upper = lower = digit = space = 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Whitespace:", space)


# 3. Swap first and last characters
string = input("Enter a string: ")
if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string
print("New string:", new_string)


# 4. Reverse string without reverse() method
string = input("Enter a string: ")
rev = ""
for ch in string:
    rev = ch + rev
print("Reversed string:", rev)


# 5. Shift string one position left
string = input("Enter a string: ")
shifted = string[1:] + string[0]
print("Shifted string:", shifted)


# 6. Print initials of full name
name = input("Enter your full name (first middle last): ")
parts = name.split()
initials = ""
for p in parts:
    initials += p[0].upper() + ". "
print("Initials:", initials)


# 7. Palindrome check
string = input("Enter a string: ")
rev = ""
for ch in string:
    rev = ch + rev
if string.lower() == rev.lower():
    print("Palindrome")
else:
    print("Not Palindrome")


# 8. Print pattern
word = "SHIFT"
for i in range(len(word)):
    print(word[i:] + word[:i])


# 9. Password validation
password = input("Enter password: ")
valid = True

if len(password) < 8:
    print("Password must be at least 8 characters long")
    valid = False
if not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")
    valid = False
if not any(ch.islower() for ch in password):
    print("Password must contain a lowercase letter")
    valid = False
if not any(ch.isdigit() for ch in password):
    print("Password must contain a digit")
    valid = False

if valid:
    print("Password is valid")
