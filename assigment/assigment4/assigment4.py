# 1. Print alternate elements of a list


# lst = input("Enter list elements separated by space: ").split()
# for i in range(0,len(lst),2):
#     print(lst[i])

# short method 

# print(lst[::2])

# 2. Reverse list without using reverse()
# print(lst[::-1])

# from loop

# rev=[]
# for i in range(len(lst)-1, -1,-1):
#     rev.append(lst[i])
# print(rev)

# 3. Find largest number in list without max()
# lst = list(map(int, input("Enter list elements separated by space: ").split()))

# largestNum=lst[0]
# for num in lst:
#     if num>largestNum:
#         largestNum=num
# print(largestNum)

# 4. Rotate list elements (left shift)

# rotated = lst[1:]+lst[:1]
# print(rotated)

# from pop 
# firstElm=lst.pop(0)
# lst.append(firstElm)
# print(lst)

# 5. Delete a given word from string

# text=input('enter any sentence')
# word=input('enter word you want to delete')
# newStr=""
# if word in text:
#     newStr=text.replace(word,'')
# else:
#      print('deleted word in not in given string')
# print(newStr)


# 6. Convert mm/dd/yyyy to Month day, year
# date = input("Enter date in mm/dd/yyyy: ")
# months = ["January","February","March","April","May","June","July",
#           "August","September","October","November","December"]
# mm,dd,yyyy=date.split('/')
# monthName=months[int(mm)-1]
# print(f'{monthName} {dd}, {yyyy}')

# 7. Capitalize first letter of each word

# text=input('enter a sentence')
# newWord=[]
# for txt in text.split():
#     newWord.append(txt[0].upper()+txt[1:])

# result=" ".join(newWord)
# print(result)


# 8. Sum of each row in matrix
matrix = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42]
]

# for i in range(0,len(matrix)):
#     rowSum=0
#     for j in range(len(matrix[i])):
#         rowSum+=matrix[i][j]
#     print(f'sum of row {i+1} {rowSum}')

# using sum method 

# for i in range(0,len(matrix)):
#     rowSum=sum(matrix[i])
#     print(f'sum of row {i+1} {rowSum}')

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
