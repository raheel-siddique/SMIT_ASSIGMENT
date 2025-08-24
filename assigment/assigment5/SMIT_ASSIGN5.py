# 1. Print numbers 1 to 10 (for loop)
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Print numbers 20 to 1 (while loop)
i = 20
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

# 3. Print even numbers 1 to 10
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# 4. Print numbers 1 to n
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end=" ")
print()

# 5. Print odd numbers 1 to n
n = int(input("Enter a number: "))
for i in range(1, n+1, 2):
    print(i, end=" ")
print()

# 6. Print "Happy Birthday" five times
for i in range(5):
    print("Happy Birthday")

# 7. First n terms by squaring numbers
n = int(input("Enter a number: "))
print("The first", n, "terms are:")
for i in range(1, n+1):
    print(i**2, end=" ")
print()

# 8. Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 9. First 8 terms of AP (a=3, d=4)
a, d = 3, 4
ap = []
for i in range(8):
    ap.append(a + i*d)
print("AP:", ap)

# 10. First 6 terms of GP (a=2, r=3)
a, r = 2, 3
gp = []
for i in range(6):
    gp.append(a * (r**i))
print("GP:", gp)

# 11. Sum of all integers 1 to n
n = int(input("Enter a number: "))
s = 0
for i in range(1, n+1):
    s += i
print("Sum =", s)

# 12. Sum of reciprocals 1 to n
n = int(input("Enter a number: "))
s = 0
for i in range(1, n+1):
    s += 1/i
print(f"Sum of reciprocals 1 to {n} = {s:.2f}")

# 13. Take 5 numbers and display final sum
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    total += num
print("Final running total:", total)

# 14. Factorial of a number
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial:", fact)

# 15. Power without ** or math.pow()
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
if exp >= 0:
    for i in range(exp):
        result *= base
else:
    for i in range(-exp):
        result *= base
    result = 1/result
print("Result:", result)
