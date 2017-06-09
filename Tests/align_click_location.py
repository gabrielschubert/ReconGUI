### Voxel selection for local tomography
### Author: Gustavo J. Q. Vasconcelos
### email: gustavo.vasconcelos@lnls.br


from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
#******************************************************************
import matplotlib
matplotlib.use("Qt5Agg")
#******************************************************************
from PyQt5 import QtCore 



import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.lines import Line2D

def cube_show_slider(cube, **kwargs):
	"""
	Display a 3d ndarray with a slider to move along the third dimension.
	"""

	#check dim
	if not cube.ndim == 3:
		raise ValueError("cube should be an ndarray with ndim == 3")

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
	
	print(s[0])
	print(img_z)

	#display initial image
	ax1 = plt.subplot(121)
	ax2 = plt.subplot(122)

	ax1.imshow(img_z, cmap='gray')
	ax2.imshow(img_x, cmap='gray')

	#define slider
	ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])

	slider = Slider(ax, 'Slice:', 1, cube.shape[0] - 1, valinit, valfmt='%i')

	#create initial lines
	line1 = Line2D([0,2048],[valinit,valinit])
	ax1.add_line(line1)

	line2 = Line2D([0,2048],[valinit,valinit])
	ax2.add_line(line2)

	plt.draw()

	def onclick(event, **kwargs):
		if event.inaxes == ax1.axes:

			#print cursor values
			print('Slice=%i, xdata=%i, ydata=%i' %(slider.val, event.xdata, event.ydata))

			#create and update projection
			s1=[]
			for i in range(3):
				s1.append([slice(int(event.ydata-1), int(event.ydata), None) if j == i else slice(None) for j in range(3)])
			img_x = cube[s1[1]].squeeze()

			ax2.imshow(img_x, cmap='gray')

			#creating shapes
			c1 = plt.Circle((event.xdata, event.ydata), fov, color=(0, 0, 1), fill=False, clip_on = False)
			r1 = plt.Rectangle((event.xdata-fov, slider.val-fov), 2*fov, 2*fov,color=(0, 0, 1), fill=False, clip_on = False, **kwargs)

			line1.set_ydata([event.ydata, event.ydata])

			#image update
			ax1.add_artist(c1)
			ax2.add_artist(r1)
			plt.draw()

			#remove shapes but not update
			c1.remove()
			r1.remove()

	def update(val, **kwargs):
		#get slider value
		ind = int(slider.val)

		#create and update slice
		s2=[]
		for i in range(3):
			s2.append([slice(ind-1, ind, None) if j == i else slice(None) for j in range(3)])

		img_z = cube[s2[0]].squeeze()
		ax1.imshow(img_z, cmap='gray')

		line2.set_ydata([slider.val, slider.val])
		plt.draw()

	fig.canvas.mpl_connect('button_press_event', onclick)
	slider.on_changed(update)

	plt.show()

if __name__ == "__main__":
	import sys

	if len(sys.argv) == 3:
		cube = sys.argv[1]
		fd = open(cube, 'rb')
		width = 2048
		height = 2048
		slices = int(sys.argv[2])
		img = np.memmap(cube, dtype=np.uint8, shape=(slices, width, height))
		fd.close()

		cube_show_slider(img)
	else:
		print("Error")
