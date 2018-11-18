from tkinter import *


def add():
    str1 = e1.get()#엔트리값가져오기
    str2 = e2.get()
    l4.configure(text = int(str1)+ int(str2))

def sub():
    str1 = e1.get()#엔트리값가져오기
    str2 = e2.get()
    l4.configure(text =int(str1)-int(str2))

def mul():
    str1 = e1.get()#엔트리값가져오기
    str2 = e2.get()
    l4.configure(text =int(str1)*int(str2))

def div():
    str1 = e1.get()#엔트리값가져오기
    str2 = e2.get()
    l4.configure(text = int(str1)/int(str2))


win=Tk()

f1=Frame()

f3=Frame()

f2=Frame()


win.title("tk")
win.geometry('500x500')

l1 = Label(f1,text = 'Operand')
e1 = Entry(f1)


l2 = Label(f1,text = 'Operand')
e2 = Entry(f1)

l3 = Label(f3,text = 'Result')
l4 = Label(f3, text = '')


btn1 = Button(f2,text = '+',command = add)#버튼누르면 레이블이름 바꾸기
btn2 = Button(f2,text = '-',command = sub)
btn3 = Button(f2,text = '*',command = mul)
btn4 = Button(f2,text = '/',command = div)



l1.grid(column = 0 , row = 0)
e1.grid(column = 1 , row = 0)

l2.grid(column = 0 , row = 1)
e2.grid(column = 1 , row = 1)

l3.grid(column = 0 , row = 0)
l4.grid(column = 1 , row = 0)







btn1.grid(column = 0 , row = 0)
btn2.grid(column = 1 , row = 0)
btn3.grid(column = 2 , row = 0)
btn4.grid(column = 3 , row = 0)

f1.grid(column = 0 , row = 0)

f3.grid(column = 1 , row = 0)
f2.grid(column =0, row =1)

win.mainloop()