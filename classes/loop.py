# for i in range(4):
#     print(i)

# friendsName=['raheel', 'junaid', 'faizan', 'owais', 'anas']
# for myFriends in friendsName:
#     print(myFriends)
# print(friendsName)



# write a program that prints a happy biorthday five times on a screen 

# for i in range(0,5):
#     print('happy birthday', i)

# write a prgramm that takes a number n input from the user and generates the first n terms of the se
# ries form by squarning the natural number 


# num1=int(input("enter a number"))

# for i in range(1, num1+1):
#     print(i**2)

# list=[i**2 for i in range(1,num1)]
# for elements in list:
#  print(elements)



# write a program that promots the user to input a number and prints its multiplication table 
# table=int(input("enter a number"))
# startFrom=int(input("enter a start number"))
# endFrom=int(input("enter a end  number"))
# for i in range(startFrom,endFrom+1):
#     print(f"{table}*{i}={table*i}")
# tableList = [(f"{table}*{i}={table*i}") for i in range(startFrom, endFrom+1)]
# for table in tableList:
#     print(table)
# print(tableList)




# print tables from 2 to 5 in a such a way every table print one time less than other

# limit =10
# for tableNumber in range(2 , 6):
#     # print(tableNumber)
#     for i in range(1,limit+1):
#         print(f"{tableNumber}*{i}={tableNumber*i}")
#     limit-=1

# tableList=[f"{tableNumber} * {i} = {tableNumber * i}"  for tableNumber in range(2,6) for i in range(1,limit+1)]
# print(tableList)


