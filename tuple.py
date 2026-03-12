empty_tuple = ()
print(empty_tuple)

tuple1 = (1,2,3,4,"HI")
print(tuple1)

tuple1 = 1,2,3,4,"HI"
print(tuple1)

tuple = (10,20,30,40)
print(tuple)
print(type(tuple))

print(max(tuple))
print(min(tuple))
print(len(tuple))
print(tuple[1:3])
print(tuple[-2])
print(tuple[0])


for i in tuple:
    print(i)