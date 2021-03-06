#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymssql
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Login import Ui_MainWindow
from Register import RegisterForm
from Admin import AdminForm
from Owner import OwnerForm
from wRepresentative import wRepresentativeForm
from eRepresentative import eRepresentativeForm
import t

#数据库服务器信息
server='DESKTOP-9J11AF2'
user="login"
password="321"
database="SQLCD"
class LoginForm(Ui_MainWindow,QtWidgets.QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(LoginForm, self).__init__()
        self.setupUi(self)


        self.conn = pymssql.connect(server, user, password, database, charset="utf8")
        self.cur = self.conn.cursor()

        self.pushButton.clicked.connect(self.loclick)
        self.pushButton_2.clicked.connect(self.reclick)
        self.pushButton_3.clicked.connect(self.showverification)
        self.test=t.verification()
        self.label_5.setScaledContents(True)
        self.label_5.setPixmap(QtGui.QPixmap("out.jpg"))
        self.lineEdit_3.setText(self.test)



    def showverification(self):
        self.test = t.verification()
        self.label_5.setPixmap(QtGui.QPixmap("out.jpg"))


    def loclick(self):                   #登录点击事件
        print (self.test.lower(),self.lineEdit_3.text().lower())
        if self.test.lower()==self.lineEdit_3.text().lower():
            account=self.lineEdit.text()
            password=self.lineEdit_2.text()
            sql = "SELECT type,own_num FROM accounts WHERE account=%s AND password=%s"
            self.cur.execute(sql,(account,password))
            ty = self.cur.fetchall()
            if len(ty)>0:
                if ty[0][0][0]=='1':
                    self.close()
                    self.ad=AdminForm()
                    self.ad.show()
                    self.conn.close()
                elif ty[0][0][0]=='2':
                    self.close()
                    self.ow=OwnerForm(ty[0][1])
                    self.ow.show()
                    self.conn.close()

                elif ty[0][0][0]=='3':
                    self.close()
                    self.wre=wRepresentativeForm()
                    self.wre.show()
                    self.conn.close()
                elif ty[0][0][0]=='4':
                    self.close()
                    self.ere=eRepresentativeForm()
                    self.ere.show()
                    self.conn.close()


            else:
                QtWidgets.QMessageBox.warning(self, '错误', '用户名或密码有误，请重新输入')
        else:
            QtWidgets.QMessageBox.warning(self,'错误','验证码输入错误')
            self.showverification()

    def reclick(self):                #注册点击事件
        self.re = RegisterForm()
        if self.cur:
            self.re.SetSql(self.conn,self.cur)
            self.re.exec_()

