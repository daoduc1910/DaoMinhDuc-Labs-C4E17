from random import randint
import random

def calc( x , y, op):
    # x = randint(0,10)
    # y = randint(0,10)
    # op_list = ["+", "-", "*", "/"]
    # op = random.choice(op_list)
    res = 0
    #op = "+"
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y

    return res

print(__name__)
if __name__ == "__main__":
    print("eval.py imported")
#print(res)

#usage/call
# calc(3,7, "-")

#return argument
res = calc(1,2,"+")

#print(res)
