import turtle

win = turtle.Screen()

t1 = turtle.Turtle()
t1.circle(100)
t1.circle(100, steps=3)#3이면 삼각형 4면 사각형
t1.circle(100, steps=4)

win.onkey(exit,'q')
win.listen()

win.mainloop()