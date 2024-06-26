# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\easytts\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(824, 463)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\easytts\\icon.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("#mainWindow{background:white}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("QWidget{background:white}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(500, 400))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("QFrame{background:white}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_select_dir = QtWidgets.QPushButton(self.frame)
        self.pushButton_select_dir.setStyleSheet("QPushButton {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 16px;\n"
"    color: #ffffff;\n"
"    background-color: rgb(206, 175, 36);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: gray;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover{ background-color: #b4bd3a;}\n"
"QPushButton:pressed{  background-color:  #a5ad35;}")
        self.pushButton_select_dir.setObjectName("pushButton_select_dir")
        self.horizontalLayout.addWidget(self.pushButton_select_dir)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonlisten = QtWidgets.QPushButton(self.frame)
        self.pushButtonlisten.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonlisten.setStyleSheet("QPushButton {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 16px;\n"
"    color: #ffffff;\n"
"    background-color: rgb(206, 175, 36);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: gray;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover{ background-color: #b4bd3a;}\n"
"QPushButton:pressed{  background-color:  #a5ad35;}")
        self.pushButtonlisten.setFlat(True)
        self.pushButtonlisten.setObjectName("pushButtonlisten")
        self.verticalLayout.addWidget(self.pushButtonlisten)
        self.pushButton_start = QtWidgets.QPushButton(self.frame)
        self.pushButton_start.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_start.setAutoFillBackground(False)
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 16px;\n"
"    color: #ffffff;\n"
"    background-color: rgb(206, 175, 36);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: gray;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover{ background-color: #b4bd3a;}\n"
"QPushButton:pressed{  background-color:  #a5ad35;}")
        self.pushButton_start.setFlat(True)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.frame)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionreadme = QtWidgets.QAction(mainWindow)
        self.actionreadme.setObjectName("actionreadme")
        self.menu.addAction(self.actionreadme)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "文本转语音"))
        self.pushButton_select_dir.setText(_translate("mainWindow", "选择路径"))
        self.pushButtonlisten.setText(_translate("mainWindow", "试听声音"))
        self.pushButton_start.setText(_translate("mainWindow", "开始转换"))
        self.menu.setTitle(_translate("mainWindow", "帮助"))
        self.actionreadme.setText(_translate("mainWindow", "Readme"))
