import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QSlider
from PyQt5.QtGui import QIcon
#******************************************************************
import matplotlib
matplotlib.use("Qt5Agg")
#******************************************************************
from PyQt5 import QtCore 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

import numpy as np
 
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.lines import Line2D
 
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		self.left = 10
		self.top = 10
		self.title = 'PyQt5 matplotlib example - pythonspot.com'
		self.width = 800
		self.height = 600
		self.initUI()
		

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		m = PlotCanvas(self, width=6, height=5)
		m.move(0,0)

		button = QPushButton('PyQt5 button', self)
		button.setToolTip('This s an example button')
		button.move(600,0)
		button.resize(140,100)
		
		slider = QSlider(self)
		slider.move(0,530)
		slider.resize(600,25)
		slider.setRange(0, 2047)
		slider.setPageStep(1)
		slider.setTickPosition(QSlider.TicksBothSides)
		slider.setTickInterval(100)
		slider.setOrientation(QtCore.Qt.Horizontal)
		slider.valueChanged[int].connect(self.SliderMoved)
		
		line = QLineEdit(self)
		line.move(600,730)
		line.resize(600,25)
		
		self.show()


	def SliderMoved(self, valueOfSlider):
		m = PlotCanvas(self)
		valueinit = valueOfSlider
		m.plot(valueOfSlider)
		pass

		
		#slider.
		
		
 
 
class PlotCanvas(FigureCanvas):
 
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)

		FigureCanvas.__init__(self, fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self,
				QSizePolicy.Expanding,
				QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.plot(valueinit)
 
	def plot(self, valinit):
		
		#valinit=1
		fov = 200

		#generate figure
		fig = plt.figure()
		fig.subplots_adjust(left=0.25, bottom=0.2)

		#creating slices list
		s=[]
		for i in range(3):
			s.append([slice(valinit-1, valinit, None) if j == i else slice(None) for j in range(3)])
		
		print (s)
		img_z = img[s[0]].squeeze()
		#img_x = cube[s[1]].squeeze()
		
		
		data = img_z
		#ax = plt.subplot(111)
		ax = self.figure.add_subplot(111)
		ax.imshow(data, cmap="gray")
		#ax.set_title('PyQt Matplotlib Example')
		#plt.draw()
		self.draw()
		#plt.show()
		
		
		#print (img_z)
		
		#plt.imshow(img_z,cmap='gray', vmin = 0, vmax = 255)
		
		"""
		Display a 3d ndarray with a slider to move along the third dimension.
		"""
		'''
		#check dim
		#if not cube.ndim == 3:
		#	raise ValueError("cube should be an ndarray with ndim == 3")

		valinit=1024
		fov = 200

		#generate figure
		fig = plt.figure()
		fig.subplots_adjust(left=0.25, bottom=0.2)

		#creating slices list
		s=[]
		for i in range(3):
			s.append([slice(valinit-1, valinit, None) if j == i else slice(None) for j in range(3)])
		img_z = cube[s[0]].squeeze()
		img_x = cube[s[1]].squeeze()

		#display initial image
		ax1 = plt.subplot(121)
		ax2 = plt.subplot(122)

		ax1.imshow(img_z, cmap='gray')
		ax2.imshow(img_x, cmap='gray')
		'''
			
		'''
		data = [random.random() for i in range(25)]
		ax = self.figure.add_subplot(111)
		ax.plot(data, 'r-')
		ax.set_title('PyQt Matplotlib Example')
		self.draw()
		'''
 
if __name__ == '__main__':
	cube = "/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/recon/tomo-2048x2048x2048_8bit.b"
	fd = open(cube, 'rb')
	width = 2048
	height = 2048
	slices = 2048
	global img
	global valueinit
	valueinit=1024
	img = np.memmap(cube, dtype=np.uint8, shape=(slices, width, height))
	fd.close()
	
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
