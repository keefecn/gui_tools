# -*- coding: utf-8 -*-
"""
@author: keefe
@date: 2020-12-2
@requirement: pyqtgraph pyqt5（无法安装，依赖vc++14.0）
@refer: https://github.com/swharden/Python-GUI-examples/tree/master/2019-02-03_pyQtGraph
"""

import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters


# set the styling of pyqtgraph
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

# create some data
pointCount = 1000
xs = np.arange(pointCount)/pointCount*np.pi*2*5
ys = np.sin(xs)

# add noise
ys += np.random.random_sample(len(ys))/10

# create plot
plt = pg.plot(xs, ys, title="Example PyQtGraph", pen='r')
plt.showGrid(x=True,y=True)


if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()