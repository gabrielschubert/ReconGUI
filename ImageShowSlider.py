#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageShowSlider.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, "/home/gabrielschubert/QtDesigner_Interfaces/ReconGUI/Functions/")
from H5Files import getArray
from PIL import Image

class Ui_ImageShowWidget(object):
	def setupUi(self, ImageShowWidget):
		ImageShowWidget.setObjectName("ImageShowWidget")
		ImageShowWidget.resize(659, 527)
		self.gridLayout = QtWidgets.QGridLayout(ImageShowWidget)
		self.gridLayout.setObjectName("gridLayout")
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.ImageShowLineEdit = QtWidgets.QLineEdit(ImageShowWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.ImageShowLineEdit.sizePolicy().hasHeightForWidth())
		self.ImageShowLineEdit.setSizePolicy(sizePolicy)
		self.ImageShowLineEdit.setObjectName("ImageShowLineEdit")
		self.gridLayout_2.addWidget(self.ImageShowLineEdit, 0, 1, 1, 1)
		self.ImageShowSlider = QtWidgets.QSlider(ImageShowWidget)
		self.ImageShowSlider.setOrientation(QtCore.Qt.Horizontal)
		
		self.ImageShowSlider.setObjectName("ImageShowSlider")
		
		self.gridLayout_2.addWidget(self.ImageShowSlider, 0, 0, 1, 1)
		self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
		self.ImageShowGraphicsView = QtWidgets.QGraphicsView(ImageShowWidget)
		self.ImageShowGraphicsView.setObjectName("ImageShowGraphicsView")
		self.gridLayout.addWidget(self.ImageShowGraphicsView, 0, 0, 1, 2)

		self.retranslateUi(ImageShowWidget)
		QtCore.QMetaObject.connectSlotsByName(ImageShowWidget)

	def retranslateUi(self, ImageShowWidget):
		_translate = QtCore.QCoreApplication.translate
		ImageShowWidget.setWindowTitle(_translate("ImageShowWidget", "Image Show"))
		
		self.ImageShowSlider.setMinimum(0)
		numberofprojections, projection = getArray("/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo.h5", "/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo_dark_before.h5", "/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo_flats.h5")
		print(numberofprojections)
		self.ImageShowSlider.setMaximum(numberofprojections)
      
      
		self.ImageShowSlider.sliderMoved.connect(self.sliderMoved)
        
	def sliderMoved(self):
		numberofprojections, projection = getArray("/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo.h5", "/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo_dark_before.h5", "/mnt/DataDisk/Scripts/Pitch_Roll_BIC_Test/tomo_flats.h5")

		

		#self.ImageShowGraphicsView.setPixmap(projection)
		#print(numberofprojections)

        
        



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ImageShowWidget = QtWidgets.QWidget()
	ui = Ui_ImageShowWidget()
	ui.setupUi(ImageShowWidget)
	ImageShowWidget.show()
	sys.exit(app.exec_())

