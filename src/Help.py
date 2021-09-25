# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paatNDtYJP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import source_rc

class Help():
    def setupUi(self):
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