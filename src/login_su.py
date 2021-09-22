# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paatNDtYJP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

#####################################################
## Main Window Object
#####################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1908, 1090)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/bg1/bg9.png);")
#####################################################
## Central Widget Object (All login/sign up page contents)
#####################################################
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

#####################################################
## LogIn: Username and password / login button
#####################################################

        self.username_lg = QLineEdit(self.centralwidget)
        self.username_lg.setObjectName(u"username_lg")
        self.username_lg.setGeometry(QRect(460, 410, 381, 51))

        self.password_lg = QLineEdit(self.centralwidget)
        self.password_lg.setObjectName(u"password_lg")
        self.password_lg.setGeometry(QRect(460, 590, 381, 51))

        self.terms = QCheckBox(self.centralwidget)
        self.terms.setObjectName(u"terms")
        self.terms.setGeometry(QRect(1190, 760, 251, 21))
        self.terms.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"background: transparent;\n"
"color: rgb(255, 255, 255);")

        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(540, 720, 271, 91))
        self.login.setAutoFillBackground(False)
        self.login.setStyleSheet(u"font: 18pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        

#########################################################
## SignUp: Email, Username, Password, T&C / signup button
#########################################################

          
        self.email_su = QLineEdit(self.centralwidget)
        self.email_su.setObjectName(u"email_su")
        self.email_su.setGeometry(QRect(1190, 350, 381, 51))

        self.username_su = QLineEdit(self.centralwidget)
        self.username_su.setObjectName(u"username_su")
        self.username_su.setGeometry(QRect(1190, 500, 381, 51))

        self.password_su = QLineEdit(self.centralwidget)
        self.password_su.setObjectName(u"password_su")
        self.password_su.setGeometry(QRect(1190, 660, 381, 51))

        self.signup = QPushButton(self.centralwidget)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(1250, 830, 271, 91))
        self.signup.setAutoFillBackground(False)
        self.signup.setStyleSheet(u"font: 18pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")

#####################################################
## Top Icon Buttons: Settings icon + help window
#####################################################
        self.settings_icon = QPushButton(self.centralwidget)
        self.settings_icon.setObjectName(u"settings_icon")
        self.settings_icon.setGeometry(QRect(1730, 50, 101, 91))
        self.settings_icon.setAutoFillBackground(False)
        self.settings_icon.setStyleSheet(u"background: transparent;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_icon.setIcon(icon1)
        self.settings_icon.setIconSize(QSize(86, 76))

#####################################################
## Top Icon Buttons: Info icon + help window
#####################################################  
        self.info_icon = QPushButton(self.centralwidget)
        self.info_icon.setObjectName(u"info_icon")
        self.info_icon.setGeometry(QRect(1600, 50, 101, 91))
        self.info_icon.setAutoFillBackground(False)
        self.info_icon.setStyleSheet(u"background: transparent;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_icon.setIcon(icon)
        self.info_icon.setIconSize(QSize(76, 66))
        self.info_icon.clicked.connect(self.helpUi)
                
#####################################################
## UI window setup
#####################################################        
        MainWindow.setCentralWidget(self.centralwidget)
        self.username_lg.raise_()
        self.password_lg.raise_()
        self.terms.raise_()
        self.login.raise_()
        self.info_icon.raise_()
        self.settings_icon.raise_()
        self.signup.raise_()
        self.email_su.raise_()
        self.username_su.raise_()
        self.password_su.raise_()
 
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.terms.setText(QCoreApplication.translate("MainWindow", u"Accept Terms and Conditions.", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.info_icon.setText("")
        self.settings_icon.setText("")
        self.signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
    # retranslateUi
    
    def helpUi(self):
        self.help_wgt = QWidget(self.centralwidget)
        self.help_wgt.setObjectName(u"help_wgt")
        self.help_wgt.setGeometry(QRect(50, 10, 591, 321))
        self.help_wgt.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 160, 165) stop:0.55 rgb(0, 160, 165) , stop:0.98 rgb(1, 114, 148), stop:1 rgb(0, 0, 0))")
        self.help_title = QLabel(self.help_wgt)
        self.help_title.setObjectName(u"help_title")
        self.help_title.setGeometry(QRect(240, 20, 111, 71))
        self.help_title.setAutoFillBackground(False)
        self.help_title.setStyleSheet(u"background: transparent;\n"
"font: 26pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255)\n"
"")
        self.understood_bt = QPushButton(self.help_wgt)
        self.understood_bt.setObjectName(u"understood_bt")
        self.understood_bt.setGeometry(QRect(230, 230, 131, 41))
        self.understood_bt.setAutoFillBackground(False)
        self.understood_bt.setStyleSheet(u"font: 8pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding: 5px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.info_txt = QTextBrowser(self.help_wgt)
        self.info_txt.setObjectName(u"info_txt")
        self.info_txt.setGeometry(QRect(70, 100, 451, 111))
        self.info_txt.setStyleSheet(u"border: transparent;\n"
"background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Medium Cond\";")
        self.help_wgt.raise_()
        self.help_title.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.understood_bt.setText(QCoreApplication.translate("MainWindow", u"Understood", None))
        self.info_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:7.8pt; font-weight:496;\">P.A.A.T. is a packet amplification assesment tool that enables the user to send and recieve packets between users on different servers easily. To access the tool please create an account and sign up if you're a new user, and log in with your credentials if you're an existing user.</span></p></body></html>", None))