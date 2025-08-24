# problems in variables 
# storing cities in many variables 
# city_0="karachi"
# city_1="lahore"
# city_2="hyderabad"
# city_3="islambad"
# etc 

# 1 managing collection 
# 2 slower because it stores variables in storages
# 3 solution data structure  


# List(managing collection of values together its like an array)
# its identity is []
# we use , as a seperator 
# cities = ["karachi", "lahore", "islamabad", "hyderbaad"]
# print(type(cities))

# methods of list

# append or elemenbt add krna  end me 
# cities.append("faislabad")
# print(cities)


# print(cities.count('karachi'))


# extend ye koi na koi itertable lega means ak se zada more than 1 values

# cities.extend(['Quetta', "Multan"])
# print(cities) 


# insert  means value add krna konse index pe ye batna pre ga 
# cities.insert(1,'peshawar')1


# index index batata he 
# print(cities.index('Multan'))


# copy return the shallow copy of the list 

# newCities=cities.copy()
# print(cities)
# print(newCities)

# pop: element nikaalana 

# cities.pop(5)
# print(cities)

# agar index na den to last wali nikaale ga


# remove: remove the first occurence of the values means agfar 2 dafa aarhe hon to ohle ko nikaale ga 

# cities.insert(2,'sukkur')
# print(cities)


# reverse list ka order reverse krna 

# cities.reverse() 

# sort:sort krna 

# clear:it removes all the items 

# cities.clear()
# shallow copy:  
# 1 means ak hi addreess pe nh rkhta diffrent hota 
#  2 or values chnage kre first ki to secodn pe frk nh pre ga 

# newCities=cities.copy()
# cities.insert(1,'new val')
# print(cities)
# print(newCities)


# Shallow copy vs Deep copy
# Shallow copy: Sirf top-level list copy hoti hai, nested objects same reference share karte hain.

# Deep copy: Har nested element ka bhi naya copy ban jata hai.
# Bhai simple lafzon me — deep copy tab use hota hai jab tumhari list ke andar nested lists ya complex objects ho, aur tum chahte ho ki copy bilkul alag ho, original se koi link na rahe.


# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)  # shallow copy
# shallow[0][0] = 99

# print("Original:", original) # [[99, 2], [3, 4]]
# print("Shallow:", shallow)   # [[99, 2], [3, 4]]  (same change!)

# Deep copy ka farq
# Har nested list/object ka bhi naya copy banata hai

# Original aur copy completely independent ho jaate hain.


# tasks

# implement deep copy on list 
# adding diff values on diff method without insert() method   

 


cities = ["karachi", "lahore", "islamabad", "hyderbaad"]


# cities[2]='sukkur'
# print(cities)

# slicing list k tukre krna 

# print(cities[2:3])


# print(cities[1:8])

# reverse krna 
# print(cities[::-1])


# task 
# create a list of names 
names = ['raheel', 'junaid', 'owais', 'anas', 'qasim']
# names.sort()
# print(names)
names.append("taha")
# print(names)
names.extend(['taha', 'sarah'])
# print(names)
# names.reverse()
# print(names)
# names.remove('taha')
# print(names)
# names.pop(5)
# print(names)
names.insert(3, 'rehman')
# print(names)

# new_names=names.copy()
# names.remove('taha')
# print(new_names)
# print(names)

new_names=names
names.append('usman')
print(new_names)
print(names)