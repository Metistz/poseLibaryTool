try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from PySide2 import QtCore, QtGui, QtWidgets

import maya.cmds as cmds


def save_pose(self):
    base_name = self.pose_name_enter.text().strip()
    prefix = self.prefix_enter.text().strip()
    suffix = self.suffix_enter.text().strip()


    sel = cmds.ls(selection=True)
    if not sel:
        cmds.warning("please select object/joint")
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

    pose_name = item.text()
    if pose_name in PoseLibraryUI.pose_library:
        del PoseLibraryUI.pose_library[pose_name]

    self.pose_list.takeItem(self.pose_list.row(item))
    cmds.inViewMessage(amg=f"Pose <hl>{pose_name}</hl> deleted!", pos="midCenter", fade=True)


def rename_pose(self):

    item = self.pose_list.currentItem()

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
