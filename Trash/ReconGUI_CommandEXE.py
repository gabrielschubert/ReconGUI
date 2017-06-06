from PyQt5 import QtCore, QtGui, QtWidgets

### NEW IMPORTS ###
import os, subprocess


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setStyleSheet("background-color:rgb(234, 234, 234)")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.RunCommandButton = QtWidgets.QPushButton(self.centralwidget)
		self.RunCommandButton.setGeometry(QtCore.QRect(290, 260, 85, 27))
		self.RunCommandButton.setStyleSheet("")
		self.RunCommandButton.setObjectName("RunCommandButton")
		self.CommandLineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.CommandLineEdit.setGeometry(QtCore.QRect(390, 260, 113, 27))
		self.CommandLineEdit.setObjectName("CommandLineEdit")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		################ CONNECTIONS ###############

		self.RunCommandButton.clicked.connect(self.executeCommand)
		
		############################################
		
		
		
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.RunCommandButton.setText(_translate("MainWindow", "PushButton"))


	###################### ACTIONS ######################

	def executeCommand(self):
		print("Command Button Clicked, executing commands...")
		#cmd = self.CommandLineEdit.text()
		#os.system(cmd)
		os.system("python3 FolderDialog.py")
		print(cmd)
		

	def choosePath(self):
		cmd = "python3 FolderDialog.py"
		path = (subprocess.check_output(cmd, shell=True)).decode("utf-8")
		#print ("PATH!!!", path)
		#print (type(path))
		self.CommandLineEdit.setText(path)
		
	#####################################################

if __name__ == "__main__":
		import sys
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		ui = Ui_MainWindow()
		ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())

