# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1057, 818))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.label.setStyleSheet("font: 18pt \"黑体\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tableView = QtWidgets.QTableView(self.splitter_2)
        self.tableView.setMinimumSize(QtCore.QSize(761, 701))
        self.tableView.setStyleSheet("font: 14pt \"黑体\";")
        self.tableView.setObjectName("tableView")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(221, 211))
        self.groupBox_2.setStyleSheet("font: 14pt \"Agency FB\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 40, 111, 51))
        self.pushButton_3.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 61, 21))
        self.label_2.setStyleSheet("font: 15pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 120, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(221, 278))
        self.groupBox.setStyleSheet("font: 14pt \"Agency FB\";")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 111, 51))
        self.pushButton.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 140, 111, 51))
        self.pushButton_2.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(221, 211))
        self.widget.setObjectName("widget")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 70, 111, 51))
        self.pushButton_4.setStyleSheet("font: 15pt \"黑体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "物业管理系统-管理员"))
        self.label.setText(_translate("MainWindow", "   管理员"))
        self.groupBox_2.setTitle(_translate("MainWindow", "查询"))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))
        self.label_2.setText(_translate("MainWindow", "业主号"))
        self.groupBox.setTitle(_translate("MainWindow", "增添"))
        self.pushButton.setText(_translate("MainWindow", "增添"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_4.setText(_translate("MainWindow", "显示全部"))

