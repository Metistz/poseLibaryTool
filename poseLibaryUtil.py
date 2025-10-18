<<<<<<< HEAD
try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from PySide2 import QtCore, QtGui, QtWidgets

import maya.cmds as cmds


def save_pose(self):
    base_name = self.pose_name_enter.text().strip()
    prefix = self.prefix_enter.text().strip()
    suffix = self.suffix_enter.text().strip()

    if not base_name:
        cmds.warning("กรุณาใส่ชื่อ pose")
        return

    sel = cmds.ls(selection=True)
    if not sel:
        cmds.warning("กรุณาเลือก object/joint ก่อน save pose")
        return

    pose_name = f"{prefix}{base_name}{suffix}"

    PoseLibraryUI.pose_library[pose_name] = {}

    for obj in sel:
        obj_data = {}
        if cmds.nodeType(obj) == "joint":
            obj_data["t"] = cmds.getAttr(obj + ".translate")[0]
            obj_data["r"] = cmds.getAttr(obj + ".rotate")[0]
            obj_data["s"] = cmds.getAttr(obj + ".scale")[0]
            obj_data["jo"] = cmds.getAttr(obj + ".jointOrient")[0]
        else:
            if cmds.getAttr(obj + ".translate", settable=True):
                obj_data["t"] = cmds.getAttr(obj + ".translate")[0]
            if cmds.getAttr(obj + ".rotate", settable=True):
                obj_data["r"] = cmds.getAttr(obj + ".rotate")[0]
            if cmds.getAttr(obj + ".scale", settable=True):
                obj_data["s"] = cmds.getAttr(obj + ".scale")[0]

        PoseLibraryUI.pose_library[pose_name][obj] = obj_data

    if not self.pose_list.findItems(pose_name, QtCore.Qt.MatchExactly):
        self.pose_list.addItem(pose_name)
        self.pose_list.sortItems()  

    self.pose_name_enter.clear()


    cmds.inViewMessage(
        amg=f"Pose <hl>{pose_name}</hl> saved (overwritten if existed)!",
        pos="midCenter",
        fade=True
    )


def clear_pose(self, pose_name):
    if pose_name not in PoseLibraryUI.pose_library:
        return
    for obj in PoseLibraryUI.pose_library[pose_name]:
        if cmds.objExists(obj):
            if cmds.attributeQuery("translate", node=obj, exists=True):
                cmds.setAttr(obj + ".translate", 0, 0, 0)
            if cmds.attributeQuery("rotate", node=obj, exists=True):
                cmds.setAttr(obj + ".rotate", 0, 0, 0)
            if cmds.attributeQuery("scale", node=obj, exists=True):
                cmds.setAttr(obj + ".scale", 1, 1, 1)
            if cmds.nodeType(obj) == "joint" and cmds.attributeQuery("jointOrient", node=obj, exists=True):
                cmds.setAttr(obj + ".jointOrient", 0, 0, 0)


def load_pose(self):
    item = self.pose_list.currentItem()
    if not item:
        cmds.warning("กรุณาเลือก pose ก่อนโหลด")
        return

    pose_name = item.text()
    self.clear_pose(pose_name)

    for obj, attrs in PoseLibraryUI.pose_library[pose_name].items():
        if cmds.objExists(obj):
            if "t" in attrs: cmds.setAttr(obj + ".translate", *attrs["t"])
            if "r" in attrs: cmds.setAttr(obj + ".rotate", *attrs["r"])
            if "s" in attrs: cmds.setAttr(obj + ".scale", *attrs["s"])
            if "jo" in attrs and cmds.nodeType(obj) == "joint":
                cmds.setAttr(obj + ".jointOrient", *attrs["jo"])

    cmds.inViewMessage(amg=f"Pose <hl>{pose_name}</hl> loaded!", pos="midCenter", fade=True)


def delete_pose(self):
    item = self.pose_list.currentItem()
    if not item:
        cmds.warning("กรุณาเลือก pose ก่อนลบ")
        return

    pose_name = item.text()
    if pose_name in PoseLibraryUI.pose_library:
        del PoseLibraryUI.pose_library[pose_name]

    self.pose_list.takeItem(self.pose_list.row(item))
    cmds.inViewMessage(amg=f"Pose <hl>{pose_name}</hl> deleted!", pos="midCenter", fade=True)


def rename_pose(self):

    item = self.pose_list.currentItem()
    if not item:
        cmds.warning("กรุณาเลือก pose ก่อนเปลี่ยนชื่อ")
        return

    old_name = item.text()
    new_name, ok = QtWidgets.QInputDialog.getText(
        self, "Rename Pose", f"Enter new name for '{old_name}':"
    )

    if ok and new_name.strip():
        new_name = new_name.strip()
        PoseLibraryUI.pose_library[new_name] = PoseLibraryUI.pose_library.pop(old_name)
        item.setText(new_name)
        self.pose_list.sortItems()
        cmds.inViewMessage(amg=f"Pose renamed to <hl>{new_name}</hl>", pos="midCenter", fade=True)
=======
def import_image():
	self.pose_list = QtWidgets.QListWidget()
	self.mainLayout.addWidget(self.pose_list)
	self.pose_list.setStyleSheet('background-color: #ece2d6;')
	self.pose_list.setSortingEnabled(True)
	self.pose_list.setIconSize(QtCore.QSize(80, 80))
	self.pose_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
	self.pose_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

	# ลบปุ่ม import image เดิม
	# self.import_img_btn = QtWidgets.QPushButton("IMPORT IMAGE")
	# self.mainLayout.addWidget(self.import_img_btn)
	# self.import_img_btn.clicked.connect(self.import_image)

	# เชื่อมสัญญาณ double click กับ list item
	self.pose_list.itemDoubleClicked.connect(self.import_image_for_item)

	self.savePose_button.clicked.connect(self.savePose)
	self.load_button.clicked.connect(self.loadPose)

	self.selected_image_path = None

def savePose(self):
	pose_name = self.pose_name_enter.text().strip()
	prefix = self.prefix_name_enter.text().strip()
	suffix = self.suffix_name_enter.text().strip()
	if not pose_name:
		QtWidgets.QMessageBox.warning(self, "Warning", "Please enter a pose name")
		return

	final_name = f"{prefix}{pose_name}{suffix}"
	if final_name not in self.pose_library:
		item = QtWidgets.QListWidgetItem(final_name)
		# ใส่ไอคอนถ้ามีการเลือกภาพก่อนบันทึก
		if self.selected_image_path:
			item.setIcon(QtGui.QIcon(self.selected_image_path))
		self.pose_list.addItem(item)
		self.pose_library[final_name] = {"image": self.selected_image_path}
	else:
		QtWidgets.QMessageBox.warning(self, "Warning", "Pose name already exists!")

	# เคลียร์ช่องใส่ชื่อและรูป
	self.pose_name_enter.clear()
	self.selected_image_path = None

def import_image_for_item(self, item):
	# เปิด dialog เลือกรูป
	file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
		self,
		"เลือกภาพสำหรับ Pose",
		"",
		"Image Files (*.png *.jpg *.jpeg *.bmp)"
	)
	if file_path:
		self.selected_image_path = file_path
		item.setIcon(QtGui.QIcon(file_path))
		pose_name = item.text()
		self.pose_library[pose_name] = {"image": file_path}





# def savePose(self):
# 	base_name = self.pose_name_enter.text().strip()
# 	prefix = self.prefix_name_enter.text().strip()
# 	suffix = self.suffix_name_enter.text().strip()

# 	sel = cmds.ls(selection=True)
# 	if not sel:
# 		cmds.warning("No objects selected!")
# 		return

# 	pose_name = f'{prefix}{base_name}{suffix}'

# 	msg_box = None
# 	yes_button = None

# 	# เช็ค overwrite
# 	if pose_name in PoseLibraryUI.pose_library:
# 		msg_box = QtWidgets.QMessageBox(self)
# 		msg_box.setWindowTitle("Confirm overwrite")
# 		msg_box.setText(f"Pose '{pose_name}' already exists.\nDo you want to overwrite?")
# 		msg_box.setIcon(QtWidgets.QMessageBox.Warning)
# 		yes_button = msg_box.addButton("Yes", QtWidgets.QMessageBox.YesRole)
# 		no_button = msg_box.addButton("No", QtWidgets.QMessageBox.NoRole)
# 		msg_box.exec()

# 		if msg_box.clickedButton() != yes_button:
# 			return  # ยกเลิก save ถ้าไม่ใช่ yes

# 	# บันทึกข้อมูล pose
# 	PoseLibraryUI.pose_library[pose_name] = {}
# 	for obj in sel:
# 		obj_data = {}
# 		node_type = cmds.nodeType(obj)
# 		if node_type == 'joint':
# 			obj_data['t'] = cmds.getAttr(obj + '.translate')[0]
# 			obj_data['r'] = cmds.getAttr(obj + '.rotate')[0]
# 			obj_data['s'] = cmds.getAttr(obj + '.scale')[0]
# 			obj_data['jo'] = cmds.getAttr(obj + '.jointOrient')[0]
# 		else:
# 			if cmds.getAttr(obj + '.translate', settable=True):
# 				obj_data['t'] = cmds.getAttr(obj + '.translate')[0]
# 			if cmds.getAttr(obj + '.rotate', settable=True):
# 				obj_data['r'] = cmds.getAttr(obj + '.rotate')[0]
# 			if cmds.getAttr(obj + '.scale', settable=True):
# 				obj_data['s'] = cmds.getAttr(obj + '.scale')[0]

# 		PoseLibraryUI.pose_library[pose_name][obj] = obj_data

# 	# เพิ่มรูปภาพถ้ามี
# 	if self.selected_image_path:
# 		PoseLibraryUI.pose_library[pose_name]["image"] = self.selected_image_path

# 		item = QtWidgets.QListWidgetItem(pose_name)
# 	if self.selected_image_path and os.path.exists(self.selected_image_path):
# 		item.setIcon(QtGui.QIcon(self.selected_image_path))
# 	else:
# 		item.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))
# 	self.pose_list.addItem(item)
# 	self.pose_list.sortItems()

# 	# เพิ่มใน list widget
# 	if not self.pose_list.findItems(pose_name, QtCore.Qt.MatchExactly):
# 		item = QtWidgets.QListWidgetItem(pose_name)
# 		if self.selected_image_path and os.path.exists(self.selected_image_path):
# 			icon = QtGui.QIcon(self.selected_image_path)
# 			item.setIcon(icon)
# 		else:
# 			item.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))

# 		item.setTextAlignment(QtCore.Qt.AlignHCenter)
# 		self.pose_list.addItem(item)
# 		self.pose_list.sortItems()  # เรียงชื่ออัตโนมัติ

# 	# รีเซ็ตค่า
# 	self.selected_image_path = None
# 	cmds.inViewMessage(amg=f"Save Pose: <hl>{pose_name}</hl>", pos="botLeft", fade=True)


# def refreshPoseList(self):
# 	self.pose_list.clear()
# 	for pose_name, data in PoseLibraryUI.pose_library.items():
# 		item = QtWidgets.QListWidgetItem(pose_name)
# 		if 'image' in data and os.path.exists(data['image']):
# 			icon = QtGui.QIcon(data['image'])
# 			item.setIcon(icon)
# 		else:
# 			item.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))

# 		item.setTextAlignment(QtCore.Qt.AlignHCenter)
# 		self.pose_list.addItem(item)
>>>>>>> 71757d7d67d936638092085d5abe6a50dc1c7a6c
