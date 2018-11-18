# coding: utf-8
"""
@desc: gui auto screen shot，书自动截屏
@author: Keefe
@date: 2016/11/18
@refer: 
"""

import time
import pyautogui

time.sleep(5)
for i in xrange(10):
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    pyautogui.screenshot('images/page_%d.jpg' %i)
    time.sleep(0.05)
