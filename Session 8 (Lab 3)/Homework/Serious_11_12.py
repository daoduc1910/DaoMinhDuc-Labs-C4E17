def is_inside(x,y):
    if 140 <=x and x <= 240 and 60 <=y and y <=260:
        print(True)
        return(True)
    else:
        print(False)
        return False

x = int(input("x = "))
y = int(input("y = "))

is_inside(x,y)
