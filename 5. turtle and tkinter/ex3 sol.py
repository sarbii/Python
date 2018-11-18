from tkinter import *


def fun1():
    str1 = e2.get()#엔트리값가져오기
    l3.configure(text= str(str1)+'='+str(eval(str1)))


win=Tk()

f1=Frame()

f3=Frame()


win.title("tk")
win.geometry('500x500')

l1 = Label(f1,text = 'Operation')
e2 = Entry(f1)


l2 = Label(f1,text = 'Result')
l3 = Label(f1,text = '')


btn1 = Button(f3,text = 'Calculating',command = fun1)#버튼누르면 레이블이름 바꾸기


l1.grid(column = 0 , row = 0)
e2.grid(column = 1 , row = 0)

l2.grid(column = 0 , row = 1)
l3.grid(column = 1 , row = 1)


btn1.pack()

f1.pack()

f3.pack()

win.mainloop()