import turtle

win = turtle.Screen()

t1 = turtle.Turtle()
t1.circle(100)
t1.circle(100, steps=3)#3�̸� �ﰢ�� 4�� �簢��
t1.circle(100, steps=4)

win.onkey(exit,'q')
win.listen()

win.mainloop()