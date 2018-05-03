#Cách 1: pythonic

list = [1, 2, 3, 4, 5, 6]

x = int(input("Enter a number: "))

y = list.count(x)

if y >= 1:
    print(x, "avaliable in list")
else:
    print(x, "not avaliable in list")

#Cách 2:

list = [1, 2, 3, 4, 5, 6]

x = int(input("Enter a number: "))
