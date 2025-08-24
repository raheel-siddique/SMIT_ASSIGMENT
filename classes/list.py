# list assignment

# write a program that acccepts the list from user and print the alternative element  of list 

# numbers=[1,2,3,4,5,8,6,9,100]
# for myNums in range(0, len(numbers), 2):
#     print(numbers[myNums])
    
# print(numbers[::2])   # alternate elements directly


# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# for i in range(0, len(numbers), 2):
#     print(numbers[i])

# print(numbers)


# write a programm that accepts a list from user. your program should reverse the content of list
# and dsiplay it. dont use reverse method   

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# newArr=[]
# for i in range(len(numbers)-1, 0-1, -1):
#         newArr.append(numbers[i])
# print(newArr)

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# print(numbers[::-1])


# find and display large number 
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# muNums=numbers[0]
# for i in range(0,len(numbers)):
#     if(numbers[i] > muNums):
#         muNums = numbers[i]
# print(muNums)


# find and display smallerst number 

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# muNums=numbers[0]
# for i in range(0,len(numbers)):
#     if(numbers[i] < muNums):
#         muNums = numbers[i]
# print(muNums)

# write a program that roatest the elenmt of the list so that the element of first
# index moves to the second index. the elemnt in the second moves in a third index 
# , etc. and the element in the last index move to the first index 

# nums= [1,2,3,4,5,6,7,8,50]
# lstElm= nums.pop()
# print(lstElm)
# nums.insert(0,lstElm)
# print(nums)

# write a program that input a string and ask user to delete a given word from a string 
# str=input("write the sentence")
# giveWords=input("write the word whcih do u want to delete")

# newStr=str.replace(giveWords, "")
# print(newStr)


# str=input("write the sentence")
# giveWords=input("write the word whcih do u want to delete")

# lstStr=str.split()
# newStr=[]


# from for loop 
# for strs in lstStr:
#     if(strs != giveWords):
#         newStr.append(strs)
# newVal=" ".join(newStr)
# print(newVal)


# from filter 
# newWords=list(filter(lambda strs: strs!=giveWords, lstStr))
# newArr=' '.join(newWords)
# print(newArr)   

# from list comprehension 
# removeWord=[str for str in lstStr if(str!=giveWords)]
# print(removeWord)

     


# find the even numbers 
# evenNums=[]
# for nums in range(0,10):
#     if(nums%2==0):
#          evenNums.append(nums)
        
# print(evenNums)

# evenNums=[nums for nums in range(0,10) if nums%2==0]


# print(evenNums)

myNums=[]
for i in range(0,10):
    myNums.append(i)

# myEven=list(filter(lambda nums:nums%2==0, myNums))
# print(myEven)

# myEven=[]
# for nums in myNums:
#     if(nums%2==0):
#         myEven.append(nums)
        
# print(myEven)
        
# myEven=[nums for nums in myNums if nums%2==0]
# print(myEven)        



