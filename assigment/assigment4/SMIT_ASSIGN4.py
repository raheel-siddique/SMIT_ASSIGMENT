# 1. Print alternate elements of a list
lst = input("Enter list elements separated by space: ").split()
print("Alternate elements:", lst[::2])


# 2. Reverse list without using reverse()
lst = input("Enter list elements separated by space: ").split()
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print("Reversed list:", rev)


# 3. Find largest number in list without max()
lst = list(map(int, input("Enter numbers separated by space: ").split()))
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("Largest number:", largest)


# 4. Rotate list elements (left shift)
lst = input("Enter list elements separated by space: ").split()
rotated = lst[1:] + [lst[0]]
print("Rotated list:", rotated)


# 5. Delete a given word from string
text = input("Enter a string: ")
word = input("Enter word to delete: ")
new_text = text.replace(word, "")
print("Updated string:", new_text)


# 6. Convert mm/dd/yyyy to Month day, year
date = input("Enter date in mm/dd/yyyy: ")
months = ["January","February","March","April","May","June","July",
          "August","September","October","November","December"]
mm, dd, yyyy = date.split("/")
month_name = months[int(mm)-1]
print(f"{month_name} {int(dd)}, {yyyy}")


# 7. Capitalize first letter of each word
sentence = input("Enter a sentence: ")
words = sentence.split()
new_sentence = ""
for w in words:
    new_sentence += w[0].upper() + w[1:].lower() + " "
print("Capitalized:", new_sentence.strip())


# 8. Sum of each row in matrix
matrix = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42]
]
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")


# 9. Add two matrices
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print("Matrix Addition:", result)


# 10. Multiply two matrices
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        s = 0
        for k in range(len(B)):
            s += A[i][k] * B[k][j]
        row.append(s)
    result.append(row)
print("Matrix Multiplication:", result)
