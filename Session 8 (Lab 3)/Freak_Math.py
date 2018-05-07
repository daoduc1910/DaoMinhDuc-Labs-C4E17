from random import *
from evaluate import calc

x = randint(0,10)
y = randint(0,10)


op = choice(["+", "-", "*", "/"])

res = calc(x ,y, op)

error = choice([-1,0,0,0,1])
display = res + error

print("*" *20)
print("{0} {1} {2} = {3} ".format(x, op, y,display))
print("*" *20)

ans = input("(Y/N)").upper()

if ans == "Y":
    if display == res:
        print("YAY")
    else:
        print("Try again!")
if ans == "N":
    if display != res:
        print("YAY")
    else:
        print("Try again!")
