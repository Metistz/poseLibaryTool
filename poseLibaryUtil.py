try:
	from PySide6 import QtCore, QtGui, QtWidgets
except:
	from PySide2 import QtCore, QtGui, QtWidgets

import maya.cmds as cmds


def save_pose(self):
	pose_name = self.pose_name_enter.text().strip()
	prefix = self.prefix_name_enter.text().strip()
	suffix = self.suffix_name_enter.text().strip()

	if not pose_name:
		cmds.warning("Please enter a pose name.")
		return

	full_name = f"{prefix}_{pose_name}_{suffix}".strip("_")
	selected = cmds.ls(sl=True)
	if not selected:
		cmds.warning("Please select controls or joints to save pose.")
		return

	if full_name in self.pose_library:
		reply = QtWidgets.QMessageBox.question(
			self,
			"Pose Already Exists",
			f"Pose '{full_name}' already exists. Overwrite?",
			QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
		)
		if reply == QtWidgets.QMessageBox.No:
			return

		items = self.pose_list.findItems(full_name, QtCore.Qt.MatchExactly)
		for item in items:
			row = self.pose_list.row(item)
			self.pose_list.takeItem(row)

	pose_data = {}
	for obj in selected:
		if cmds.objExists(obj):
			attrs = {}
			for attr in ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]:
				if cmds.attributeQuery(attr, node=obj, exists=True):
					attrs[attr] = cmds.getAttr(f"{obj}.{attr}")
			pose_data[obj] = attrs

	self.pose_library[full_name] = pose_data

	item = QtWidgets.QListWidgetItem(full_name)
	item.setForeground(QtGui.QColor("#2d276f"))
	self.pose_list.addItem(item)

	cmds.inViewMessage(amg=f"Pose <hl>{full_name}</hl> saved!", pos="midCenter", fade=True)



def clear_pose(self, pose_name):

	if pose_name not in self.pose_library:
		  return
	for obj in self.pose_library[pose_name]:
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
		cmds.warning("Please select a pose to load.")
		return

	pose_name = item.text()
	if pose_name not in self.pose_library:
		cmds.warning(f"Pose '{pose_name}' not found in library.")
		return

	for obj, attrs in self.pose_library[pose_name].items():
		if cmds.objExists(obj):
			for attr, value in attrs.items():
				if cmds.getAttr(f"{obj}.{attr}", settable=True):
					cmds.setAttr(f"{obj}.{attr}", value)

	cmds.inViewMessage(amg=f"Pose <hl>{pose_name}</hl> loaded!", pos="midCenter", fade=True)



def delete_pose(self):

	item = self.pose_list.currentItem()

	pose_name = item.text()
	if pose_name in self.pose_library:
		del self.pose_library[pose_name]

	self.pose_list.takeItem(self.pose_list.row(item))
	cmds.inViewMessage(amg=f"Pose <hl>{pose_name}</hl> deleted!", pos="midCenter", fade=True)


def rename_pose(self, new_name=None):
	
	item = self.pose_list.currentItem()
	if not item:
		cmds.warning("Please select a pose to rename.")
		return

	old_name = item.text()

	if new_name is None:
		new_name, ok = QtWidgets.QInputDialog.getText(
			self, "Rename Pose", f"Enter new name for '{old_name}':"
		)
		if not ok or not new_name.strip():
			return
		new_name = new_name.strip()
	else:
		new_name = new_name.strip()
		if not new_name:
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

	cmds.inViewMessage(
	amg=f"Pose renamed to <hl>{new_name}</hl>",
	pos="midCenter",
	fade=True
	)


