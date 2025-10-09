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
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		#ใส่ชื่อpose
		self.name_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.name_layout)

		self.pose_name_enter = QtWidgets.QLineEdit()
		self.pose_name_enter.setPlaceholderText("Enter pose name")
		self.buttonSavePose = QtWidgets.QPushButton("Save Pose")
		self.name_layout.addWidget(self.pose_name_enter)
		self.name_layout.addWidget(self.buttonSavePose)

		#ใส่ชื่อ prefix suffix 
		self.preSufLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.preSufLayout)
		self.prefix_name_enter = QtWidgets.QLineEdit()
		self.prefix_name_enter.setPlaceholderText("Prefix...")

		self.suffix_name_enter = QtWidgets.QLineEdit()
		self.suffix_name_enter.setPlaceholderText("Suffix...")
		
		self.preSufLayout.addWidget(self.prefix_name_enter)
		self.preSufLayout.addWidget(self.suffix_name_enter)

		#list pose
		self.pose_list = QtWidgets.QListWidget()
		self.mainLayout.addWidget(self.pose_list)
		#เรียงชื่อตามตัวอักษร
		self.pose_list.setSortingEnabled(True)

		#button
		self.button_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.button_layout)

		self.load_button = QtWidgets.QPushButton('Load Pose')
		self.button_layout.addWidget(self.load_button)
		self.load_button.clicked.connect(self.loadPose)

		self.deleate_button = QtWidgets.QPushButton('Deleate Pose')
		self.button_layout.addWidget(self.deleate_button)
		self.deleate_button.clicked.connect(self.deleatePose)

		self.rename_button = QtWidgets.QPushButton('Rename Pose')
		self.button_layout.addWidget(self.rename_button)
		self.rename_button.clicked.connect(self.renamePose)


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