#!/usr/bin/python
#coding: utf-8

from Tkinter import *
import tkMessageBox

root = Tk()
root.title("窗口标题")

# create component
# editframe + bottomfarame + textframe
editframe = Frame(root)
bottomframe = Frame(root)
textframe = Frame(root)
editframe.pack()
bottomframe.pack()  # side = BOTTOM
textframe.pack()

# editframe:
label = Label(editframe, text="datapath:", relief=RAISED)
E1 = Entry(editframe, bd=5)
label.pack(side=LEFT)
E1.pack(side=RIGHT)


# bottomfarame:
# callback func
def commitCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World")


button1 = Button(bottomframe, text="start", command=commitCallBack)
button1.pack(side=LEFT)

# textframe:
text = Text(textframe)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

root.mainloop()  # 进入消息循环
