# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home2XcfRtQ.ui'
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

#####################################################
## Main Window Object
#####################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1906, 1077)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")

#####################################################
## Central Widget Object (all page contents)
#####################################################
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

#####################################################
## Side menu Object (side menu icons and buttons )
#####################################################
        self.side_menu = QFrame(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setGeometry(QRect(0, 0, 60, 1081))
        self.side_menu.setMinimumSize(QSize(0, 0))
        self.side_menu.setMaximumSize(QSize(200, 16777215))
        self.side_menu.setStyleSheet(u"background: rgb(1, 58, 83)")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)

## HOME ICON ##
        self.home_icon = QPushButton(self.side_menu)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setGeometry(QRect(-10, 80, 111, 81))
        self.home_icon.setMinimumSize(QSize(100, 0))
        self.home_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/homeic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_icon.setIcon(icon)
        self.home_icon.setIconSize(QSize(55, 55))

## SENT ICON ##
        self.sent_icon = QPushButton(self.side_menu)
        self.sent_icon.setObjectName(u"sent_icon")
        self.sent_icon.setGeometry(QRect(0, 220, 100, 81))
        self.sent_icon.setMinimumSize(QSize(100, 0))
        self.sent_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sendic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sent_icon.setIcon(icon1)
        self.sent_icon.setIconSize(QSize(55, 55))

## RECIEVED ICON ##        
        self.recieve_icon = QPushButton(self.side_menu)
        self.recieve_icon.setObjectName(u"recieve_icon")
        self.recieve_icon.setGeometry(QRect(0, 360, 121, 81))
        self.recieve_icon.setMinimumSize(QSize(100, 0))
        self.recieve_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/rec.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recieve_icon.setIcon(icon2)
        self.recieve_icon.setIconSize(QSize(55, 55))

## INFO ICON ##
        self.info_icon = QPushButton(self.side_menu)
        self.info_icon.setObjectName(u"info_icon")
        self.info_icon.setGeometry(QRect(0, 760, 100, 81))
        self.info_icon.setMinimumSize(QSize(100, 0))
        self.info_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_icon.setIcon(icon3)
        self.info_icon.setIconSize(QSize(55, 55))

## DRAFTS ICON ##
        self.drafts_icon = QPushButton(self.side_menu)
        self.drafts_icon.setObjectName(u"drafts_icon")
        self.drafts_icon.setGeometry(QRect(0, 510, 111, 81))
        self.drafts_icon.setMinimumSize(QSize(100, 0))
        self.drafts_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/editic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drafts_icon.setIcon(icon4)
        self.drafts_icon.setIconSize(QSize(55, 55))

#####################################################
## Top menu Object (top menu icons and buttons)
#####################################################

        self.top_menu = QFrame(self.centralwidget)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setGeometry(QRect(0, 0, 1911, 61))
        self.top_menu.setStyleSheet(u"background: transparent;\n"
"background-color: rgb(1, 67, 86);")
        self.top_menu.setFrameShape(QFrame.StyledPanel)
        self.top_menu.setFrameShadow(QFrame.Raised)

## MENU ICON ##
        self.menu_icon = QPushButton(self.top_menu)
        self.menu_icon.setObjectName(u"menu_icon")
        self.menu_icon.setGeometry(QRect(50, -10, 100, 82))
        self.menu_icon.setMinimumSize(QSize(50, 0))
        self.menu_icon.setMaximumSize(QSize(100, 16777215))
        self.menu_icon.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_icon.setIcon(icon5)
        self.menu_icon.setIconSize(QSize(55, 55))

## NOTIF ICON ##
        self.notif_icon = QPushButton(self.top_menu)
        self.notif_icon.setObjectName(u"notif_icon")
        self.notif_icon.setGeometry(QRect(910, 10, 91, 51))
        self.notif_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/notific.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notif_icon.setIcon(icon6)
        self.notif_icon.setIconSize(QSize(45, 45))

## SETTINGS ICON ##
        self.settings_icon = QPushButton(self.top_menu)
        self.settings_icon.setObjectName(u"settings_icon")
        self.settings_icon.setGeometry(QRect(1090, 10, 91, 51))
        self.settings_icon.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_icon.setIcon(icon7)
        self.settings_icon.setIconSize(QSize(45, 55))

## ACCOUNT ICON ##
        self.account_icon = QPushButton(self.top_menu)
        self.account_icon.setObjectName(u"account_icon")
        self.account_icon.setGeometry(QRect(730, 10, 91, 51))
        self.account_icon.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.account_icon.setIcon(icon8)
        self.account_icon.setIconSize(QSize(45, 45))


#####################################################
## Stacked Widget Object (contains all pages and their contents)
#####################################################

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(60, 60, 1851, 1021))
        self.stackedWidget.setStyleSheet(u"background-image: url(:/bg1/17.png);")

## Page 1 - Home page ##

        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/bg1/home.png);")
       
      ## Send/Recieve Label and buttons ## 
        self.sentl = QLabel(self.home)
        self.sentl.setObjectName(u"sentl")
        self.sentl.setGeometry(QRect(620, 610, 211, 91))
        self.sentl.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);")
        self.sentop = QComboBox(self.home)
        self.sentop.addItem("")
        self.sentop.addItem("")
        self.sentop.addItem("")
        self.sentop.addItem("")
        self.sentop.setObjectName(u"sentop")
        self.sentop.setGeometry(QRect(610, 610, 241, 91))
        self.sentop.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);")
        self.sentop.setEditable(False)
        self.sentop.setMaxVisibleItems(10)
        self.sentop.setFrame(True)
        self.recieve_pack = QPushButton(self.home)
        self.recieve_pack.setObjectName(u"recieve_pack")
        self.recieve_pack.setGeometry(QRect(1070, 610, 241, 91))
        self.recieve_pack.setAutoFillBackground(False)
        self.recieve_pack.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.stackedWidget.addWidget(self.home)
        self.sentop.raise_()
        self.recieve_pack.raise_()
        self.sentl.raise_()

## Page 2 - Network Packets Page ##
        self.packets = QWidget()
        self.packets.setObjectName(u"packets")
        self.packets.setStyleSheet(u"background-image: url(:/bg1/newpc.png);")

        ## DNS ##
        self.dns_bt = QPushButton(self.packets)
        self.dns_bt.setObjectName(u"dns_bt")
        self.dns_bt.setGeometry(QRect(820, 540, 241, 91))
        self.dns_bt.setAutoFillBackground(False)
        self.dns_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")

        ## SSDP ##
        self.ssdp_bt = QPushButton(self.packets)
        self.ssdp_bt.setObjectName(u"ssdp_bt")
        self.ssdp_bt.setGeometry(QRect(1230, 540, 241, 91))
        self.ssdp_bt.setAutoFillBackground(False)
        self.ssdp_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")

        ## NTP ##
        self.ntp_bt = QPushButton(self.packets)
        self.ntp_bt.setObjectName(u"ntp_bt")
        self.ntp_bt.setGeometry(QRect(410, 540, 241, 91))
        self.ntp_bt.setAutoFillBackground(False)
        self.ntp_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.stackedWidget.addWidget(self.packets)

## Page 3 - ETHERNET PACKET labels, inputs and buttons ##
        self.ETH = QWidget()
        self.ETH.setObjectName(u"ETH")
        self.ETH.setStyleSheet(u"background-image: url(:/bg1/eth.png);")
        self.source = QLineEdit(self.ETH)
        self.source.setObjectName(u"source")
        self.source.setGeometry(QRect(410, 390, 361, 51))
        self.source.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.dest = QLineEdit(self.ETH)
        self.dest.setObjectName(u"dest")
        self.dest.setGeometry(QRect(980, 390, 361, 51))
        self.dest.setStyleSheet(u"background: rgb(183, 206, 212);")
        self.type = QLineEdit(self.ETH)
        self.type.setObjectName(u"type")
        self.type.setGeometry(QRect(660, 600, 361, 51))
        self.type.setStyleSheet(u"background: rgb(183, 199, 206);")
        self.def_eth = QPushButton(self.ETH)
        self.def_eth.setObjectName(u"def_eth")
        self.def_eth.setGeometry(QRect(230, 790, 151, 41))
        self.def_eth.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")
        self.nxt_eth = QPushButton(self.ETH)
        self.nxt_eth.setObjectName(u"nxt_eth")
        self.nxt_eth.setGeometry(QRect(1410, 760, 241, 91))
        self.nxt_eth.setAutoFillBackground(False)
        self.nxt_eth.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.info = QLabel(self.ETH)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(230, 850, 351, 16))
        self.info.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad = QLabel(self.ETH)
        self.srcad.setObjectName(u"srcad")
        self.srcad.setGeometry(QRect(410, 450, 161, 21))
        self.srcad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dstad = QLabel(self.ETH)
        self.dstad.setObjectName(u"dstad")
        self.dstad.setGeometry(QRect(980, 450, 211, 21))
        self.dstad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.ty = QLabel(self.ETH)
        self.ty.setObjectName(u"ty")
        self.ty.setGeometry(QRect(660, 660, 161, 21))
        self.ty.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stackedWidget.addWidget(self.ETH)

## Page 4 -  IP PACKET labels, inputs and buttons ##
        self.IP = QWidget()
        self.IP.setObjectName(u"IP")
        self.IP.setStyleSheet(u"background-image: url(:/bg1/ip.png);")
        self.vrsn_box = QLineEdit(self.IP)
        self.vrsn_box.setObjectName(u"vrsn_box")
        self.vrsn_box.setGeometry(QRect(240, 260, 131, 61))
        self.vrsn_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.versn = QLabel(self.IP)
        self.versn.setObjectName(u"versn")
        self.versn.setGeometry(QRect(240, 320, 91, 41))
        self.versn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.IHL_box = QLineEdit(self.IP)
        self.IHL_box.setObjectName(u"IHL_box")
        self.IHL_box.setGeometry(QRect(380, 260, 91, 61))
        self.IHL_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.ihl = QLabel(self.IP)
        self.ihl.setObjectName(u"ihl")
        self.ihl.setGeometry(QRect(380, 320, 91, 41))
        self.ihl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.tos = QLabel(self.IP)
        self.tos.setObjectName(u"tos")
        self.tos.setGeometry(QRect(480, 320, 91, 41))
        self.tos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.tos_box = QLineEdit(self.IP)
        self.tos_box.setObjectName(u"tos_box")
        self.tos_box.setGeometry(QRect(480, 260, 161, 61))
        self.tos_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.length = QLabel(self.IP)
        self.length.setObjectName(u"length")
        self.length.setGeometry(QRect(660, 320, 141, 41))
        self.length.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.len_box = QLineEdit(self.IP)
        self.len_box.setObjectName(u"len_box")
        self.len_box.setGeometry(QRect(660, 260, 381, 61))
        self.len_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.id_box = QLineEdit(self.IP)
        self.id_box.setObjectName(u"id_box")
        self.id_box.setGeometry(QRect(240, 380, 401, 61))
        self.id_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.idfn = QLabel(self.IP)
        self.idfn.setObjectName(u"idfn")
        self.idfn.setGeometry(QRect(240, 440, 141, 41))
        self.idfn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.flgs = QLabel(self.IP)
        self.flgs.setObjectName(u"flgs")
        self.flgs.setGeometry(QRect(650, 440, 91, 41))
        self.flgs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.flags_box = QLineEdit(self.IP)
        self.flags_box.setObjectName(u"flags_box")
        self.flags_box.setGeometry(QRect(650, 380, 111, 61))
        self.flags_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.fragoff = QLabel(self.IP)
        self.fragoff.setObjectName(u"fragoff")
        self.fragoff.setGeometry(QRect(790, 440, 181, 41))
        self.fragoff.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.frag_box = QLineEdit(self.IP)
        self.frag_box.setObjectName(u"frag_box")
        self.frag_box.setGeometry(QRect(790, 380, 251, 61))
        self.frag_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.ttl = QLabel(self.IP)
        self.ttl.setObjectName(u"ttl")
        self.ttl.setGeometry(QRect(240, 570, 91, 41))
        self.ttl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.ttl_box = QLineEdit(self.IP)
        self.ttl_box.setObjectName(u"ttl_box")
        self.ttl_box.setGeometry(QRect(240, 510, 181, 61))
        self.ttl_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.protcl = QLabel(self.IP)
        self.protcl.setObjectName(u"protcl")
        self.protcl.setGeometry(QRect(440, 570, 91, 41))
        self.protcl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.prtcl_box = QLineEdit(self.IP)
        self.prtcl_box.setObjectName(u"prtcl_box")
        self.prtcl_box.setGeometry(QRect(440, 510, 191, 61))
        self.prtcl_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.hdrchksm = QLabel(self.IP)
        self.hdrchksm.setObjectName(u"hdrchksm")
        self.hdrchksm.setGeometry(QRect(650, 570, 211, 41))
        self.hdrchksm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.chksum_box = QLineEdit(self.IP)
        self.chksum_box.setObjectName(u"chksum_box")
        self.chksum_box.setGeometry(QRect(650, 510, 391, 61))
        self.chksum_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.opts = QLabel(self.IP)
        self.opts.setObjectName(u"opts")
        self.opts.setGeometry(QRect(240, 700, 91, 41))
        self.opts.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.textEdit = QTextEdit(self.IP)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(240, 640, 811, 61))
        self.textEdit.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad1 = QLineEdit(self.IP)
        self.srcad1.setObjectName(u"srcad1")
        self.srcad1.setGeometry(QRect(1220, 380, 351, 61))
        self.srcad1.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_txt = QLabel(self.IP)
        self.srcad_txt.setObjectName(u"srcad_txt")
        self.srcad_txt.setGeometry(QRect(1300, 340, 151, 41))
        self.srcad_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 15pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.dstad_txt = QLabel(self.IP)
        self.dstad_txt.setObjectName(u"dstad_txt")
        self.dstad_txt.setGeometry(QRect(1290, 500, 191, 41))
        self.dstad_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 15pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.dstad1 = QLineEdit(self.IP)
        self.dstad1.setObjectName(u"dstad1")
        self.dstad1.setGeometry(QRect(1220, 540, 351, 61))
        self.dstad1.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.nxt_ip = QPushButton(self.IP)
        self.nxt_ip.setObjectName(u"nxt_ip")
        self.nxt_ip.setGeometry(QRect(1410, 760, 241, 91))
        self.nxt_ip.setAutoFillBackground(False)
        self.nxt_ip.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.def_ip = QPushButton(self.IP)
        self.def_ip.setObjectName(u"def_ip")
        self.def_ip.setGeometry(QRect(250, 810, 151, 41))
        self.def_ip.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")
        self.info_2 = QLabel(self.IP)
        self.info_2.setObjectName(u"info_2")
        self.info_2.setGeometry(QRect(250, 870, 351, 16))
        self.info_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stackedWidget.addWidget(self.IP)


## Page 5 -  UDP PACKET labels, inputs and buttons ##
        self.UDP = QWidget()
        self.UDP.setObjectName(u"UDP")
        self.UDP.setStyleSheet(u"background-image: url(:/bg1/udp.png);")
        self.nxt_udp = QPushButton(self.UDP)
        self.nxt_udp.setObjectName(u"nxt_udp")
        self.nxt_udp.setGeometry(QRect(1410, 760, 241, 91))
        self.nxt_udp.setAutoFillBackground(False)
        self.nxt_udp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.srcad_txtt = QLabel(self.UDP)
        self.srcad_txtt.setObjectName(u"srcad_txtt")
        self.srcad_txtt.setGeometry(QRect(420, 390, 181, 41))
        self.srcad_txtt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.ovr_chksm = QCheckBox(self.UDP)
        self.ovr_chksm.setObjectName(u"ovr_chksm")
        self.ovr_chksm.setGeometry(QRect(770, 350, 321, 31))
        self.ovr_chksm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.source_box = QLineEdit(self.UDP)
        self.source_box.setObjectName(u"source_box")
        self.source_box.setGeometry(QRect(420, 330, 251, 61))
        self.source_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.leng_box = QLineEdit(self.UDP)
        self.leng_box.setObjectName(u"leng_box")
        self.leng_box.setGeometry(QRect(1190, 470, 141, 61))
        self.leng_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.dest_box = QLineEdit(self.UDP)
        self.dest_box.setObjectName(u"dest_box")
        self.dest_box.setGeometry(QRect(420, 470, 251, 61))
        self.dest_box.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.chksm_text = QLabel(self.UDP)
        self.chksm_text.setObjectName(u"chksm_text")
        self.chksm_text.setGeometry(QRect(1190, 390, 181, 41))
        self.chksm_text.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.chksum_box_2 = QLineEdit(self.UDP)
        self.chksum_box_2.setObjectName(u"chksum_box_2")
        self.chksum_box_2.setGeometry(QRect(1190, 330, 141, 61))
        self.chksum_box_2.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.ovr_lenval = QCheckBox(self.UDP)
        self.ovr_lenval.setObjectName(u"ovr_lenval")
        self.ovr_lenval.setGeometry(QRect(770, 490, 311, 31))
        self.ovr_lenval.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.leng_txt = QLabel(self.UDP)
        self.leng_txt.setObjectName(u"leng_txt")
        self.leng_txt.setGeometry(QRect(1190, 530, 181, 41))
        self.leng_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dst_txt = QLabel(self.UDP)
        self.dst_txt.setObjectName(u"dst_txt")
        self.dst_txt.setGeometry(QRect(420, 530, 181, 41))
        self.dst_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.info3 = QLabel(self.UDP)
        self.info3.setObjectName(u"info3")
        self.info3.setGeometry(QRect(220, 820, 351, 16))
        self.info3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.def_udp = QPushButton(self.UDP)
        self.def_udp.setObjectName(u"def_udp")
        self.def_udp.setGeometry(QRect(220, 760, 151, 41))
        self.def_udp.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.UDP)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_icon.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.sent_icon.setText(QCoreApplication.translate("MainWindow", u"SENT", None))
        self.recieve_icon.setText(QCoreApplication.translate("MainWindow", u"RECIEVED", None))
        self.info_icon.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.drafts_icon.setText(QCoreApplication.translate("MainWindow", u"DRAFTS", None))
        self.menu_icon.setText("")
        self.notif_icon.setText("")
        self.settings_icon.setText("")
        self.account_icon.setText("")
        self.sentl.setText(QCoreApplication.translate("MainWindow", u"     Send", None))
        self.sentop.setItemText(0, QCoreApplication.translate("MainWindow", u"Sent", None))
        self.sentop.setItemText(1, QCoreApplication.translate("MainWindow", u"Drafts", None))
        self.sentop.setItemText(2, QCoreApplication.translate("MainWindow", u"Autocreate", None))
        self.sentop.setItemText(3, QCoreApplication.translate("MainWindow", u"New Packet", None))

#if QT_CONFIG(tooltip)
        self.sentop.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sentop.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Send</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.sentop.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.sentop.setCurrentText(QCoreApplication.translate("MainWindow", u"Sent", None))
        self.recieve_pack.setText(QCoreApplication.translate("MainWindow", u"Recieve", None))
        self.dns_bt.setText(QCoreApplication.translate("MainWindow", u"DNS", None))
        self.ssdp_bt.setText(QCoreApplication.translate("MainWindow", u"SSDP", None))
        self.ntp_bt.setText(QCoreApplication.translate("MainWindow", u"NTP", None))
        self.def_eth.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.nxt_eth.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.srcad.setText(QCoreApplication.translate("MainWindow", u"Source Address", None))
        self.dstad.setText(QCoreApplication.translate("MainWindow", u"Destination Address", None))
        self.ty.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.versn.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.ihl.setText(QCoreApplication.translate("MainWindow", u"IHL", None))
        self.tos.setText(QCoreApplication.translate("MainWindow", u"TOS", None))
        self.length.setText(QCoreApplication.translate("MainWindow", u"Total Length", None))
        self.id_box.setText("")
        self.idfn.setText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.flgs.setText(QCoreApplication.translate("MainWindow", u"Flags", None))
        self.fragoff.setText(QCoreApplication.translate("MainWindow", u"Fragment Offset", None))
        self.ttl.setText(QCoreApplication.translate("MainWindow", u"TTL", None))
        self.protcl.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        self.hdrchksm.setText(QCoreApplication.translate("MainWindow", u"Header Checksum", None))
        self.opts.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.srcad_txt.setText(QCoreApplication.translate("MainWindow", u"Source Address", None))
        self.dstad_txt.setText(QCoreApplication.translate("MainWindow", u"Destination Address", None))
        self.nxt_ip.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.def_ip.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.info_2.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.nxt_udp.setText(QCoreApplication.translate("MainWindow", u"NEXT", None))
        self.srcad_txtt.setText(QCoreApplication.translate("MainWindow", u"Source Port", None))
        self.ovr_chksm.setText(QCoreApplication.translate("MainWindow", u"Override UDP Checksum Value ", None))
        self.source_box.setText("")
        self.leng_box.setText("")
        self.dest_box.setText("")
        self.chksm_text.setText(QCoreApplication.translate("MainWindow", u"Checksum", None))
        self.chksum_box_2.setText("")
        self.ovr_lenval.setText(QCoreApplication.translate("MainWindow", u"Override UDP Length Value ", None))
        self.leng_txt.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.dst_txt.setText(QCoreApplication.translate("MainWindow", u"Destination Port", None))
        self.info3.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.def_udp.setText(QCoreApplication.translate("MainWindow", u"Default", None))
    # retranslateUi

