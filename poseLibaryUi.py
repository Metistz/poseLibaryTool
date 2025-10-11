try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import importlib
import os
<<<<<<< HEAD

=======
ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/poseLibaryTool'
>>>>>>> e10144e (Update styleSheet)

class poseLibaryTool(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

<<<<<<< HEAD
		self.setWindowTitle('Pose Libary')
=======
		self.setWindowTitle('POSE LIBARY')
>>>>>>> e10144e (Update styleSheet)
		self.resize(500,400)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
<<<<<<< HEAD
=======
		self.mainLayout.setContentsMargins(30, 20, 30, 20)
		self.mainLayout.setSpacing(15)


>>>>>>> e10144e (Update styleSheet)

		#ใส่ชื่อpose
		self.name_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.name_layout)
<<<<<<< HEAD
		self.setStyleSheet(
			'''
			QDialog {
				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
				stop:0 #282443, stop:1 #2d276f, stop:2 #344483);
			}
			'''
		)
=======
		self.setStyleSheet("""
		QDialog {
			background: qlineargradient(
				x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0 #060e1f, stop:0.5 #344483, stop: 1 #344483
			);
			self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image.jpg")
			background-repeat: no-repeat;
			background-position: center;
			background-origin: content;
			}
		""")

>>>>>>> e10144e (Update styleSheet)



		self.pose_name_enter = QtWidgets.QLineEdit()
		self.pose_name_enter.setPlaceholderText("Enter pose name")
		self.pose_name_enter.setStyleSheet(
			'''
			QLineEdit {
<<<<<<< HEAD
				background-color: #3d5f9c;
				border: 1px solid #ccc;
				border-radius: 4px;
=======
				background-color: #919de6;
				border: 1px solid #ccc;
				border-radius: 4px;
				color: black;
>>>>>>> e10144e (Update styleSheet)
				padding: 4px;
			}
			'''
		)


<<<<<<< HEAD
		self.savePose_button = QtWidgets.QPushButton("Save Pose")
		self.savePose_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #feb852, stop:1 #917cb6, stop:2 #789fe5);
					border-radius: 10px;
					font-size: 16px;
=======
		self.savePose_button = QtWidgets.QPushButton("SAVE POSE")
		self.savePose_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #feb852, stop:0.5 #917cb6, stop:1 #789fe5);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
>>>>>>> e10144e (Update styleSheet)
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
<<<<<<< HEAD
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
=======
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6d597a, stop:0.5 #e56b6f, stop:1 #eaac8b);
				}
				QPushButton:pressed {
					background-color: white;
>>>>>>> e10144e (Update styleSheet)
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
<<<<<<< HEAD
				background-color: #abb2d6;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: black;
=======
				background-color: #636b99;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: white;
>>>>>>> e10144e (Update styleSheet)
			}
			'''
		)


		self.suffix_name_enter = QtWidgets.QLineEdit()
		self.suffix_name_enter.setPlaceholderText("Suffix...")
		self.suffix_name_enter.setStyleSheet(
			'''
			QLineEdit {
<<<<<<< HEAD
				background-color: #aeafe6;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: black;
=======
				background-color: #636b99;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: white;
>>>>>>> e10144e (Update styleSheet)
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

<<<<<<< HEAD
		self.load_button = QtWidgets.QPushButton('Load Pose')
=======
		self.load_button = QtWidgets.QPushButton('LOAD POSE')
>>>>>>> e10144e (Update styleSheet)
		self.button_layout.addWidget(self.load_button)
		self.load_button.clicked.connect(self.loadPose)
		self.load_button.setStyleSheet(
			'''
				QPushButton {
<<<<<<< HEAD
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #9b80c6, stop:1 #e690ec, stop:2 #f17a9f);
					border-radius: 10px;
					font-size: 16px;
=======
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #9b80c6, stop:0.5 #e690ec, stop:1 #fa578e);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
>>>>>>> e10144e (Update styleSheet)
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
<<<<<<< HEAD
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
=======
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ffc8dd, stop:0.5 #bde0fe, stop:1 #a2d2ff);
				}
				QPushButton:pressed {
					background-color: white;
				}
			'''
		)
		self.delete_button = QtWidgets.QPushButton('DELETE POSE')
		self.button_layout.addWidget(self.delete_button)
		self.delete_button.clicked.connect(self.deletePose)
		self.delete_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #819fd5, stop:0.5 #6fbeea, stop:1 #57fae2);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
>>>>>>> e10144e (Update styleSheet)
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
<<<<<<< HEAD
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
=======
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #40798c, stop:0.5 #70a9a1, stop:1 #9ec1a3);
				}
				QPushButton:pressed {
					background-color: white;
>>>>>>> e10144e (Update styleSheet)
				}
			'''
		)

<<<<<<< HEAD
		self.rename_button = QtWidgets.QPushButton('Rename Pose')
=======
		self.rename_button = QtWidgets.QPushButton('RENAME POSE')
>>>>>>> e10144e (Update styleSheet)
		self.button_layout.addWidget(self.rename_button)
		self.rename_button.clicked.connect(self.renamePose)
		self.rename_button.setStyleSheet(
			'''
				QPushButton {
<<<<<<< HEAD
					background-color:  qlineargradient(x1:0, y1:0, x2:0, y2:1,
					stop:0 #dcd48c, stop:1 #ebc570, stop:2 #efac68);
					border-radius: 10px;
					font-size: 16px;
=======
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #dcd48c, stop:0.5 #ebc570, stop:1 #fa9357);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
>>>>>>> e10144e (Update styleSheet)
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
<<<<<<< HEAD
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: navy;
=======
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f8ad9d, stop:0.5 #fbc4ab, stop:1 #ffdab9);
				}
				QPushButton:pressed {
					background-color: white;
>>>>>>> e10144e (Update styleSheet)
				}
			'''
		)


	def savePose(self):
		pass

	def loadPose(self):
		pass

<<<<<<< HEAD
	def deleatePose(self):
		pass

	def renamePose(self):
		pass
=======
	def deletePose(self):
		pass

	def renamePose(self):
		self.re_dialog = QtWidgets.QDialog(self)
		self.re_dialog.setWindowTitle("RENAME POSE")
		self.re_dialog.resize(250, 140)

		self.re_layout = QtWidgets.QVBoxLayout(self.re_dialog)

		self.re_lineEdit = QtWidgets.QLineEdit()
		self.re_lineEdit.setPlaceholderText("Enter new pose name...")
		self.re_layout.addWidget(self.re_lineEdit)

		button_layout = QtWidgets.QHBoxLayout()

		self.rename_button = QtWidgets.QPushButton("RENAME")
		self.cancel_button = QtWidgets.QPushButton("CANCEL")

		button_layout.addWidget(self.rename_button)
		button_layout.addWidget(self.cancel_button)

		self.re_layout.addLayout(button_layout)

		self.re_dialog.setStyleSheet("""
			QDialog {
				background: qlineargradient(
					x1: 0, y1: 0, x2: 1, y2: 1,
					stop: 0 #282443,
					stop: 0.5 #2d276f,
					stop: 1 #344483
				);
				border: 2px solid #917cb6;
				border-radius: 12px;
			}

			QLineEdit {
				background-color: #ece2d6;
				border-radius: 6px;
				padding: 6px;
				font-family: "Segoe UI";
				font-size: 14px;
				color: black;
			}

		""")

		self.rename_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #e7c6ff, stop:0.5 #c8b6ff, stop:1 #bbd0ff);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f8ad9d, stop:0.5 #fbc4ab, stop:1 #ffdab9);
				}
				QPushButton:pressed {
					background-color: black;
					color: white;
				}
			'''
		)
		self.cancel_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #ff86c8, stop:0.5 #ffa3a5, stop:1 #bbd0ff);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f8ad9d, stop:0.5 #fbc4ab, stop:1 #ffdab9);
				}
				QPushButton:pressed {
					background-color: black;
					color: white;
				}
			'''
		)



		self.re_dialog.exec_()

>>>>>>> e10144e (Update styleSheet)

def run():
	global ui
	try:
		ui.close()
<<<<<<< HEAD
	except:
		pass

mayaMainWindow = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(mayaMainWindow), QtWidgets.QWidget)
ui = poseLibaryTool(parent=ptr)
ui.show()


=======
		ui.deleteLater()
	except:
		pass

	mayaMainWindow = omui.MQtUtil.mainWindow()
	ptr = wrapInstance(int(mayaMainWindow), QtWidgets.QWidget)
	ui = poseLibaryTool(parent=ptr)
	ui.show()
>>>>>>> e10144e (Update styleSheet)



