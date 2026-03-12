my_set = {1,2,3,3,4,5,2}
print(my_set) #set will not display duplicate values

# list to set conversion
set1 = set([1,2,3,4,5,3,2,4])
print(set1)

# identofy the element in the set 
print(2 in set1)
print(8 in set1)

#set to list conversion
my_list = list(set1)
print(my_list)

# add and remove element in the set
set1.add(8)
print(set1)
set1.remove(4)
print(set1)