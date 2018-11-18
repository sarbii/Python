import turtle
import random


wn = turtle.Screen()
wn.title('gubuk')

t1 = turtle.Turtle()

t1.shape('turtle')

t1.color('blue')




#t1.right(90)
#t1.penup()
#t1.forward(200)
#t1.pendown()
#t1.left(90)
a= int(input())

t1.circle(a)
t1.left(90)
t1.color('white')
t1.forward(a)
t1.color('blue')
t1.left(90)
t1.forward(a/2)
t1.left(90)
t1.forward(a/2)
t1.left(90)
t1.forward(a/2)
t1.left(90)
t1.forward(a/2)