# -*- coding: utf-8 -*-


import time
import requests
import logging
import random
import hashlib
import threading

from tkinter import *

RUN_FLAG = True
LOG_LINE_NUM = 0
COUNT = 0


def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(5.5, fun_timer)
    timer.start()


# timer = threading.Timer(1, fun_timer)
# timer.start()


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("流量工具_v1.0")  # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高

        # 第一行用户名输入框
        self.timer_label = Label(self.init_window_name, text='定时时间（秒）：')
        self.timer_label.grid(row=2, sticky=W)
        self.timer_edit = Entry(self.init_window_name)
        self.timer_edit.grid(row=2, column=1, sticky=E, padx=3)  #
        self.start_button = Button(self.init_window_name, text="开始执行", bg="lightblue", width=20,
                                   command=self.access_url)  # 调用内部方法  加()为直接调用
        self.start_button.grid(row=2, column=4)

        # 按钮
        # self.stop_button = Button(self.init_window_name, text="停止执行", bg="lightblue", width=20,
        #                           command=self.stop_gui())  # 调用内部方法  加()为直接调用
        # self.stop_button.grid(row=2, column=11)

        # 标签
        self.init_data_label = Label(self.init_window_name, text="待处理URL：")
        self.init_data_label.grid(row=4, column=0, sticky=W)
        self.result_data_label = Label(self.init_window_name, text="输出结果：")
        self.result_data_label.grid(row=4, column=12, sticky=W)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=11, column=0)

        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=5, column=0, rowspan=5, columnspan=5)  # 10*10的合并区域
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=5, column=10, rowspan=20, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=12, column=0, rowspan=20, columnspan=8)

    def access_url(self):
        global RUN_FLAG, COUNT
        src = self.init_data_Text.get(1.0, END).strip()
        if not src:
            src = "http://www.baidu.com"
        src = src.split('\n')  # .replace("\n", "").encode()
        if isinstance(src, list):
            src = src[random.randint(0, len(src) - 1)]
        print("src =", src)
        try:
            response = requests.get(src)
            COUNT += 1
            self.result_data_Text.insert(1.0, f"[{COUNT}] {src} {response.status_code}\n")
            self.write_log_to_Text(f"INFO:access_url success: {response.content}\n")
        except Exception as e:
            self.write_log_to_Text(f"INFO:access_url exception: {str(e)}\n")

        timer_time = float(self.timer_edit.get()) * 1000 if self.timer_edit.get() else 1000
        self.init_window_name.after(int(timer_time), self.access_url)  # 每隔1s调用函数 gettime 自身获取时间

    def stop_gui(self):
        global RUN_FLAG
        RUN_FLAG = False

    def str_trans_to_md5(self):
        """ 字符串转 MD5 """
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        print("src =", src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
