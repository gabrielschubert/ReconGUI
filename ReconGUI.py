# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReconGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IMXReconGUI(object):
    def setupUi(self, IMXReconGUI):
        IMXReconGUI.setObjectName("IMXReconGUI")
        IMXReconGUI.resize(800, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainWindowIcon/Images/LNLS_logo_mini.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IMXReconGUI.setWindowIcon(icon)
        IMXReconGUI.setStyleSheet("background-color:rgb(234, 234, 234)")
        self.centralwidget = QtWidgets.QWidget(IMXReconGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 3, 3, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.StartSliceLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartSliceLabel.setObjectName("StartSliceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.StartSliceLabel)
        self.StartSliceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.StartSliceLineEdit.setObjectName("StartSliceLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.StartSliceLineEdit)
        self.FinalSliceLabel = QtWidgets.QLabel(self.centralwidget)
        self.FinalSliceLabel.setObjectName("FinalSliceLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.FinalSliceLabel)
        self.FinalSliceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FinalSliceLineEdit.setObjectName("FinalSliceLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.FinalSliceLineEdit)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.StartReconButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartReconButton.setObjectName("StartReconButton")
        self.horizontalLayout.addWidget(self.StartReconButton)
        self.StopReconButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopReconButton.setObjectName("StopReconButton")
        self.horizontalLayout.addWidget(self.StopReconButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CloseGuiButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseGuiButton.setObjectName("CloseGuiButton")
        self.gridLayout_2.addWidget(self.CloseGuiButton, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet("Base:rgb(0, 85, 255)")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.IMXGUINameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IMXGUINameLabel.setFont(font)
        self.IMXGUINameLabel.setAutoFillBackground(False)
        self.IMXGUINameLabel.setObjectName("IMXGUINameLabel")
        self.horizontalLayout_2.addWidget(self.IMXGUINameLabel)
        self.LNLSLogoImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.LNLSLogoImageLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LNLSLogoImageLabel.setText("")
        self.LNLSLogoImageLabel.setPixmap(QtGui.QPixmap(":/MainWindowIcon/Images/LNLS_logo_mini.jpg"))
        self.LNLSLogoImageLabel.setObjectName("LNLSLogoImageLabel")
        self.horizontalLayout_2.addWidget(self.LNLSLogoImageLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FilePathLabel = QtWidgets.QLabel(self.centralwidget)
        self.FilePathLabel.setObjectName("FilePathLabel")
        self.horizontalLayout_3.addWidget(self.FilePathLabel)
        self.FilePathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FilePathLineEdit.setEnabled(False)
        self.FilePathLineEdit.setObjectName("FilePathLineEdit")
        self.horizontalLayout_3.addWidget(self.FilePathLineEdit)
        self.FilePathChooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.FilePathChooseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/FolderIcon/Images/closed_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FilePathChooseButton.setIcon(icon1)
        self.FilePathChooseButton.setObjectName("FilePathChooseButton")
        self.horizontalLayout_3.addWidget(self.FilePathChooseButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 4)
        IMXReconGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IMXReconGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 27))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        IMXReconGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IMXReconGUI)
        self.statusbar.setObjectName("statusbar")
        IMXReconGUI.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(IMXReconGUI)
        self.actionVersion.setObjectName("actionVersion")
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(IMXReconGUI)
        self.CloseGuiButton.clicked.connect(IMXReconGUI.close)
        self.StartReconButton.clicked.connect(self.progressBar.show)
        QtCore.QMetaObject.connectSlotsByName(IMXReconGUI)

    def retranslateUi(self, IMXReconGUI):
        _translate = QtCore.QCoreApplication.translate
        IMXReconGUI.setWindowTitle(_translate("IMXReconGUI", "IMX Recon GUI"))
        self.label.setText(_translate("IMXReconGUI", "Theshold"))
        self.label_2.setText(_translate("IMXReconGUI", "Rotation Shift"))
        self.StartSliceLabel.setText(_translate("IMXReconGUI", "Start Slice"))
        self.FinalSliceLabel.setText(_translate("IMXReconGUI", "Final Slice"))
        self.StartReconButton.setText(_translate("IMXReconGUI", "Start Recon"))
        self.StopReconButton.setText(_translate("IMXReconGUI", "Stop Recon"))
        self.CloseGuiButton.setText(_translate("IMXReconGUI", "Close"))
        self.IMXGUINameLabel.setText(_translate("IMXReconGUI", "IMX Tomography Reconstruction User Interface"))
        self.FilePathLabel.setText(_translate("IMXReconGUI", "File Path"))
        self.menuAbout.setTitle(_translate("IMXReconGUI", "About"))
        self.actionVersion.setText(_translate("IMXReconGUI", "Version"))



        ############### CONNECTIONS ###############

        self.FilePathChooseButton.clicked.connect(self.choosePath)
		
		############################################


    ###################### ACTIONS ######################

    def choosePath(self):
		
        cmd = "python3 Functions/FolderDialog.py"
        path = (subprocess.check_output(cmd, shell=True)).decode("utf-8")
        #print ("PATH!!!", path)
        #print (type(path))
        self.FilePathLineEdit.setText(path)




import subprocess
import ReconGUIResource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IMXReconGUI = QtWidgets.QMainWindow()
    ui = Ui_IMXReconGUI()
    ui.setupUi(IMXReconGUI)
    IMXReconGUI.show()
    sys.exit(app.exec_())

