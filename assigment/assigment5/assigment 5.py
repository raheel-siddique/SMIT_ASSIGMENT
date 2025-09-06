# 1. Print numbers 1 to 10 (for loop)
# for i in range(1,10+1):
#     print(i)

# 2. Print numbers 20 to 1 (while loop)

# for i in range(20,1-1,-1):
#     print(i)

# 3. Print even numbers 1 to 10

# for i in range(2,10,2):
#     print (i)


# 4. Print numbers 1 to n
# n=int(input('write a number'))
# for i in range(1,n+1):
#     print(i)

# 5. Print odd numbers 1 to n
# for i in range(1,n+1,2):
#     print(i)

# 6. Print "Happy Birthday" five times

# for i in range(0,5):
#     print('happy boirthdya')

# 7. First n terms by squaring numbers

# n = int(input("Enter how many terms: "))

# for i in range(1, n+1):
#     print(i*i, end=" ")


# 8. Multiplication table
# table=int(input('enter  table number'))
# for i in range(1,10+1):
#     print(f'{table}*{i}={table*i}')


# 9. First 8 terms of AP (a=3, d=4)

# a = 3
# d = 4
# n = 8

# for i in range(n):
#     term = a + i*d
#     print(term, end=" ")

# a = 2
# r = 3
# n = 6

# for i in range(n):
#     term = a * (r**i)
#     print(term, end=" ")

# n=int(input('enter number'))
# sum=0
# for i in range(0,n+1):
#     sum+=i
    
# print(sum)


# 12. Sum of reciprocals 1 to n

# n = int(input("Enter n: "))
# s = 0

# for i in range(1, n+1):
#     s += 1/i

# print("Sum of reciprocals from 1 to", n, "=", s)

# sum=0
# for i in range(0,5):
#     nums=int(input("enter number"))
#     sum+=nums
# print(sum)


# 14. Factorial of a number

# n=int(input('enter number'))
# if n<0:
#     print('factoiral doenst exist for negative numbers')
# elif n==0:
#     print('factoiral of 0 is 1')
# else:
#     fact=1
#     for i in range(1,n+1):
#         fact*=i

#     print('factorial',fact)    

# a = int(input("Enter base: "))
# b = int(input("Enter exponent: "))

# result = 1
# exp = abs(b)   

# for i in range(exp):
#     result *= a

# if b < 0:
#     result = 1 / result   

# print(f"{a}^{b} = {result}")

