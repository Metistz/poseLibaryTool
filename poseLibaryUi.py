
try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds  
import importlib
import os
from . import poseLibaryUtil as poseUtil
importlib.reload(poseUtil)

class poseLibaryTool(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.pose_library = {}

		self.setWindowTitle('POSE LIBARY')
		self.resize(600,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.mainLayout.setContentsMargins(30, 20, 30, 20)
		self.mainLayout.setSpacing(15)

		#ใส่ชื่อpose
		self.name_layout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.name_layout)
		self.setStyleSheet("""
		QDialog{
			background: qlineargradient(
				x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0 #060e1f, stop:0.5 #344483, stop: 1 #344483
			);
		}
		""")

		self.pose_name_enter = QtWidgets.QLineEdit()
		self.pose_name_enter.setPlaceholderText("Enter pose name")
		self.pose_name_enter.setStyleSheet(
			'''
			QLineEdit {
				background-color: #919de6;
				border: 1px solid #ccc;
				border-radius: 4px;
				color: black;
				padding: 4px;
			}
			'''
		)

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
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6d597a, stop:0.5 #e56b6f, stop:1 #eaac8b);
				}
				QPushButton:pressed {
					background-color: white;
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
				background-color: #636b99;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: white;
			}
			'''
		)

		self.suffix_name_enter = QtWidgets.QLineEdit()
		self.suffix_name_enter.setPlaceholderText("Suffix...")
		self.suffix_name_enter.setStyleSheet(
			'''
			QLineEdit {
				background-color: #636b99;
				border: 1px solid #ccc;
				border-radius: 4px;
				padding: 4px;
				color: white;
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

		self.load_button = QtWidgets.QPushButton('LOAD POSE')
		self.button_layout.addWidget(self.load_button)
		self.load_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #9b80c6, stop:0.5 #e690ec, stop:1 #fa578e);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
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
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #40798c, stop:0.5 #70a9a1, stop:1 #9ec1a3);
				}
				QPushButton:pressed {
					background-color: white;
				}
			'''
		)

		self.rename_button = QtWidgets.QPushButton('RENAME POSE')
		self.button_layout.addWidget(self.rename_button)
		self.rename_button.clicked.connect(self.renamePose)
		self.rename_button.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #dcd48c, stop:0.5 #ebc570, stop:1 #fa9357);
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
					background-color: white;
				}
			'''
		)

		# scrollable 
		self.pose_list.setIconSize(QtCore.QSize(150,150))
		self.pose_list.setGridSize(QtCore.QSize(160, 180))  
		self.pose_list.setResizeMode(QtWidgets.QListView.Adjust)
		self.pose_list.setViewMode(QtWidgets.QListView.IconMode)  
		self.pose_list.setMovement(QtWidgets.QListView.Static)    
		self.pose_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.pose_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.pose_list.setStyleSheet('''
			QListWidget {
				background-color: #f7eac1;
				color: #2a2a57;   
				font-size: 10pt;
				font-family: "Arial";
			}
			QListWidget::item:selected {
				background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #CD2C58, stop:0.5 #E06B80, stop:1 #FFC69D);
				color: #fff5d9;
			}
		''')

		self.import_img_btn = QtWidgets.QPushButton("IMPORT IMAGE")
		self.mainLayout.addWidget(self.import_img_btn)
		self.import_img_btn.setStyleSheet(
			'''
				QPushButton {
					background-color:  qlineargradient(x1:0, y1:0, x2:1, y2:0,
					stop:0 #feb852, stop:0.5 #917cb6, stop:1 #789fe5);
					border-radius: 10px;
					font-size: 12px;
					font-family: Arial;
					color: black;
					padding: 8px;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6d597a, stop:0.5 #e56b6f, stop:1 #eaac8b);
				}
				QPushButton:pressed {
					background-color: white;
				}
			'''
		)

		self.import_img_btn.clicked.connect(self.import_image)

		self.savePose_button.clicked.connect(self.savePose)
		self.load_button.clicked.connect(self.loadPose)

		self.selected_image_path = None 

	def savePose(self):
		poseUtil.save_pose(self)


	def import_image(self):
		file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
			self,
			"select Picture",
			"",
			"Image Files (*.png *.jpg *.jpeg *.bmp)"
		)
		if file_path:
			self.selected_image_path = file_path
			current_item = self.pose_list.currentItem()
			if current_item:
				pixmap = QtGui.QPixmap(file_path)
				icon = QtGui.QIcon(pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
				current_item.setIcon(icon)
				current_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

	def loadPose(self):
		poseUtil.load_pose(self)

	def deletePose(self):
		poseUtil.delete_pose(self)

	def renamePose(self):
		item = self.pose_list.currentItem()
		if not item:
			cmds.warning("Please select a pose to rename.")
			return

		old_name = item.text()

		re_dialog = QtWidgets.QDialog(self)
		re_dialog.setWindowTitle("RENAME POSE")
		re_dialog.resize(250, 140)

		re_layout = QtWidgets.QVBoxLayout(re_dialog)

		re_lineEdit = QtWidgets.QLineEdit()
		re_lineEdit.setPlaceholderText(f"Enter new name for '{old_name}'")
		re_layout.addWidget(re_lineEdit)

		button_layout = QtWidgets.QHBoxLayout()
		confirm_rename_btn = QtWidgets.QPushButton("RENAME")
		cancel_button = QtWidgets.QPushButton("CANCEL")

		button_layout.addWidget(confirm_rename_btn)
		button_layout.addWidget(cancel_button)
		re_layout.addLayout(button_layout)

		def confirmRename():
			new_name = re_lineEdit.text().strip()
			if not new_name:
				cmds.warning("Please enter a new pose name.")
				return

			if new_name in self.pose_library and new_name != old_name:
				QtWidgets.QMessageBox.warning(
					self,
					"Duplicate Name",
					f"Pose '{new_name}' already exists!"
				)
				return

			self.pose_library[new_name] = self.pose_library.pop(old_name)

			item.setText(new_name)
			re_dialog.close()

			cmds.inViewMessage(
				amg=f"Pose renamed to <hl>{new_name}</hl>",
				pos="midCenter",
				fade=True
			)

		confirm_rename_btn.clicked.connect(confirmRename)
		cancel_button.clicked.connect(re_dialog.close)

		re_dialog.exec_()


def run():
	global ui
	try:
		ui.close()
		ui.deleteLater()
	except:
		pass

	mayaMainWindow = omui.MQtUtil.mainWindow()
	ptr = wrapInstance(int(mayaMainWindow), QtWidgets.QWidget)
	ui = poseLibaryTool(parent=ptr)
	ui.show()