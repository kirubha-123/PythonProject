print("Welcome to Python")

username = "kirubha"
exp = 10
is_active = True
value = 12.000

print("username", username)
print("exp", exp)
print(is_active)
print(type(username))
print(type(exp))
print(type(is_active))
print(type(value))

nameInput = input("Enter a name: ")
print(nameInput)
a = int(input("Enter number A : "))
b = int(input("Enter number B : "))
print(type(a))
print(a + b)
print(a - b)
print(a * b)
print(a/b)

if(a == b):
    print("A and B are equal")
else:
    print("A and B are not equal")

kirubha = input("Enter a name : ")
print(kirubha)

a = int(input("enter A value : "))
b = int(input("Enter b value : "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

if(a==b):
    print(True)
else:
    print(False)


tamil = int(input("Enter the mark of A : "))
English = int(input("Enter the mark of B : "))
Maths = int(input("Enter the mark of C : "))
Science = int(input("Enter the mark of D : "))
Social = int(input("Enter the mark of E : "))

total = tamil+English+Maths+Science+Social
average = total / 5

print("total marks : ",total)
print("average : ",average)

if(average>=90):
    print("Your Grade O")
elif(average>=80):
    print("Your Grade A+")
elif(average>=70):
    print("Your Grade A")
elif(average>=60):
    print("Your Grade B+")
elif(average>=50):
    print("Your Grade is B")
else:
    print("FAIL")

if (tamil>English):
    print("tamil is higher : ",tamil)
elif(English>Maths):
    print("English is higher : ",English )
else:
    print("Maths is higher : ",Maths)
