# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:41:09 2018
frozen dir
@author: yanhua
@refer: https://blog.csdn.net/weixin_42052836/article/details/82315118
"""

import os 
import sys

def app_path():
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return os.path.dirname(sys.executable)

    return os.path.dirname(__file__)



if __name__ == "__main__":
    """ 外部调用 示例 """
    import frozen_dir
    SETUP_DIR = frozen_dir.app_path()    
    sys.path.append(SETUP_DIR)
    FONT_MSYH = matplotlib.font_manager.FontProperties(
                    fname = SETUP_DIR + r'\data\fonts\msyh.ttf',
                    size = 8)
     
    DIR_HELP_DOC = SETUP_DIR + r'\data\docs'
