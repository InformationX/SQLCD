#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Admin import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymssql

#数据库服务器信息
server='DESKTOP-9J11AF2'
user="admin"
password="123"
database="SQLCD"

title=['业主号', '业主名','房间号','电话']
dist={0:'owner_num',1:'owner_name'}
class AdminForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(AdminForm, self).__init__()
        self.setupUi(self)

        self.conn = pymssql.connect(server, user, password, database, charset="utf8")
        self.cur = self.conn.cursor()
        self.init()
        self.num=self.model.rowCount()

        self.pushButton.clicked.connect(self.addRow)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.select)
        self.pushButton_4.clicked.connect(self.showall)
        self.tableView.doubleClicked.connect(self.gettemp)
        #self.tableView.doubleClicked.connect(self.tableView.edit)
        self.model.itemChanged.connect(self.addorcor)



    #初始化界面
    def init(self):
        self.model = QStandardItemModel(0, len(title));
        self.model.setHorizontalHeaderLabels(title)
        self.showall()
        self.tableView.setModel(self.model)

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QtWidgets.QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

#展示业主信息
    def showall(self):
        self.model.removeRows(0, self.model.rowCount())
        sql = "SELECT * FROM owner"
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        self.addItem(rows)

#获取修改前的值
    def gettemp(self,item):
        self.temp=item.data()


#添加或修改
    def addorcor(self,item):

        text=item.text()

        if item.row()>=self.num:
            self.num = self.num + 1
            sql="INSERT INTO owner(owner_num) VALUES (%s)"
            try:
                self.cur.execute(sql,"temp")
                self.conn.commit()

            except:
                QMessageBox.critical(self, '错误', '输入有误，主码可能重复*')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                self.num = self.num - 1
                return

#是否为主键，是否第一次修改的关键逻辑，核心
        if self.model.item(item.row(), 0)!=None:
            if item.column()!=0:
                key = self.model.item(item.row(), 0).text()
            else:
                if self.temp!=None:
                    key=self.temp
                else:
                    key="temp"
        else:
            key="temp"


        if item.column()==0:

            sql="UPDATE owner SET owner_num=%s WHERE owner_num=%s"
            try:

                self.cur.execute(sql, (str(text), key))
            except:
                QMessageBox.critical(self, '错误', '输入有误，主码可能重复')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                return
        elif item.column()==1:
            print("1")
            sql = "UPDATE owner SET owner_name=%s WHERE owner_num=%s"
            try:
                self.cur.execute(sql,(str(item.text()),str(key)))
            except:
                QMessageBox.critical(self, '错误', '输入有误')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                return
        elif item.column() == 2:
            print("2")
            sql = "UPDATE owner SET room_num=%s WHERE owner_num=%s"
            try:
                self.cur.execute(sql, (str(item.text()), str(key)))
            except:
                QMessageBox.critical(self, '错误', '输入有误')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                return
        elif item.column() == 3:
            print("3")
            sql = "UPDATE owner SET tell=%s WHERE owner_num=%s"
            try:
                self.cur.execute(sql, (str(item.text()), str(key)))
            except:
                QMessageBox.critical(self, '错误', '输入有误')
                self.model.setItem(item.row(), item.column(), QStandardItem(self.temp))
                return
        self.conn.commit()
        #print(item.row(),item.column(),item.text())

#加入新行
    def addRow(self):
        self.model.appendRow([])

#添加表项
    def addItem(self,rows):
        row=len(rows)
        col=len(title)
        for i in range(row):
            date = []
            for j in range(col):
                item = QStandardItem(str(rows[i][j]))
                date.append(item)
            self.model.appendRow(date)

#删除某行
    def delete(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs) > 0:
            index = indexs[0]
            key = self.model.item(index.row(), 0).text()
            sql = "DELETE FROM owner WHERE owner_num=%s"
            try:
                self.cur.execute(sql,key)
                self.conn.commit()
                self.model.removeRows(index.row(), 1)
            except:
                QMessageBox.critical(self,'错误','该业主号已被注册，无法删除')

        self.num = self.model.rowCount()

#搜索于业主
    def select(self):
        self.model.removeRows(0,self.model.rowCount())
        text=str(self.lineEdit.text())
        if len(text)>0:
            sql="SELECT * FROM owner WHERE owner_num=%s"
            self.cur.execute(sql,text)
            rows = self.cur.fetchall()
            self.addItem(rows)

