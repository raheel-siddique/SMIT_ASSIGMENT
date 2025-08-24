# loops ak cheez ko dobara baar baar repeat krna tab tak khtm na ho.or ye collection of values pe run hota he

# syntax 
# for tem_var in iteratable([1,2,4,5,6,7,8]):
#     loop_body
    
# for temp in [1,2,4,5,6,8,9]:
#     print(temp)

# for temp in ("Raheel",'Siddique', '1000', True):
#     print(temp)

# for temp in {1,2,4,6,6,6}:
#     print(temp)

# write a program that prints a happy biorthday five times on a screen 

# for myString in range(5):
#     print("happy birthday")

# write a prgramm that takes a number n input from the user and generates the first n terms of the se
# ries form by squarning the natural number 
    
# sample ouput 
# enter a number 6
# the first six terms of the series are 1,4,9,16,25,36


# num=int(input('put number'))

# for seriesIndex in range(1,num+1):
#     print(seriesIndex * seriesIndex)






# write a program that promots the user to input a number and prints its multiplication table 


# range ka function kaha se kaha tak chlaan he 
# range(0,5) 0 se start krna  5 tak chalnana

# numberOfTimes=int(input("how many times you want tp run a string"))
# for temp in range(numberOfTimes):
#     print(temp+1,'happy birthday!!')



# num=int(input('enter a number'))
# for temp in range(num):
#     print((temp+1)**2)


# num=int(input('enter a number which table u want to print'))
# startTimes=int(input('how  start many times'))
# endTimes=int(input('how end times'))
# for temp in range(startTimes,endTimes+1):
#     print(num*(temp))


# print to table 2 to 5 or ak ak decrement hota rehta 

# print tables from 2 to 5 in a such a way every table print one time less than other

# num=int(input("enter number ")) 

# for table in ([2,3,4,5]):
#     print()

# starttimes=int(input('enter start times'))
# endTimes=int(input('enter end times'))
# times=int(input('enter table time'))
# for myTable in range(starttimes,endTimes):
#     for temp in range(times):
#         print(myTable*(temp+1))
#     times-=1
    
    
    
# Dictionary whicn has key and value its same like javascript object

# syntax 
myData={'firstName':"Raheel", 'lastName':"Siddique", 'age1':25, "weight":65}

# myData['isPresent']=True

# myData.keys()
# myData.values()
# myData.items()
# print(myData.get('firstNames')) hogi to value dega wrna nh


# myData.pop('firstName') 
# myData.popitem() 

# myData.update({'firstName':'junaid'}) 

# myData.setdefault('age','20')
# myData.clear()
# myData.copy()
# keys=['firstName', 'lastName']
# newData=myData.fromkeys(keys)
# print(newData)
# print(myData)

# for key,value in myData.items():
#     print(key,value)

# dict or list assigment or revision 


# list/dic comprehension 

# normal way of code 
# lst=[]
# for temp in range(10):
#     lst.append(temp)
    
# print(lst)


# # advance 
# newList=[temp if temp%2==0 else "odd" for temp in range(10) ] 

# print(newList)   


# dic comprehension

# list1 = ["name", "age", "city"]
# list2 = ["Ali", 22, "Lahore"]

# myDic=dict(zip(list1, list2))

# print(myDic)

# paractice loops, dict, list comp , dic comp 








