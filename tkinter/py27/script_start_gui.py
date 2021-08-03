#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@desc: gui
@version: 1.0
@author: Keefe
@date: 2016/4/22
@refer: http://www.tutorialspoint.com/python/python_gui_programming.htm
    https://wiki.python.org/moin/TkInter/
'''

import time

from Tkinter import *  # 导入 Tkinter 库
import tkMessageBox


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class Application(Frame):
    ''' Application
    '''
    file_fullname = 'd:/project/topicspider/test/tools/rank_sort2.py'

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # editframe + bottomfarame + textframe
        self.editframe = Frame(self)
        self.bottomframe = Frame(self)
        self.textframe = Frame(self)
        self.editframe.pack()
        self.bottomframe.pack()  # side = BOTTOM
        self.textframe.pack()

        # editframe:
        self.label = Label(self.editframe, text='script_path:', padx=5)
        var = StringVar()
        self.E1 = Entry(self.editframe, bd=5, textvariable=var, width=50)
        var.set(self.file_fullname)
        self.label.pack(side=LEFT)
        self.E1.pack(side=RIGHT)

        # bottomfarame:
        self.button1 = Button(self.bottomframe, text="start",
                              command=self.commitCallBack)
        self.button1.pack(side=LEFT)

        # textframe:
        self.text = Text(self.textframe)
        self.text.insert(INSERT, "Hello.....")
        self.text.insert(END, "This is a Test.....")
        self.text.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

    def commitCallBack(self):
        # datapath = self.E1.get() or 'world'
        # tkMessageBox.showinfo('Message', datapath )
        self.text.delete(INSERT, END)
        self.text.insert(INSERT, "\n%s start rank_sort..." % 
                         get_current_time())
        self.text.insert(INSERT, "\n%s %s %s" % (
            get_current_time(), self.label.cget('text'), self.E1.get()))

        # call subprocess
        import threading
        threading.Thread(target=self.startProcess).start()
        # self.startProcess()

    def startProcess(self):
        # os.getcwd():
        # python d:/project/topicspider/namespider/anchor/rank_sort.py
        import sys
        import os
        import subprocess
        scriptfile = self.E1.get() or self.file_fullname
        if not os.path.exists(scriptfile):
            self.text.insert(
                INSERT, "\nCannot find scriptfile: \"%s\"." % scriptfile)
            return
        self.button1.configure(state=DISABLED)  # state: DISABLED/NORMAL/ACTIVE

        pargs = ['python', scriptfile]
        # shell=True~bad/blocked, False~ok/default
        p = subprocess.Popen(pargs, shell=False)
        p.wait()
        # self.text.insert(sys.stdout.readline())
        self.text.insert(INSERT, "\n%s end rank_sort..." % get_current_time())
        self.button1.configure(state=NORMAL)


if __name__ == "__main__":
    # start message loop
    app = Application()
    app.master.title('脚本启动助手')
    app.mainloop()
