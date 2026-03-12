#break condition
for i in range(10):
    if i == 2:
        break
    print(i)

#continue condition
for i in range(10):
    if i == 2:
        continue
    print(i)

#we have to give start and end and also continue
for i in range(5,10):
    if i == 7:
        continue
    print(i)

#this is used to find out the odd number
for i in range(1,10,2):
    print(i)

# this is used to find the even number
for i in range(0,10,2):
    print(i)

#list in for loop
list=["kirubha","abhi","karthi"]
for i in list:
    print(i)

# the output will be 
# kirubha
# abhi
# karthi
#list without for loop 
list=["kirubha","abhi","karthi"]
print(list)

# the output wil be ['kirubha', 'abhi', 'karthi']

name = "kirubha"
for i in name:
    print(i)