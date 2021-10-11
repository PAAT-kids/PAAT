# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home2XcfRtQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from typing import Text
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import source_rc

#####################################################
## Main Window Object
#####################################################
class Ui_OtherWindow(object):
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
        self.sentop.addItem("Sent")
        self.sentop.addItem("Drafts")
        self.sentop.addItem("Autocreate")
        self.sentop.addItem("New Packet")
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

        self.sentop.activated.connect(self.chosen)

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
        self.pressed = ''
        self.ntp_bt.clicked.connect(lambda: self.ethpage('ntp'))
        self.ssdp_bt.clicked.connect(lambda: self.ethpage('ssdp'))
        self.dns_bt.clicked.connect(lambda: self.ethpage('dns'))

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
        
        self.nxt_eth.clicked.connect(self.ippage)

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

        self.nxt_ip.clicked.connect(self.udppage)


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

        self.nxt_udp.clicked.connect(self.nxtpage)

## Page 6 -  NTP PACKET labels, inputs and buttons ##

        self.NTP = QWidget()
        self.NTP.setObjectName(u"NTP")
        self.NTP.setStyleSheet(u"background-image: url(:/bg1/ntp.png);")
        self.send_ntp = QPushButton(self.NTP)
        self.send_ntp.setObjectName(u"send_ntp")
        self.send_ntp.setGeometry(QRect(1560, 680, 241, 91))
        self.send_ntp.setAutoFillBackground(False)
        self.send_ntp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.draft_ntp = QPushButton(self.NTP)
        self.draft_ntp.setObjectName(u"draft_ntp")
        self.draft_ntp.setGeometry(QRect(1560, 550, 241, 91))
        self.draft_ntp.setAutoFillBackground(False)
        self.draft_ntp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.mode_field = QLineEdit(self.NTP)
        self.mode_field.setObjectName(u"mode_field")
        self.mode_field.setGeometry(QRect(970, 290, 141, 61))
        self.mode_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.dispersion_field = QLineEdit(self.NTP)
        self.dispersion_field.setObjectName(u"dispersion_field")
        self.dispersion_field.setGeometry(QRect(1130, 410, 141, 61))
        self.dispersion_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.id_field = QLineEdit(self.NTP)
        self.id_field.setObjectName(u"id_field")
        self.id_field.setGeometry(QRect(650, 530, 621, 61))
        self.id_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.delay_field = QLineEdit(self.NTP)
        self.delay_field.setObjectName(u"delay_field")
        self.delay_field.setGeometry(QRect(970, 410, 141, 61))
        self.delay_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.poll_field = QLineEdit(self.NTP)
        self.poll_field.setObjectName(u"poll_field")
        self.poll_field.setGeometry(QRect(650, 410, 141, 61))
        self.poll_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.sent_field = QLineEdit(self.NTP)
        self.sent_field.setObjectName(u"sent_field")
        self.sent_field.setGeometry(QRect(1130, 770, 141, 61))
        self.sent_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.stratum_field = QLineEdit(self.NTP)
        self.stratum_field.setObjectName(u"stratum_field")
        self.stratum_field.setGeometry(QRect(1130, 290, 141, 61))
        self.stratum_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.version_field = QLineEdit(self.NTP)
        self.version_field.setObjectName(u"version_field")
        self.version_field.setGeometry(QRect(810, 290, 141, 61))
        self.version_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.precision_field = QLineEdit(self.NTP)
        self.precision_field.setObjectName(u"precision_field")
        self.precision_field.setGeometry(QRect(810, 410, 141, 61))
        self.precision_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.leap_field = QLineEdit(self.NTP)
        self.leap_field.setObjectName(u"leap_field")
        self.leap_field.setGeometry(QRect(650, 290, 141, 61))
        self.leap_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.referenceid_field = QLineEdit(self.NTP)
        self.referenceid_field.setObjectName(u"referenceid_field")
        self.referenceid_field.setGeometry(QRect(650, 650, 621, 61))
        self.referenceid_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.recieve_field = QLineEdit(self.NTP)
        self.recieve_field.setObjectName(u"recieve_field")
        self.recieve_field.setGeometry(QRect(970, 770, 141, 61))
        self.recieve_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.origin_field = QLineEdit(self.NTP)
        self.origin_field.setObjectName(u"origin_field")
        self.origin_field.setGeometry(QRect(810, 770, 141, 61))
        self.origin_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.reference_field = QLineEdit(self.NTP)
        self.reference_field.setObjectName(u"reference_field")
        self.reference_field.setGeometry(QRect(650, 770, 141, 61))
        self.reference_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_23 = QLabel(self.NTP)
        self.srcad_23.setObjectName(u"srcad_23")
        self.srcad_23.setGeometry(QRect(810, 470, 141, 41))
        self.srcad_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_24 = QLabel(self.NTP)
        self.srcad_24.setObjectName(u"srcad_24")
        self.srcad_24.setGeometry(QRect(1130, 470, 141, 41))
        self.srcad_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_25 = QLabel(self.NTP)
        self.srcad_25.setObjectName(u"srcad_25")
        self.srcad_25.setGeometry(QRect(970, 470, 141, 41))
        self.srcad_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_26 = QLabel(self.NTP)
        self.srcad_26.setObjectName(u"srcad_26")
        self.srcad_26.setGeometry(QRect(650, 470, 141, 41))
        self.srcad_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_27 = QLabel(self.NTP)
        self.srcad_27.setObjectName(u"srcad_27")
        self.srcad_27.setGeometry(QRect(650, 590, 621, 41))
        self.srcad_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_28 = QLabel(self.NTP)
        self.srcad_28.setObjectName(u"srcad_28")
        self.srcad_28.setGeometry(QRect(970, 830, 141, 41))
        self.srcad_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_29 = QLabel(self.NTP)
        self.srcad_29.setObjectName(u"srcad_29")
        self.srcad_29.setGeometry(QRect(650, 830, 141, 41))
        self.srcad_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_30 = QLabel(self.NTP)
        self.srcad_30.setObjectName(u"srcad_30")
        self.srcad_30.setGeometry(QRect(810, 830, 141, 41))
        self.srcad_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_31 = QLabel(self.NTP)
        self.srcad_31.setObjectName(u"srcad_31")
        self.srcad_31.setGeometry(QRect(1130, 830, 141, 41))
        self.srcad_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_32 = QLabel(self.NTP)
        self.srcad_32.setObjectName(u"srcad_32")
        self.srcad_32.setGeometry(QRect(650, 710, 621, 41))
        self.srcad_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_33 = QLabel(self.NTP)
        self.srcad_33.setObjectName(u"srcad_33")
        self.srcad_33.setGeometry(QRect(970, 350, 141, 41))
        self.srcad_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_34 = QLabel(self.NTP)
        self.srcad_34.setObjectName(u"srcad_34")
        self.srcad_34.setGeometry(QRect(1130, 350, 141, 41))
        self.srcad_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_35 = QLabel(self.NTP)
        self.srcad_35.setObjectName(u"srcad_35")
        self.srcad_35.setGeometry(QRect(810, 350, 141, 41))
        self.srcad_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_36 = QLabel(self.NTP)
        self.srcad_36.setObjectName(u"srcad_36")
        self.srcad_36.setGeometry(QRect(650, 350, 141, 41))
        self.srcad_36.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.info_6 = QLabel(self.NTP)
        self.info_6.setObjectName(u"info_6")
        self.info_6.setGeometry(QRect(200, 910, 351, 16))
        self.info_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stackedWidget.addWidget(self.NTP)

## Page 6 -  DNS PACKET labels, inputs and buttons ##

        self.DNS = QWidget()
        self.DNS.setObjectName(u"DNS")
        self.DNS.setStyleSheet(u"background-image: url(:/bg1/dns.png);")
        self.draft_dns = QPushButton(self.DNS)
        self.draft_dns.setObjectName(u"draft_dns")
        self.draft_dns.setGeometry(QRect(1560, 550, 241, 91))
        self.draft_dns.setAutoFillBackground(False)
        self.draft_dns.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.send_dns = QPushButton(self.DNS)
        self.send_dns.setObjectName(u"send_dns")
        self.send_dns.setGeometry(QRect(1560, 680, 241, 91))
        self.send_dns.setAutoFillBackground(False)
        self.send_dns.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.srcad_39 = QLabel(self.DNS)
        self.srcad_39.setObjectName(u"srcad_39")
        self.srcad_39.setGeometry(QRect(790, 650, 141, 41))
        self.srcad_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.srcad_37 = QLabel(self.DNS)
        self.srcad_37.setObjectName(u"srcad_37")
        self.srcad_37.setGeometry(QRect(1010, 650, 141, 41))
        self.srcad_37.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qname_field = QLineEdit(self.DNS)
        self.qname_field.setObjectName(u"qname_field")
        self.qname_field.setGeometry(QRect(460, 370, 1021, 61))
        self.qname_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_38 = QLabel(self.DNS)
        self.srcad_38.setObjectName(u"srcad_38")
        self.srcad_38.setGeometry(QRect(460, 430, 1021, 41))
        self.srcad_38.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qtype_field = QLineEdit(self.DNS)
        self.qtype_field.setObjectName(u"qtype_field")
        self.qtype_field.setGeometry(QRect(790, 590, 141, 61))
        self.qtype_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.qclass_field = QLineEdit(self.DNS)
        self.qclass_field.setObjectName(u"qclass_field")
        self.qclass_field.setGeometry(QRect(1010, 590, 141, 61))
        self.qclass_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.info_7 = QLabel(self.DNS)
        self.info_7.setObjectName(u"info_7")
        self.info_7.setGeometry(QRect(200, 910, 351, 16))
        self.info_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stackedWidget.addWidget(self.DNS)

## Page 6 -  SSDP PACKET labels, inputs and buttons ##

        self.SSDP = QWidget()
        self.SSDP.setObjectName(u"SSDP")
        self.SSDP.setStyleSheet(u"background-image: url(:/bg1/ssdp.png);")
        self.draft_dns_2 = QPushButton(self.SSDP)
        self.draft_dns_2.setObjectName(u"draft_dns_2")
        self.draft_dns_2.setGeometry(QRect(1560, 550, 241, 91))
        self.draft_dns_2.setAutoFillBackground(False)
        self.draft_dns_2.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.send_dns_2 = QPushButton(self.SSDP)
        self.send_dns_2.setObjectName(u"send_dns_2")
        self.send_dns_2.setGeometry(QRect(1560, 680, 241, 91))
        self.send_dns_2.setAutoFillBackground(False)
        self.send_dns_2.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.srcad_40 = QLabel(self.SSDP)
        self.srcad_40.setObjectName(u"srcad_40")
        self.srcad_40.setGeometry(QRect(770, 700, 141, 41))
        self.srcad_40.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qtype_field_2 = QLineEdit(self.SSDP)
        self.qtype_field_2.setObjectName(u"qtype_field_2")
        self.qtype_field_2.setGeometry(QRect(1020, 490, 371, 61))
        self.qtype_field_2.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_41 = QLabel(self.SSDP)
        self.srcad_41.setObjectName(u"srcad_41")
        self.srcad_41.setGeometry(QRect(1020, 550, 141, 41))
        self.srcad_41.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qclass_field_2 = QLineEdit(self.SSDP)
        self.qclass_field_2.setObjectName(u"qclass_field_2")
        self.qclass_field_2.setGeometry(QRect(770, 640, 371, 61))
        self.qclass_field_2.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_42 = QLabel(self.SSDP)
        self.srcad_42.setObjectName(u"srcad_42")
        self.srcad_42.setGeometry(QRect(1020, 420, 141, 41))
        self.srcad_42.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qtype_field_3 = QLineEdit(self.SSDP)
        self.qtype_field_3.setObjectName(u"qtype_field_3")
        self.qtype_field_3.setGeometry(QRect(550, 490, 371, 61))
        self.qtype_field_3.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_43 = QLabel(self.SSDP)
        self.srcad_43.setObjectName(u"srcad_43")
        self.srcad_43.setGeometry(QRect(550, 550, 141, 41))
        self.srcad_43.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qclass_field_3 = QLineEdit(self.SSDP)
        self.qclass_field_3.setObjectName(u"qclass_field_3")
        self.qclass_field_3.setGeometry(QRect(1020, 360, 371, 61))
        self.qclass_field_3.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.srcad_44 = QLabel(self.SSDP)
        self.srcad_44.setObjectName(u"srcad_44")
        self.srcad_44.setGeometry(QRect(550, 420, 141, 41))
        self.srcad_44.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qclass_field_4 = QLineEdit(self.SSDP)
        self.qclass_field_4.setObjectName(u"qclass_field_4")
        self.qclass_field_4.setGeometry(QRect(550, 360, 371, 61))
        self.qclass_field_4.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.info_8 = QLabel(self.SSDP)
        self.info_8.setObjectName(u"info_8")
        self.info_8.setGeometry(QRect(200, 910, 351, 16))
        self.info_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stackedWidget.addWidget(self.SSDP)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.send_ntp.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))
        self.draft_ntp.setText(QCoreApplication.translate("MainWindow", u"Save As Draft", None))
        self.mode_field.setText("")
        self.dispersion_field.setText("")
        self.id_field.setText("")
        self.delay_field.setText("")
        self.poll_field.setText("")
        self.sent_field.setText("")
        self.stratum_field.setText("")
        self.version_field.setText("")
        self.precision_field.setText("")
        self.leap_field.setText("")
        self.referenceid_field.setText("")
        self.recieve_field.setText("")
        self.origin_field.setText("")
        self.reference_field.setText("")
        self.srcad_23.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.srcad_24.setText(QCoreApplication.translate("MainWindow", u"Dispersion", None))
        self.srcad_25.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.srcad_26.setText(QCoreApplication.translate("MainWindow", u"Poll", None))
        self.srcad_27.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.srcad_28.setText(QCoreApplication.translate("MainWindow", u"Recieve", None))
        self.srcad_29.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.srcad_30.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.srcad_31.setText(QCoreApplication.translate("MainWindow", u"Sent", None))
        self.srcad_32.setText(QCoreApplication.translate("MainWindow", u"Reference ID", None))
        self.srcad_33.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.srcad_34.setText(QCoreApplication.translate("MainWindow", u"Stratum", None))
        self.srcad_35.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.srcad_36.setText(QCoreApplication.translate("MainWindow", u"Leap", None))
        self.info_6.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.draft_dns.setText(QCoreApplication.translate("MainWindow", u"Save As Draft", None))
        self.send_dns.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))
        self.srcad_39.setText(QCoreApplication.translate("MainWindow", u"Qtype", None))
        self.srcad_37.setText(QCoreApplication.translate("MainWindow", u"Qclass", None))
        self.qname_field.setText("")
        self.srcad_38.setText(QCoreApplication.translate("MainWindow", u"Qname", None))
        self.qtype_field.setText("")
        self.qclass_field.setText("")
        self.info_7.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.draft_dns_2.setText(QCoreApplication.translate("MainWindow", u"Save As Draft", None))
        self.send_dns_2.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))
        self.srcad_40.setText(QCoreApplication.translate("MainWindow", u"ST", None))
        self.qtype_field_2.setText("")
        self.srcad_41.setText(QCoreApplication.translate("MainWindow", u"MX", None))
        self.qclass_field_2.setText("")
        self.srcad_42.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.qtype_field_3.setText("")
        self.srcad_43.setText(QCoreApplication.translate("MainWindow", u"MAN", None))
        self.qclass_field_3.setText("")
        self.srcad_44.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.qclass_field_4.setText("")
        self.info_8.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
    # retranslateUi

    def ethpage(self, packet):

        self.pressed = packet
        self.stackedWidget.setCurrentIndex(2)

    def ippage(self):

        self.stackedWidget.setCurrentIndex(3)

    def udppage(self):

        self.stackedWidget.setCurrentIndex(4)

    def nxtpage(self):

        if self.pressed == 'ntp':

                self.stackedWidget.setCurrentIndex(5)
        elif self.pressed == 'dns':

                self.stackedWidget.setCurrentIndex(6)
        elif self.pressed == 'ssdp':

                self.stackedWidget.setCurrentIndex(7)

    def chosen(self):

        text = self.sentop.currentText()

        if text == 'New Packet':

                self.stackedWidget.setCurrentIndex(1)