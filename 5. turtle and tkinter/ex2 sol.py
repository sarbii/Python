import turtle
import math

win = turtle.Screen()
a= math.sqrt(2)
t1 = turtle.Turtle()




t1.circle(a*100)

t1.circle(a*100, steps=4)

t1.penup()

t1.left(90)

t1.forward(a*100 - 100)
t1.right(90)


t1.pendown()

t1.circle(100)
win.onkey(exit,'q')
win.listen()

win.mainloop()