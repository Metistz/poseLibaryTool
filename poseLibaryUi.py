try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import importlib
import os


class poseLibaryTool(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Pose Libary')
		self.resize(500,400)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		#ใส่ชื่อpose
		self.name_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.name_layout)
		self.setStyleSheet(
			'''
			QDialog {
				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
				stop:0 #282443, stop:1 #2d276f, stop:2 #344483);
			}
			'''
		)



		self.pose_name_enter = QtWidgets.QLineEdit()
		self.pose_name_enter.setPlaceholderText("Enter pose name")
		self.pose_name_enter.setStyleSheet(
			'''
			QLineEdit {
				background-color: ##789fe5;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: black;
			}
			'''
		)


		self.savePose_button = QtWidgets.QPushButton("Save Pose")
		self.savePose_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #feb852, stop:1 #917cb6, stop:2 #789fe5);
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
		)
		self.name_layout.addWidget(self.pose_name_enter)
		self.name_layout.addWidget(self.savePose_button)

		#ใส่ชื่อ prefix suffix 
		self.preSufLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.preSufLayout)
		self.prefix_name_enter = QtWidgets.QLineEdit()
		self.prefix_name_enter.setPlaceholderText("Prefix...")
		self.prefix_name_enter.setStyleSheet(
			'''
			QLineEdit {
				background-color: ##789fe5;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: black;
			}
			'''
		)


		self.suffix_name_enter = QtWidgets.QLineEdit()
		self.suffix_name_enter.setPlaceholderText("Suffix...")
		self.suffix_name_enter.setStyleSheet(
			'''
			QLineEdit {
				background-color: ##789fe5;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: black;
			}
			'''
		)

		
		self.preSufLayout.addWidget(self.prefix_name_enter)
		self.preSufLayout.addWidget(self.suffix_name_enter)

		#list pose
		self.pose_list = QtWidgets.QListWidget()
		self.mainLayout.addWidget(self.pose_list)
		self.pose_list.setStyleSheet('background-color: #ece2d6;')
		#เรียงชื่อตามตัวอักษร
		self.pose_list.setSortingEnabled(True)

		#button
		self.button_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.button_layout)

		self.load_button = QtWidgets.QPushButton('Load Pose')
		self.button_layout.addWidget(self.load_button)
		self.load_button.clicked.connect(self.loadPose)
		self.load_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #9b80c6, stop:1 #e690ec, stop:2 #f17a9f);
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
		)
		self.deleate_button = QtWidgets.QPushButton('Deleate Pose')
		self.button_layout.addWidget(self.deleate_button)
		self.deleate_button.clicked.connect(self.deleatePose)
		self.deleate_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #819fd5, stop:1 #6fbeea, stop:2 #6bded2);
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
		)

		self.rename_button = QtWidgets.QPushButton('Rename Pose')
		self.button_layout.addWidget(self.rename_button)
		self.rename_button.clicked.connect(self.renamePose)
		self.rename_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #dcd48c, stop:1 #ebc570, stop:2 #efac68);
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
		)


	def savePose(self):
		pass

	def loadPose(self):
		pass

	def deleatePose(self):
		pass

	def renamePose(self):
		pass

def run():
	global ui
	try:
		ui.close()
	except:
		pass

mayaMainWindow = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(mayaMainWindow), QtWidgets.QWidget)
ui = poseLibaryTool(parent=ptr)
ui.show()





