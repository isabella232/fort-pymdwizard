# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Ducky.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent_Files = QtWidgets.QMenu(self.menuFile)
        self.menuRecent_Files.setObjectName("menuRecent_Files")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionItem_1 = QtWidgets.QAction(MainWindow)
        self.actionItem_1.setObjectName("actionItem_1")
        self.actionItem_2 = QtWidgets.QAction(MainWindow)
        self.actionItem_2.setObjectName("actionItem_2")
        self.actionItem_3 = QtWidgets.QAction(MainWindow)
        self.actionItem_3.setObjectName("actionItem_3")
        self.actionItem_4 = QtWidgets.QAction(MainWindow)
        self.actionItem_4.setObjectName("actionItem_4")
        self.actionItem_5 = QtWidgets.QAction(MainWindow)
        self.actionItem_5.setObjectName("actionItem_5")
        self.actionItem_6 = QtWidgets.QAction(MainWindow)
        self.actionItem_6.setObjectName("actionItem_6")
        self.actionItem_7 = QtWidgets.QAction(MainWindow)
        self.actionItem_7.setObjectName("actionItem_7")
        self.actionItem_8 = QtWidgets.QAction(MainWindow)
        self.actionItem_8.setObjectName("actionItem_8")
        self.actionItem_9 = QtWidgets.QAction(MainWindow)
        self.actionItem_9.setObjectName("actionItem_9")
        self.actionItem_10 = QtWidgets.QAction(MainWindow)
        self.actionItem_10.setObjectName("actionItem_10")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecent_Files.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metadata Wizard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRecent_Files.setTitle(_translate("MainWindow", "Recent Files"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as ..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionItem_1.setText(_translate("MainWindow", "item 1"))
        self.actionItem_2.setText(_translate("MainWindow", "item 2"))
        self.actionItem_3.setText(_translate("MainWindow", "item 3"))
        self.actionItem_4.setText(_translate("MainWindow", "item 4"))
        self.actionItem_5.setText(_translate("MainWindow", "item 5"))
        self.actionItem_6.setText(_translate("MainWindow", "item 6"))
        self.actionItem_7.setText(_translate("MainWindow", "item 7"))
        self.actionItem_8.setText(_translate("MainWindow", "item 8"))
        self.actionItem_9.setText(_translate("MainWindow", "item 9 "))
        self.actionItem_10.setText(_translate("MainWindow", "item 10"))

import icons_rc