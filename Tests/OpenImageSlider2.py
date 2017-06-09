import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from PIL import Image
import numpy as np

 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 image - pythonspot.com'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()
	 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
	 
				
		img = Image.open( "LNLS_logo.jpg" )
		img.load()
		data = np.asarray( img, dtype="int32" )
		print (data)

		
		# Create widget
		label = QLabel(self)
		pixmap = QPixmap(data)#'LNLS_logo.jpg')
		label.setPixmap(pixmap)
		self.resize(pixmap.width(),pixmap.height())
	 
		self.show()
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
