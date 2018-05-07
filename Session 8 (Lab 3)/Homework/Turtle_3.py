from turtle import*

def draw_square(x,y):
    for i in range(4):
        color(y)
        forward(x)
        lt(90)

a = draw_square(100,"blue")



mainloop()
