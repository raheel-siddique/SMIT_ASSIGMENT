# creating a list of dictiniores

# courses=[
#     {"courseId":1, "courseName":"Cloud"},
#     {"courseId":2, "courseName":"development"},
#     {"courseId":3, "courseName":"Graphic designing"}
#         ]

# courses.append({"courseId":4, "courseName":"web designing"})
# print(courses)
# print(courses[0]['courseName'])

# customerData={
#     'firstName':"Raheel",
#     'age':15,
#     'hobbies':['cricket', 'gym', 'food']
# }

# print(customerData["hobbies"][0])

# creating dic into dic 

# customerData={
#     'firstName':"Raheel",
#     'age':15,
#     'hobbies':['cricket', 'gym', 'food'],
#      "myFriendData":{'name':'junaid','age':50, 'qualification':"nothing",'hobbies':['cricket', 'gym', 'food']}
# }
# print(customerData['myFriendData']['name'])


#  Functions
# we use this for resuabilty of code 

# def addition():
#     num1=int(input('enter number first '))
#     num2=int(input('enter number second'))
#     totalNumbers=num1+num2
#     print(totalNumbers)

# addition()
# addition()
# addition()
# addition()
# addition()
# addition()


# task 
# take 2 numbers and operator as input 
# perform calculation based on user input

# def calculator(num1,num2,oper):
   
#     expression=f'{num1}{oper}{num2}'
#     result=eval(expression)
#     print(result)

# num1=int(input('enter number first '))
# num2=int(input('enter number second'))
# operator=input('enter operator')

# calculator(num1,num2,operator)


# simple way 

# def calculator():
#  num1=int(input('enter number first '))
#  num2=int(input('enter number second'))
#  operator=input('enter operator')

#  if operator=='+':
#     result=num1+num2
#     print(result)
#  elif operator=='-':
#     result=num1-num2
#     print(result)
    
#  elif operator=='*':
#     result=num1-num2
#     print(result)
    
#  elif operator=='/':
#     result=num1/num2
#     print(result)
    
#  else:
#      print('invalid operator')

# calculator()


# task 
#   1)register a user with this name , email and password
#   save name , email and password in  a list 
# 2)create another fucntion to login a user with his email and password


# users=[]
# def registerUser():
#     name=input('enter name')
#     email=input('enter email')
#     password=input('enter password')
#     userInfo=[name,email,password]
#     users.append(userInfo)

# def loginUser():
#     name=input('enter name')
#     email=input('enter email')
    
#     for user in users:
#         if user[0]==name and user[1]==email:
#             print('you are successfully logged in')
#         else:
#             print('user doesnt exist')
# registerUser()
# loginUser()
            
    
    