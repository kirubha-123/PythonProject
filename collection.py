my_list = [1,2,3,4]
my_list.append(5)
print(my_list)

my_list1 = [1,3,4]
my_list1.insert(1,2)
print(my_list1)

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

new_list = list1 + list2
print(new_list)

list1.remove(2)
print(list1)

removed_value = list1.pop(2)
print(list1)
print(removed_value)

pop_new = list1.pop()
print(pop_new)

list1.clear()
print(list1)

list3 = [1,2,3,4,5,6]
del list3[4]
print(list3)

del list3[1:3]
print(list3)

list4 = [10,20,30,40]
list4[1] = 50
print(list4)

list4[2:4] = [60,70,80,90,100]
print(list4)