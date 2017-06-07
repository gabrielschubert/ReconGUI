# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageShowSlider.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.ImageShowGraphicsView = ImageView(ImageShowWidget)
        self.ImageShowGraphicsView.setObjectName("ImageShowGraphicsView")
        self.gridLayout.addWidget(self.ImageShowGraphicsView, 0, 0, 1, 2)

        self.retranslateUi(ImageShowWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageShowWidget)

    def retranslateUi(self, ImageShowWidget):
        _translate = QtCore.QCoreApplication.translate
        ImageShowWidget.setWindowTitle(_translate("ImageShowWidget", "Image Show"))
        ImageShowWidget.setImage(data)

from pyqtgraph import ImageView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageShowWidget = QtWidgets.QWidget()
    ui = Ui_ImageShowWidget()
    ui.setupUi(ImageShowWidget)
    ImageShowWidget.show()
    sys.exit(app.exec_())

