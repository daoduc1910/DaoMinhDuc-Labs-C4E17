from turtle import*

speed(0)
def draw_square(x,y):
    for i in range(4):
        color(y)
        forward(x)
        lt(90)

#a = draw_square(100,"blue")
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()



mainloop()
