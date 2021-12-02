# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home2XcfRtQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import drafting
from typing import Text
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from paatSecurity import validateEthAddr, validateIPAddr, validateIntOnly
from sendPacket import sendPacketClass, displaySent
from receiver import startSniffing, displayReceiveLog
from ssdpWorker import WorkerThread
from dnsWorker import WorkerThreadDns
from NtpWorker import WorkerThreadNTP




import source_rc

sPacket = sendPacketClass()
sPacketType = 0

#####################################################
## Main Window Object
#####################################################
class Ui_OtherWindow(object):

    def setupUi(self, MainWindow, darkmodes,currentUser):

        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1077)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")

        self.currentUser = currentUser
#####################################################
## Central Widget Object (all page contents)
#####################################################
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.choice = "nope"

#####################################################
## Side menu Object (side menu icons and buttons )
#####################################################
        self.side_menu = QFrame(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setGeometry(QRect(0, 0, 61, 1081))
        self.side_menu.setMinimumSize(QSize(63, 0))
        self.side_menu.setMaximumSize(QSize(200, 16777215))
        self.side_menu.setStyleSheet(u"background: rgb(1, 58, 83)")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.side_menu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.darkmode = darkmodes

## HOME ICON ##
        self.home_icon = QPushButton(self.side_menu)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setGeometry(QRect(-10, 80, 121, 81))
        self.home_icon.setMinimumSize(QSize(100, 0))
        self.home_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/homeic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_icon.setIcon(icon)
        self.home_icon.setIconSize(QSize(55, 55))
        self.home_icon.clicked.connect(self.homepg)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.home_icon)


## SENT ICON ##
        self.sent_icon = QPushButton(self.side_menu)
        self.sent_icon.setObjectName(u"sent_icon")
        self.sent_icon.setGeometry(QRect(-10, 220, 121, 81))
        self.sent_icon.setMinimumSize(QSize(100, 0))
        self.sent_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sendic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sent_icon.setIcon(icon1)
        self.sent_icon.setIconSize(QSize(55, 55))
        self.sent_icon.clicked.connect(self.gosent)
        
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sent_icon)


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
        self.recieve_icon.clicked.connect(self.gorecvd)
        
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.recieve_icon)


## INFO ICON ##
        self.info_icon = QPushButton(self.side_menu)
        self.info_icon.setObjectName(u"info_icon")
        self.info_icon.setGeometry(QRect(-10, 760, 121, 81))
        self.info_icon.setMinimumSize(QSize(100, 0))
        self.info_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_icon.setIcon(icon3)
        self.info_icon.setIconSize(QSize(55, 55))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.info_icon)

        self.info_icon.clicked.connect(self.printHelp);


## DRAFTS ICON ##
        self.drafts_icon = QPushButton(self.side_menu)
        self.drafts_icon.setObjectName(u"drafts_icon")
        self.drafts_icon.setGeometry(QRect(0, 510, 121, 81))
        self.drafts_icon.setMinimumSize(QSize(100, 0))
        self.drafts_icon.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/editic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drafts_icon.setIcon(icon4)
        self.drafts_icon.setIconSize(QSize(55, 55))
        self.drafts_icon.clicked.connect(self.godraft)
        self.drafts_icon.clicked.connect(self.getDrafts)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.drafts_icon)

        self.home_icon.raise_()
        self.recieve_icon.raise_()
        self.info_icon.raise_()
        self.drafts_icon.raise_()
        self.sent_icon.raise_()

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

        self.horizontalLayout_2 = QHBoxLayout(self.top_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

## MENU ICON ##
        self.side_menu_toggle = QFrame(self.top_menu)
        self.side_menu_toggle.setObjectName(u"side_menu_toggle")
        self.side_menu_toggle.setGeometry(QRect(0, 0, 100, 61))
        self.side_menu_toggle.setMinimumSize(QSize(63, 0))
        self.side_menu_toggle.setMaximumSize(QSize(100, 16777215))
        self.side_menu_toggle.setStyleSheet(u"background: transparent;")
        self.side_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.side_menu_toggle.setFrameShadow(QFrame.Raised)
        self.side_menu_toggle.raise_()

        self.menu_icon = QPushButton(self.side_menu_toggle)
        self.menu_icon.setObjectName(u"menu_icon")
        self.menu_icon.setGeometry(QRect(1, 5, 50, 50))
        self.menu_icon.setMinimumSize(QSize(50, 0))
        self.menu_icon.setMaximumSize(QSize(100, 16777215))
        self.menu_icon.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_icon.setIcon(icon5)
        self.menu_icon.setIconSize(QSize(55, 55))

        self.menu_icon.clicked.connect(lambda: self.slideleft())

        self.horizontalLayout_2.addWidget(self.menu_icon)


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
        self.settings_icon.clicked.connect(self.gosettings)

        self.horizontalLayout_2.addWidget(self.settings_icon)

## CONTACT ICON ##
        self.contact_icon = QPushButton(self.top_menu)
        self.contact_icon.setObjectName(u"contact_icon")
        self.contact_icon.setGeometry(QRect(730, 10, 91, 51))
        self.contact_icon.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/contacts.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contact_icon.setIcon(icon8)
        self.contact_icon.setIconSize(QSize(45, 45))
        self.contact_icon.clicked.connect(self.goconts)

        self.horizontalLayout_2.addWidget(self.contact_icon)


#####################################################
## Stacked Widget Object (contains all pages and their contents)
#####################################################

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(60, 60, 1851, 1021))
        
        
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
        self.recieve_pack.clicked.connect(self.recieve_page)

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

        self.def_eth.clicked.connect(self.default_eth)

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
        self.srcad.setToolTip("<b style='background:white; font:9pt; color:black;'>The MAC address of the source machine. [6 Bytes]</b>")
        self.dstad = QLabel(self.ETH)
        self.dstad.setObjectName(u"dstad")
        self.dstad.setGeometry(QRect(980, 450, 211, 21))
        self.dstad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dstad.setToolTip("<b style='background:white; font:9pt; color:black;'>The MAC address of the destination machine. [6 Bytes]</b>")
        self.ty = QLabel(self.ETH)
        self.ty.setObjectName(u"ty")
        self.ty.setGeometry(QRect(660, 660, 161, 21))
        self.ty.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.ty.setToolTip("<b style='background:white; font:9pt; color:black;'>Indicates the encapsulated protocol in frame payload and determines how it is processed when recieved by the data link layer. [2 Octet]</b>")
        
        self.back_eth = QPushButton(self.ETH)
        self.back_eth.setObjectName(u"back_eth")
        self.back_eth.setGeometry(QRect(130, 80, 241, 91))
        self.back_eth.setAutoFillBackground(False)
        self.back_eth.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_eth.setIcon(icon9)
        self.back_eth.setIconSize(QSize(52, 52))

        self.stackedWidget.addWidget(self.ETH)

        self.nxt_eth.clicked.connect(self.validateEth)
        
        self.back_eth.clicked.connect(self.goback)
        

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
        self.versn.setToolTip("<b style='background:white; font: 9pt; color:black;'>It is a version indicator, in IPv4 it is set to 0100 which is 4 in binary. [4 Bits]</b>")
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
        self.ihl.setToolTip("<b style='background:white; font:9pt; color:black;'>Shows how many 32-bit words are present in the header. [4 Bits]</b>")
        self.tos = QLabel(self.IP)
        self.tos.setObjectName(u"tos")
        self.tos.setGeometry(QRect(480, 320, 91, 41))
        self.tos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.tos.setToolTip("<b style='background:white; font: 9pt; color:black;'>Provides features like quality of service for data streaming and handling datagrams.</b>")
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
        self.length.setToolTip("<b style='background:white; font: 9pt; color:black;'>Size of data being sent, it is measured in bytes and can be used to calculate the payload dimension with IHL. [20-65535 Bits] </b>")
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
        self.idfn.setToolTip("<b style='background:white; font: 9pt; color:black;'> It is packet used to identify fragments of an IP datagram.</b>")
        self.flgs = QLabel(self.IP)
        self.flgs.setObjectName(u"flgs")
        self.flgs.setGeometry(QRect(650, 440, 91, 41))
        self.flgs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.flgs.setToolTip("<b style='background:white; font: 9pt; color:black;'>Helps you to control and identify fragments, 0 = reserved/0 - 1 = do not fragment - 2 = more fragment. [3 Bits]</b>")
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
        self.fragoff.setToolTip("<b style='background:white; font: 9pt; color:black;'>Represents the number of Data Bytes ahead of the particular fragment in the specific Datagram. [8-65528 Bytes]</b>")
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
        self.ttl.setToolTip("<b style='background:white; font: 9pt; color:black;'>Indicates the maximum time the Datagram will be live in the internet system. [8 Bits]</b>")
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
        self.protcl.setToolTip("<b style='background:white; font: 9pt; color:black;'>Reserved to denote that internet protocol is used in the latter portion of the Datagram. </b>")
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
        self.hdrchksm.setToolTip("<b style='background:white; font: 9pt; color:black;'>Used to check the header for any errors. [16 Bits]</b>")
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
        self.opts.setToolTip("<b style='background:white; font: 9pt; color:black;'>An optional field used when the value of IHL is set to greater than 5, it contains values and settings related with security, record route and time stamp.</b>")
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
        self.srcad_txt.setToolTip("<b style='background:white; font: 9pt; color:black;'>The MAC address of the source machine. [6 Bytes]</b>")
        self.dstad_txt = QLabel(self.IP)
        self.dstad_txt.setObjectName(u"dstad_txt")
        self.dstad_txt.setGeometry(QRect(1290, 500, 191, 41))
        self.dstad_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 15pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.dstad_txt.setToolTip("<b style='background:white; font: 9pt; color:black;'>The MAC address of the destination machine. [6 Bytes]</b>")
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

        self.def_ip.clicked.connect(self.default_ip)

        self.info_2 = QLabel(self.IP)
        self.info_2.setObjectName(u"info_2")
        self.info_2.setGeometry(QRect(250, 870, 351, 16))
        self.info_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")

        self.back_ip = QPushButton(self.IP)
        self.back_ip.setObjectName(u"back_ip")
        self.back_ip.setGeometry(QRect(130, 80, 241, 91))
        self.back_ip.setAutoFillBackground(False)
        self.back_ip.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_ip.setIcon(icon9)
        self.back_ip.setIconSize(QSize(52, 52))

        self.stackedWidget.addWidget(self.IP)

        self.nxt_ip.clicked.connect(self.validateIP)
        self.back_ip.clicked.connect(self.goeth)


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
        self.srcad_txtt.setToolTip("<b style='background:white; color:black;'>The number used to identify the process sending data.</b>")
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
        self.chksm_text.setToolTip("<b style='background:white; color:black;'> Mechanism to determine the integrity of data transmitted over network.</b>")
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
        self.leng_txt.setToolTip("<b style='background:white; color:black;'>Size of data being sent, it is measured in bytes. [8-65535 bytes]</b>")
        self.dst_txt = QLabel(self.UDP)
        self.dst_txt.setObjectName(u"dst_txt")
        self.dst_txt.setGeometry(QRect(420, 530, 181, 41))
        self.dst_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dst_txt.setToolTip("<b style='background:white; color:black;'>The number used to identify the process recieving data.</b>")
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

        self.back_udp = QPushButton(self.UDP)
        self.back_udp.setObjectName(u"back_udp")
        self.back_udp.setGeometry(QRect(130, 80, 241, 91))
        self.back_udp.setAutoFillBackground(False)
        self.back_udp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_udp.setIcon(icon9)
        self.back_udp.setIconSize(QSize(52, 52))

        self.def_udp.clicked.connect(self.default_udp)

        self.stackedWidget.addWidget(self.UDP)
        
        self.nxt_udp.clicked.connect(self.setUDP)
        self.nxt_udp.clicked.connect(self.nxtpage)
        self.back_udp.clicked.connect(self.ippage)


## Page 6 -  NTP PACKET labels, inputs and buttons ##

        self.NTP = QWidget()
        self.NTP.setObjectName(u"NTP")
        self.NTP.setStyleSheet(u"background-image: url(:/bg1/ntp.png);")
        self.send_ntp = QPushButton(self.NTP)
        self.send_ntp.setObjectName(u"send_ntp")
        self.send_ntp.setGeometry(QRect(1560, 680, 241, 91))
        self.send_ntp.setAutoFillBackground(False)
        self.send_ntp.clicked.connect(self.setListValues)
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

        self.def_ntp = QPushButton(self.NTP)
        self.def_ntp.setObjectName(u"def_ntp")
        self.def_ntp.setGeometry(QRect(200, 860, 151, 41))
        self.def_ntp.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")

        self.def_ntp.clicked.connect(self.default_ntp)

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
        self.precision_label = QLabel(self.NTP)
        self.precision_label.setObjectName(u"precision_label")
        self.precision_label.setGeometry(QRect(810, 470, 141, 41))
        self.precision_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.precision_label.setToolTip("<b style='background:white; color:black;'>The smallest possible increase of time that can be experienced by a program.</b>")
        self.dispersion_label = QLabel(self.NTP)
        self.dispersion_label.setObjectName(u"dispersion_label")
        self.dispersion_label.setGeometry(QRect(1130, 470, 141, 41))
        self.dispersion_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dispersion_label.setToolTip("<b style='background:white; color:black;'>The maximum difference recorded between the NTP client and the NTP server. [seconds]</b>")
        self.delay_label = QLabel(self.NTP)
        self.delay_label.setObjectName(u"delay_label")
        self.delay_label.setGeometry(QRect(970, 470, 141, 41))
        self.delay_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.delay_label.setToolTip("<b style='background:white; color:black;'>The round-trip delay of a timing message passed from client to server and back again.</b>")
        self.poll_label = QLabel(self.NTP)
        self.poll_label.setObjectName(u"poll_label")
        self.poll_label.setGeometry(QRect(650, 470, 141, 41))
        self.poll_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.poll_label.setToolTip("<b style='background:white; color:black;'>The process sends NTP packets at intervals determined by the clock discipline algorithm to increase accuracy and decrease network overhead.</b>")
        self.id_label = QLabel(self.NTP)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(650, 590, 621, 41))
        self.id_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.id_label.setToolTip("<b style='background:white; color:black;'>It identifies the source of time in a timestamp.</b>")
        self.recieve_label = QLabel(self.NTP)
        self.recieve_label.setObjectName(u"recieve_label")
        self.recieve_label.setGeometry(QRect(970, 830, 141, 41))
        self.recieve_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.recieve_label.setToolTip("<b style='background:white; color:black;'>This value is the time at which the client request arrived at the server in 64-bit time-stamp format.</b>")
        self.reference_label = QLabel(self.NTP)
        self.reference_label.setObjectName(u"reference_label")
        self.reference_label.setGeometry(QRect(650, 830, 141, 41))
        self.reference_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.reference_label.setToolTip("<b style='background:white; color:black;'>This field is the time the system clock was last set or corrected, in 64-bit time-stamp format.</b>")
        self.origin_label = QLabel(self.NTP)
        self.origin_label.setObjectName(u"origin_label")
        self.origin_label.setGeometry(QRect(810, 830, 141, 41))
        self.origin_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.origin_label.setToolTip("<b style='background:white; color:black;'>This value is the time at which the request departed the client for the server, in 64-bit time-stamp format.</b>")
        self.sent_label = QLabel(self.NTP)
        self.sent_label.setObjectName(u"sent_label")
        self.sent_label.setGeometry(QRect(1130, 830, 141, 41))
        self.sent_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.sent_label.setToolTip("<b style='background:white; color:black;'>This value is the time at which the server reply departed the server, in 64-bit time-stamp format.</b>")
        self.referenceid_label = QLabel(self.NTP)
        self.referenceid_label.setObjectName(u"referenceid_label")
        self.referenceid_label.setGeometry(QRect(650, 710, 621, 41))
        self.referenceid_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.referenceid_label.setToolTip("<b style='background:white; color:black;'>This value is a four-character ASCII code that describes the external reference source. </b>")
        self.mode_label = QLabel(self.NTP)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setGeometry(QRect(970, 350, 141, 41))
        self.mode_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.mode_label.setToolTip("<b style='background:white; color:black;'>NTP packet mode\n The values of the Mode field follow:\n0: Reserved \n 1: Symmetric active\n2: Symmetric passive\n3: Client\n4: Server\n5: Broadcast\n6: NTP control message\n7: Reserved for private use\n [3 bits]</b>")
        self.stratum_label = QLabel(self.NTP)
        self.stratum_label.setObjectName(u"stratum_label")
        self.stratum_label.setGeometry(QRect(1130, 350, 141, 41))
        self.stratum_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.stratum_label.setToolTip("<b style='background:white; color:black;'>Stratum level of the time source (8 bits) The values of the Stratum field follow:\n0: Unspecified or invalid\n1: Primary server\n2â€“15: Secondary server\n16: Unsynchronized\n17â€“255: Reserved\n [8 bits]</b>")
        self.version_label = QLabel(self.NTP)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(810, 350, 141, 41))
        self.version_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.version_label.setToolTip("<b style='background:white; color:black;'>NTP Version Number. [3 bits]</b>")
        self.leap_label = QLabel(self.NTP)
        self.leap_label.setObjectName(u"leap_label")
        self.leap_label.setGeometry(QRect(650, 350, 141, 41))
        self.leap_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.leap_label.setToolTip("<b style='background:white; color:black;'>Leap Indicator\nThis field indicates whether the last minute of the current day is to have a leap second applied. The field values follow:\n0: No leap second adjustment\n1: Last minute of the day has 61 seconds\n2: Last minute of the day has 59 seconds\n3: Clock is unsynchronized\n[2 bits]</b>")
        self.info_6 = QLabel(self.NTP)
        self.info_6.setObjectName(u"info_6")
        self.info_6.setGeometry(QRect(200, 910, 351, 16))
        self.info_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.back_ntp = QPushButton(self.NTP)
        self.back_ntp.setObjectName(u"back_ntp")
        self.back_ntp.setGeometry(QRect(130, 80, 241, 91))
        self.back_ntp.setAutoFillBackground(False)
        self.back_ntp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_ntp.setIcon(icon9)
        self.back_ntp.setIconSize(QSize(52, 52))
        self.draft_ntp.clicked.connect(self.saveDraftNTP)
        self.stackedWidget.addWidget(self.NTP)

        self.back_ntp.clicked.connect(self.udppage)
        self.draft_ntp.clicked.connect(self.makeDraft)

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
        self.send_dns.clicked.connect(self.setListValues)
        self.send_dns.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")

        self.def_dns = QPushButton(self.DNS)
        self.def_dns.setObjectName(u"def_dns")
        self.def_dns.setGeometry(QRect(200, 860, 151, 41))
        self.def_dns.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")

        self.def_dns.clicked.connect(self.default_dns)

        self.qtype_label = QLabel(self.DNS)
        self.qtype_label.setObjectName(u"qtype_label")
        self.qtype_label.setGeometry(QRect(790, 650, 141, 41))
        self.qtype_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qtype_label.setToolTip("<b style='background:white; color:black;'>A code which specifies the type of the query. [2 Octets]</b>")
        self.qclass_label = QLabel(self.DNS)
        self.qclass_label.setObjectName(u"qclass_label")
        self.qclass_label.setGeometry(QRect(1010, 650, 141, 41))
        self.qclass_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qclass_label.setToolTip("<b style='background:white; color:black;'>A code which specifies the class of the query. [2 Octets]</b>")
        self.qname_field = QLineEdit(self.DNS)
        self.qname_field.setObjectName(u"qname_field")
        self.qname_field.setGeometry(QRect(460, 370, 1021, 61))
        self.qname_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.qname_label = QLabel(self.DNS)
        self.qname_label.setObjectName(u"qname_label")
        self.qname_label.setGeometry(QRect(460, 430, 1021, 41))
        self.qname_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.qname_label.setToolTip("<b style='background:white; color:black;'>Minimization of Qname is a privacy oriented feature which tries limiting sending of full domain destination to the root nameservers.</b>")
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

        self.back_dns = QPushButton(self.DNS)
        self.back_dns.setObjectName(u"back_dns")
        self.back_dns.setGeometry(QRect(130, 80, 241, 91))
        self.back_dns.setAutoFillBackground(False)
        self.back_dns.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_dns.setIcon(icon9)
        self.back_dns.setIconSize(QSize(52, 52))
        
        self.stackedWidget.addWidget(self.DNS)
        self.draft_dns.clicked.connect(self.saveDraftDNS)
        self.back_dns.clicked.connect(self.udppage)
        self.draft_dns.clicked.connect(self.makeDraft)

## Page 7 -  SSDP PACKET labels, inputs and buttons ##

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
        self.draft_dns_2.clicked.connect(self.saveDraftSSDP)

        self.send_dns_2 = QPushButton(self.SSDP)
        self.send_dns_2.setObjectName(u"send_dns_2")
        self.send_dns_2.setGeometry(QRect(1560, 680, 241, 91))
        self.send_dns_2.setAutoFillBackground(False)
        self.send_dns_2.clicked.connect(self.setListValues)
        self.send_dns_2.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")

        self.def_ssdp = QPushButton(self.SSDP)
        self.def_ssdp.setObjectName(u"def_ssdp")
        self.def_ssdp.setGeometry(QRect(200, 860, 151, 41))
        self.def_ssdp.setStyleSheet(u"font: 20pt \"Franklin Gothic Cond\";\n"
"background: rgb(79, 192, 232);\n"
"color: rgb(255, 255, 255);")

        self.def_ssdp.clicked.connect(self.default_ssdp)

        self.st_label = QLabel(self.SSDP)
        self.st_label.setObjectName(u"st_label")
        self.st_label.setGeometry(QRect(770, 700, 141, 41))
        self.st_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.st_label.setToolTip("<b style='background:white; color:black;'>The search target of the service the search request is attempting to discover.</b>")
        self.mx_field = QLineEdit(self.SSDP)
        self.mx_field.setObjectName(u"mx_field")
        self.mx_field.setGeometry(QRect(1020, 490, 371, 61))
        self.mx_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.mx_label = QLabel(self.SSDP)
        self.mx_label.setObjectName(u"mx_label")
        self.mx_label.setGeometry(QRect(1020, 550, 141, 41))
        self.mx_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.mx_label.setToolTip("<b style='background:white; color:black;'>The maximum seconds to delay a response.</b>")
        self.st_field = QLineEdit(self.SSDP)
        self.st_field.setObjectName(u"st_field")
        self.st_field.setGeometry(QRect(770, 640, 371, 61))
        self.st_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.port_label = QLabel(self.SSDP)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setGeometry(QRect(1020, 420, 141, 41))
        self.port_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.port_label.setToolTip("<b style='background:white; color:black;'>The port the message will be sent to.</b>")
        self.man_field = QLineEdit(self.SSDP)
        self.man_field.setObjectName(u"man_field")
        self.man_field.setGeometry(QRect(550, 490, 371, 61))
        self.man_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.man_label = QLabel(self.SSDP)
        self.man_label.setObjectName(u"man_label")
        self.man_label.setGeometry(QRect(550, 550, 141, 41))
        self.man_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.man_label.setToolTip("<b style='background:white; color:black;'>The message type, for an M-Search  is always ssdp:discover.</b>")
        self.port_field = QLineEdit(self.SSDP)
        self.port_field.setObjectName(u"port_field")
        self.port_field.setGeometry(QRect(1020, 360, 371, 61))
        self.port_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.host_label = QLabel(self.SSDP)
        self.host_label.setObjectName(u"host_label")
        self.host_label.setGeometry(QRect(550, 420, 141, 41))
        self.host_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.host_label.setToolTip("<b style='background:white; color:black;'>The host the message will be sent to.</b>")
        self.host_field = QLineEdit(self.SSDP)
        self.host_field.setObjectName(u"host_field")
        self.host_field.setGeometry(QRect(550, 360, 371, 61))
        self.host_field.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.info_8 = QLabel(self.SSDP)
        self.info_8.setObjectName(u"info_8")
        self.info_8.setGeometry(QRect(200, 910, 351, 16))
        self.info_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Cond\";\n"
"background: transparent;")

        self.back_ssdp = QPushButton(self.SSDP)
        self.back_ssdp.setObjectName(u"back_ssdp")
        self.back_ssdp.setGeometry(QRect(130, 80, 241, 91))
        self.back_ssdp.setAutoFillBackground(False)
        self.back_ssdp.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_ssdp.setIcon(icon9)
        self.back_ssdp.setIconSize(QSize(52, 52))
        
        self.stackedWidget.addWidget(self.SSDP)

        self.back_ssdp.clicked.connect(self.udppage)
        self.draft_dns_2.clicked.connect(self.makeDraft)

## Page 8 - Settings ##

        self.Account = QWidget()
        self.Account.setObjectName(u"Account")
        self.Account.setStyleSheet(u"background: url(:/bg1/settingss.png);")
        self.darkm = QPushButton(self.Account)
        self.darkm.setObjectName(u"darkm")
        self.darkm.setGeometry(QRect(930, 720, 111, 101))
        self.darkm.setAutoFillBackground(False)
        self.darkm.setStyleSheet(u"background: transparent;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.darkm.setIcon(icon9)
        self.darkm.setIconSize(QSize(86, 76))
        self.darkm.setCheckable(True)
        self.darkm.setChecked(True)
        self.name = QLabel(self.Account)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(750, 320, 131, 51))
        self.name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 33pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.accpic = QLabel(self.Account)
        self.accpic.setObjectName(u"accpic")
        self.accpic.setGeometry(QRect(420, 260, 251, 241))
        self.accpic.setStyleSheet(u"background: url(:/icons/account.png);\n"
"background-repeat: none;")
        self.usernamee = QLabel(self.Account)
        self.usernamee.setObjectName(u"usernamee")
        self.usernamee.setGeometry(QRect(750, 400, 161, 31))
        self.usernamee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.paswd = QLabel(self.Account)
        self.paswd.setObjectName(u"paswd")
        self.paswd.setGeometry(QRect(520, 640, 111, 21))
        self.paswd.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.settings1 = QLabel(self.Account)
        self.settings1.setObjectName(u"settings1")
        self.settings1.setGeometry(QRect(520, 750, 151, 31))
        self.settings1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.email1 = QLabel(self.Account)
        self.email1.setObjectName(u"email1")
        self.email1.setGeometry(QRect(520, 590, 71, 21))
        self.email1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  14pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.lightm = QPushButton(self.Account)
        self.lightm.setObjectName(u"lightm")
        self.lightm.setGeometry(QRect(760, 720, 111, 101))
        self.lightm.setAutoFillBackground(False)
        self.lightm.setStyleSheet(u"background: transparent;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lightm.setIcon(icon10)
        self.lightm.setIconSize(QSize(86, 76))
        self.lightm.setCheckable(True)
        self.lightm.setChecked(True)
        self.save = QPushButton(self.Account)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(710, 850, 271, 81))
        self.save.setAutoFillBackground(False)
        self.save.setStyleSheet(u"font: 18pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.cancel = QPushButton(self.Account)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(1010, 880, 101, 28))
        self.cancel.setStyleSheet(u"background: transparent;\n"
"font: 12pt \"Franklin Gothic Raw\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.em_txt = QLabel(self.Account)
        self.em_txt.setObjectName(u"em_txt")
        self.em_txt.setGeometry(QRect(680, 580, 411, 31))
        self.psd_txt = QLabel(self.Account)
        self.psd_txt.setObjectName(u"psd_txt")
        self.psd_txt.setGeometry(QRect(680, 640, 411, 31))
        self.em_txt.setStyleSheet(u"background: url(:/bg1/settingss.png);")
        self.psd_txt.setStyleSheet(u"background: url(:/bg1/settingss.png);")
        self.stackedWidget.addWidget(self.Account)

        self.darkm.clicked.connect(self.changebg)
        self.lightm.clicked.connect(self.changedbg)

        self.save.clicked.connect(self.homepg)

        self.psd_txt.raise_()
        self.em_txt.raise_()
        self.darkm.raise_()
        self.name.raise_()
        self.accpic.raise_()
        self.usernamee.raise_()
        self.paswd.raise_()
        self.settings1.raise_()
        self.email1.raise_()
        self.lightm.raise_()
        self.save.raise_()
        self.cancel.raise_()




## Page 9 - Drafts Page ##

        self.drafts_pg = QWidget()
        self.drafts_pg.setObjectName(u"drafts_pg")
        self.drafts_pg.setStyleSheet(u"background-image: url(:/bg1/drafts.png);")
        self.tableDrafts = QTableWidget(self.drafts_pg)
        if (self.tableDrafts.columnCount() < 6):
            self.tableDrafts.setColumnCount(6)
        self.tableDrafts.setObjectName(u"tableDrafts")
        self.tableDrafts.setGeometry(QRect(260, 320, 1351, 561))
        self.tableDrafts.setStyleSheet(u"background: rgb(221, 221, 221);\n""font: 8pt \"Franklin Gothic Demi\";\n""color: rgb(1, 58, 83);")
        self.tableDrafts.setAlternatingRowColors(True)
        self.tableDrafts.setSortingEnabled(True)

        self.tableDrafts.setColumnCount(6)

        self.tableDrafts.setHorizontalHeaderLabels(["Name", "Date Created", "Initial Size", "Reciever Address", "Edit", "Send"])
        self.tableDrafts.horizontalHeader().setDefaultSectionSize(220)
        self.tableDrafts.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableDrafts.verticalHeader().setCascadingSectionResizes(True)
        self.stackedWidget.addWidget(self.drafts_pg)

## Page 10 - Sent Page ##

        self.sent_pg = QWidget()
        self.sent_pg.setObjectName(u"sent_pg")
        self.sent_pg.setStyleSheet(u"background-image: url(:/bg1/sent.png);")
        self.tableSent = QTableWidget(self.sent_pg)
        if (self.tableSent.columnCount() < 7):
            self.tableSent.setColumnCount(7)
        self.tableSent.setObjectName(u"tableSent")
        self.tableSent.setGeometry(QRect(260, 320, 1351, 561))
        self.tableSent.setStyleSheet(u"background: rgb(221, 221, 221);\n""font: 8pt \"Franklin Gothic Demi\";\n""color: rgb(1, 58, 83);")
        self.tableSent.setAlternatingRowColors(True)
        self.tableSent.setSortingEnabled(True)
        self.tableSent.setColumnCount(7) 
        self.tableSent.setHorizontalHeaderLabels(["Name", "Date Created", "Date Sent", "Initial Size", "Reciever Address", "Edit", "Send Again"])
        self.tableSent.horizontalHeader().setDefaultSectionSize(220)
        self.tableSent.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableSent.verticalHeader().setCascadingSectionResizes(True)
        self.stackedWidget.addWidget(self.sent_pg)

## Page 11 - Recieved Page ##

        self.recvd_pg = QWidget()
        self.recvd_pg.setObjectName(u"recvd_pg")
        self.recvd_pg.setStyleSheet(u"background-image: url(:/bg1/recvd.png);")
        self.tableRecvd = QTableWidget(self.recvd_pg)
        if (self.tableRecvd.columnCount() < 5):
            self.tableRecvd.setColumnCount(5)
        self.tableRecvd.setObjectName(u"tableRecvd")
        self.tableRecvd.setGeometry(QRect(190, 270, 1051, 561))
        self.tableRecvd.setStyleSheet(u"background: rgb(221, 221, 221);\n""font: 8pt \"Franklin Gothic Demi\";\n""color: rgb(1, 58, 83);")
        self.tableRecvd.setAlternatingRowColors(True)
        self.tableRecvd.setSortingEnabled(True) 
        self.tableRecvd.setColumnCount(5)
        self.tableRecvd.setHorizontalHeaderLabels(["Reciever's Address", "Date Recieved", "Initial Size", "Recieved Size", "Amplification Factor"])
        self.tableRecvd.horizontalHeader().setDefaultSectionSize(220)
        self.tableRecvd.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableRecvd.verticalHeader().setCascadingSectionResizes(True)

        self.rcvAd_txt = QLabel(self.recvd_pg)
        self.rcvAd_txt.setObjectName(u"rcvAd_txt")
        self.rcvAd_txt.setGeometry(QRect(1420, 460, 151, 21))
        self.rcvAd_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  14pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.rcvAd = QLineEdit(self.recvd_pg)
        self.rcvAd.setObjectName(u"rcvAd")
        self.rcvAd.setGeometry(QRect(1320, 400, 361, 51))
        self.rcvAd.setStyleSheet(u"background: rgb(183, 206, 212);")
        self.rcvBox = QLCDNumber(self.recvd_pg)
        self.rcvBox.setObjectName(u"rcvBox")
        self.rcvBox.setGeometry(QRect(1550, 560, 131, 61))
        self.rcvBox.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.intBox = QLCDNumber(self.recvd_pg)
        self.intBox.setObjectName(u"intBox")
        self.intBox.setGeometry(QRect(1280, 560, 131, 61))
        self.intBox.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.ampBox = QLCDNumber(self.recvd_pg)
        self.ampBox.setObjectName(u"ampBox")
        self.ampBox.setGeometry(QRect(1420, 700, 131, 61))
        self.ampBox.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"")
        self.ampBox.setFrameShape(QFrame.NoFrame)
        self.intSz = QLabel(self.recvd_pg)
        self.intSz.setObjectName(u"intSz")
        self.intSz.setGeometry(QRect(1300, 640, 91, 21))
        self.intSz.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.rcvSz = QLabel(self.recvd_pg)
        self.rcvSz.setObjectName(u"rcvSz")
        self.rcvSz.setGeometry(QRect(1560, 640, 121, 21))
        self.rcvSz.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.ampFac = QLabel(self.recvd_pg)
        self.ampFac.setObjectName(u"ampFac")
        self.ampFac.setGeometry(QRect(1410, 780, 171, 21))
        self.ampFac.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")

        self.stackedWidget.addWidget(self.recvd_pg) 
     

## Page 12 - Contacts Page ##

        self.contacts = QWidget()
        self.contacts.setObjectName(u"contacts")
        self.contacts.setStyleSheet(u"background-image: url(:/bg1/contactss.png);")
        self.tableCont = QTableWidget(self.contacts)
        if (self.tableCont.columnCount() < 2):
            self.tableCont.setColumnCount(2)
        self.tableCont.setObjectName(u"tableCont")
        self.tableCont.setGeometry(QRect(480, 290, 461, 511))
        self.tableCont.setStyleSheet(u"background: rgb(221, 221, 221);\n""font: 8pt \"Franklin Gothic Demi\";\n""color: rgb(1, 58, 83);")
        self.tableCont.setAlternatingRowColors(True)
        self.tableCont.setSortingEnabled(True)
        self.tableCont.setColumnCount(2) 
        self.tableCont.setHorizontalHeaderLabels(["Name", "Address"])
        self.tableCont.horizontalHeader().setDefaultSectionSize(220)
        self.tableCont.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableCont.verticalHeader().setCascadingSectionResizes(True)

        self.search_bar = QLineEdit(self.contacts)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(1130, 410, 361, 51))
        self.search_bar.setStyleSheet(u"background: rgb(183, 206, 212);")
        self.srch_txt = QLabel(self.contacts)
        self.srch_txt.setObjectName(u"srch_txt")
        self.srch_txt.setGeometry(QRect(1240, 350, 161, 21))
        self.srch_txt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  17pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;")
        self.search_bt = QPushButton(self.contacts)
        self.search_bt.setObjectName(u"search_bt")
        self.search_bt.setGeometry(QRect(1510, 410, 81, 51))
        self.search_bt.setStyleSheet(u"background: transparent;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/search_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_bt.setIcon(icon11)
        self.search_bt.setIconSize(QSize(55, 55))
        self.edit_bt = QPushButton(self.contacts)
        self.edit_bt.setObjectName(u"edit_bt")
        self.edit_bt.setGeometry(QRect(1100, 610, 151, 81))
        self.edit_bt.setAutoFillBackground(False)
        self.edit_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.delete_bt = QPushButton(self.contacts)
        self.delete_bt.setObjectName(u"delete_bt")
        self.delete_bt.setGeometry(QRect(1380, 610, 151, 81))
        self.delete_bt.setAutoFillBackground(False)
        self.delete_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.save_bt = QPushButton(self.contacts)
        self.save_bt.setObjectName(u"save_bt")
        self.save_bt.setGeometry(QRect(1240, 720, 151, 81))
        self.save_bt.setAutoFillBackground(False)
        self.save_bt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")
        self.cancel_bt = QPushButton(self.contacts)
        self.cancel_bt.setObjectName(u"cancel_bt")
        self.cancel_bt.setGeometry(QRect(1270, 830, 93, 28))
        self.cancel_bt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  15pt \"Franklin Gothic Medium Cond\";\n"
"background: transparent;\n"
"text-decoration: underline;")
        self.stackedWidget.addWidget(self.contacts)   

## Page 13 - Autocreate Page ##

        self.autocreate = QWidget()
        self.autocreate.setObjectName(u"autocreate")
        self.autocreate.setStyleSheet(u"background: rgb(29, 108, 137);\n"
"background: url(:/bg1/autocreate.png);")
        self.dest_ad = QLineEdit(self.autocreate)
        self.dest_ad.setObjectName(u"dest_ad")
        self.dest_ad.setGeometry(QRect(400, 490, 361, 51))
        self.dest_ad.setStyleSheet(u"background: rgb(183, 206, 212);")
        self.src_adlabel = QLabel(self.autocreate)
        self.src_adlabel.setObjectName(u"src_adlabel")
        self.src_adlabel.setGeometry(QRect(400, 390, 161, 21))
        self.src_adlabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.dest_adlabel = QLabel(self.autocreate)
        self.dest_adlabel.setObjectName(u"dest_adlabel")
        self.dest_adlabel.setGeometry(QRect(400, 550, 211, 21))
        self.dest_adlabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.sorc_ad = QLineEdit(self.autocreate)
        self.sorc_ad.setObjectName(u"sorc_ad")
        self.sorc_ad.setGeometry(QRect(400, 330, 361, 51))
        self.sorc_ad.setStyleSheet(u"background: rgb(183, 197, 208);")
        self.pkt_type = QComboBox(self.autocreate)
        self.pkt_type.addItem("")
        self.pkt_type.addItem("")
        self.pkt_type.addItem("")
        self.pkt_type.setObjectName(u"pkt_type")
        self.pkt_type.setGeometry(QRect(1260, 370, 241, 91))
        self.pkt_type.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);")
        self.pkt_type.setEditable(False)
        self.pkt_type.setMaxVisibleItems(10)
        self.pkt_type.setFrame(True)
        self.pt_labrl = QLabel(self.autocreate)
        self.pt_labrl.setObjectName(u"pt_labrl")
        self.pt_labrl.setGeometry(QRect(1270, 370, 211, 91))
        self.pt_labrl.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);")
        self.packetsel = QLabel(self.autocreate)
        self.packetsel.setObjectName(u"packetsel")
        self.packetsel.setGeometry(QRect(1280, 330, 211, 21))
        self.packetsel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.send_pkt = QPushButton(self.autocreate)
        self.send_pkt.setObjectName(u"send_pkt")
        self.send_pkt.setGeometry(QRect(850, 640, 241, 91))
        self.send_pkt.setAutoFillBackground(False)
        self.send_pkt.setStyleSheet(u"font: 20pt \"Franklin Gothic Raw\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;\n"
"padding: 10px 10px;\n"
"background: rgb(0, 194, 203);\n"
"")     
        self.progressBar = QProgressBar(self.autocreate)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(750, 800, 471, 41))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.send_pkt.clicked.connect(self.startRandomSelection)
        self.pkt_type.activated.connect(self.chosen2)

        self.stackedWidget.addWidget(self.autocreate)

        if self.darkmode == True:
                self.changebg()


        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.side_menu.raise_()
        self.top_menu.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_icon.setText(QCoreApplication.translate("MainWindow", u" HOME", None))
        self.sent_icon.setText(QCoreApplication.translate("MainWindow", u"SENT", None))
        self.recieve_icon.setText(QCoreApplication.translate("MainWindow", u" RECIEVED", None))
        self.info_icon.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.drafts_icon.setText(QCoreApplication.translate("MainWindow", u"DRAFTS", None))
        self.menu_icon.setText("")
        self.settings_icon.setText("")
        self.contact_icon.setText("")
        self.sentl.setText(QCoreApplication.translate("MainWindow", u"     Send", None))
        self.sentop.setItemText(0, QCoreApplication.translate("MainWindow", u"Sent", None))
        self.sentop.setItemText(1, QCoreApplication.translate("MainWindow", u"Drafts", None))
        self.sentop.setItemText(2, QCoreApplication.translate("MainWindow", u"Autocreate", None))
        self.sentop.setItemText(3, QCoreApplication.translate("MainWindow", u"New Packet", None))

        self.src_adlabel.setText(QCoreApplication.translate("MainWindow", u"Source Address", None))
        self.dest_adlabel.setText(QCoreApplication.translate("MainWindow", u"Destination Address", None))
        self.pkt_type.setItemText(0, QCoreApplication.translate("MainWindow", u"DNS", None))
        self.pkt_type.setItemText(1, QCoreApplication.translate("MainWindow", u"NTP", None))
        self.pkt_type.setItemText(2, QCoreApplication.translate("MainWindow", u"SSDP", None))
        self.pkt_type.setCurrentText(QCoreApplication.translate("MainWindow", u"DNS", None))
        self.pt_labrl.setText(QCoreApplication.translate("MainWindow", u"Packet Type", None))
        self.packetsel.setText(QCoreApplication.translate("MainWindow", u"Select a Packet", None))
        self.send_pkt.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))

#if QT_CONFIG(tooltip)
        self.sentop.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sentop.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Send</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.sentop.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.def_ntp.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.def_dns.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.def_ssdp.setText(QCoreApplication.translate("MainWindow", u"Default", None))
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
        self.precision_label.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.dispersion_label.setText(QCoreApplication.translate("MainWindow", u"Dispersion", None))
        self.delay_label.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.poll_label.setText(QCoreApplication.translate("MainWindow", u"Poll", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.recieve_label.setText(QCoreApplication.translate("MainWindow", u"Recieve", None))
        self.reference_label.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.origin_label.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.sent_label.setText(QCoreApplication.translate("MainWindow", u"Sent", None))
        self.referenceid_label.setText(QCoreApplication.translate("MainWindow", u"Reference ID", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.stratum_label.setText(QCoreApplication.translate("MainWindow", u"Stratum", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.leap_label.setText(QCoreApplication.translate("MainWindow", u"Leap", None))
        self.info_6.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.draft_dns.setText(QCoreApplication.translate("MainWindow", u"Save As Draft", None))
        self.send_dns.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))
        self.qtype_label.setText(QCoreApplication.translate("MainWindow", u"Qtype", None))
        self.qclass_label.setText(QCoreApplication.translate("MainWindow", u"Qclass", None))
        self.qname_field.setText("")
        self.qname_label.setText(QCoreApplication.translate("MainWindow", u"Qname", None))
        self.qtype_field.setText("")
        self.qclass_field.setText("")
        self.info_7.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.draft_dns_2.setText(QCoreApplication.translate("MainWindow", u"Save As Draft", None))
        self.send_dns_2.setText(QCoreApplication.translate("MainWindow", u"Send Packet", None))
        self.st_label.setText(QCoreApplication.translate("MainWindow", u"ST", None))
        self.mx_field.setText("")
        self.mx_label.setText(QCoreApplication.translate("MainWindow", u"MX", None))
        self.st_field.setText("")
        self.port_label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.man_field.setText("")
        self.man_label.setText(QCoreApplication.translate("MainWindow", u"MAN", None))
        self.port_field.setText("")
        self.host_label.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.host_field.setText("")
        self.info_8.setText(QCoreApplication.translate("MainWindow", u"Place cursor over field name for more info on it!", None))
        self.darkm.setText("")
        self.back_eth.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_ip.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_udp.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_ntp.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_ssdp.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_dns.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.accpic.setText("")
        self.usernamee.setText(QCoreApplication.translate("MainWindow", u"@username", None))
        self.paswd.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.settings1.setText(QCoreApplication.translate("MainWindow", u"View Settings", None))
        self.email1.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lightm.setText("")
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.em_txt.setText("")
        self.psd_txt.setText("")
        self.rcvAd_txt.setText(QCoreApplication.translate("MainWindow", u"Reciever Address", None))
        self.intSz.setText(QCoreApplication.translate("MainWindow", u"Initial Size", None))
        self.rcvSz.setText(QCoreApplication.translate("MainWindow", u"Recieved Size", None))
        self.ampFac.setText(QCoreApplication.translate("MainWindow", u"Amplification Factor", None))
        self.srch_txt.setText(QCoreApplication.translate("MainWindow", u"Search Contact", None))
        self.search_bt.setText("")
        self.edit_bt.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_bt.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.save_bt.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancel_bt.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))

    # retranslateUi

    def homepg(self):

        self.stackedWidget.setCurrentIndex(0)

    def godraft(self):

        self.stackedWidget.setCurrentIndex(9)

    def gosent(self):

        self.stackedWidget.setCurrentIndex(10)
        displaySent(self)

    def gorecvd(self):

        self.stackedWidget.setCurrentIndex(11)
        displayReceiveLog(self)

    def goconts(self):

        self.stackedWidget.setCurrentIndex(12)    

    def gosettings(self):

        self.stackedWidget.setCurrentIndex(8)   


    def ethpage(self, packet):

        self.pressed = packet
        self.stackedWidget.setCurrentIndex(2)

    def ippage(self):

        self.stackedWidget.setCurrentIndex(3)

    def udppage(self):

        self.stackedWidget.setCurrentIndex(4)

    def netselect(self):

        self.stackedWidget.setCurrentIndex(1)        

    def nxtpage(self):

        if self.pressed == 'ntp':
                self.sPacketType = 3
                self.stackedWidget.setCurrentIndex(5)
        elif self.pressed == 'dns':
                self.sPacketType = 1
                self.stackedWidget.setCurrentIndex(6)
        elif self.pressed == 'ssdp':
                self.sPacketType = 2
                self.stackedWidget.setCurrentIndex(7)

    def validateEth(self):
        nextpage = 0

        if (validateEthAddr(self.source.text()) == False):
                self.source.setText("")
                nextpage = 1
                
        if (validateEthAddr(self.dest.text()) == False):
                self.dest.setText("")
                nextpage = 1

        if(nextpage == 0):
                self.setEthernet()
                self.ippage()

    def validateIP(self):
        nextPage =0

        if(validateIPAddr(self.srcad1.text()) == False):
                self.srcad1.setText("")
                nextPage = 1


        if(validateIPAddr(self.dstad1.text()) == False):
                self.dstad1.setText("")
                nextPage = 1 

        if(nextPage == 0):
                self.setIP()
                self.udppage()

    def setEthernet(self):
        #print("Ethernet values: "+self.source.text(),self.dest.text(),self.type.text())
        sPacket.setEthernet(self.source.text(),self.dest.text(),self.type.text())

    def setIP(self):  
        sPacket.setIP(self.vrsn_box.text(), self.IHL_box.text(),self.tos_box.text(),self.len_box.text(),self.id_box.text(),self.flags_box.text(),self.frag_box.text(),self.ttl_box.text(),self.prtcl_box.text(),self.chksum_box.text(),self.opts.text(),self.srcad1.text(),self.dstad1.text())  
    
    def setUDP(self):
        sPacket.setUDP(self.source_box.text(), self.dest_box.text(), self.chksum_box_2.text() )
    
    def setListValues(self):

        if(self.sPacketType == 1):
                self.tempListValues = [self.qname_field.text() , self.qtype_field.text(), self.qclass_field.text()]
                
        elif(self.sPacketType == 2):
                self.tempListValues = [self.host_field.text(),self.port_field.text(),self.man_field.text(),self.mx_field.text(),self.st_field.text()]
        elif(self.sPacketType == 3):
                self.tempListValues = [self.leap_field.text(),self.version_field.text(),self.mode_field.text(),self.stratum_field.text(),self.poll_field.text(),self.precision_field.text(),self.delay_field.text(),self.dispersion_field.text(),self.id_field.text(),self.referenceid_field.text(),self.reference_field.text(), self.origin_field.text(),self.recieve_field.text(),self.sent_field.text()]

        sPacket.setListValues(self.tempListValues,self.sPacketType)
        
        
    
    def chosen(self):

        text = self.sentop.currentText()

        if text == 'New Packet':

                self.stackedWidget.setCurrentIndex(1) 
            
        if text == 'Sent':
                self.stackedWidget.setCurrentIndex(10)

        if text == 'Drafts':
                self.stackedWidget.setCurrentIndex(9)

        if text == 'Autocreate':
                self.stackedWidget.setCurrentIndex(13)


    def chosen2(self):
    
        text = self.pkt_type.currentText()
        self.choice = text

        if text == 'DNS':

                self.pt_labrl.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\">DNS</p>", None))

        if text == 'SSDP':
                self.pt_labrl.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\">SSDP</p>", None))

        if text == 'NTP':
                self.pt_labrl.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\">NTP</p>", None))


    def default_eth(self):
        
        self.type.setText("2048")


    def default_ip(self):
        
        self.textEdit.setText("  ")
        self.chksum_box.setText("0")
        self.prtcl_box.setText("17")
        self.ttl_box.setText("64")
        self.frag_box.setText("0")
        self.flags_box.setText("0")
        self.id_box.setText("1")
        self.len_box.setText("0")
        self.tos_box.setText("0")
        self.IHL_box.setText("5")
        self.vrsn_box.setText("4")
        self.opts.setText("0")

    def default_udp(self):
        
        #self.source_box.setText(" ")
        self.chksum_box_2.setText("0")
        self.leng_box.setText("0")
        #self.dest_box.setText(" ")
        self.ovr_chksm.setChecked(True)
        self.ovr_lenval.setChecked(True)

    def default_ntp(self):
        
        self.leap_field.setText("Hello")
        self.version_field.setText("Hello")
        self.mode_field.setText("Hello")
        self.stratum_field.setText("Hello")
        self.poll_field.setText("Hello")
        self.precision_field.setText("Hello")
        self.delay_field.setText("Hello")
        self.dispersion_field.setText("Hello")
        self.id_field.setText("Hello")
        self.referenceid_field.setText("Hello")
        self.reference_field.setText("Hello")
        self.origin_field.setText("Hello")
        self.recieve_field.setText("Hello")
        self.sent_field.setText("Hello")

    def default_dns(self):
        
        self.qname_field.setText("google.com")
        self.qclass_field.setText("IN")
        self.qtype_field.setText("A")

    def default_ssdp(self):
        
        self.mx_field.setText("Hello")
        self.man_field.setText("Hello")
        self.st_field.setText("Hello")
        self.host_field.setText("Hello")

    def saveDraftSSDP(self):
        drafting.setVariablesEth(self.source.text(),self.dest.text(),self.type.text())
        drafting.setVariablesIP(self.srcad1.text(),self.dstad1.text(),self.ttl_box.text(),self.vrsn_box.text(),self.IHL_box.text(),self.tos_box.text(),self.id_box.text(),self.flags_box.text(),self.frag_box.text(),self.prtcl_box.text(),self.chksum_box.text(),self.opts.text(),self.len_box.text())
        drafting.setVariablesUDP(self.dest_box.text(),self.source_box.text(),self.chksum_box_2.text(),self.leng_box.text())
        drafting.setVariablesSSDP(self.mx_field.text(),self.st_field.text(),self.man_field.text(),self.port_field.text(),self.host_field.text())
        drafting.saveDraft("SSDP")
        

    def saveDraftDNS(self):
        drafting.setVariablesEth(self.source.text(),self.dest.text(),self.type.text())
        drafting.setVariablesIP(self.srcad1.text(),self.dstad1.text(),self.ttl_box.text(),self.vrsn_box.text(),self.IHL_box.text(),self.tos_box.text(),self.id_box.text(),self.flags_box.text(),self.frag_box.text(),self.prtcl_box.text(),self.chksum_box.text(),self.opts.text(),self.len_box.text())
        drafting.setVariablesUDP(self.dest_box.text(),self.source_box.text(),self.chksum_box_2.text(),self.leng_box.text())
        drafting.setVariablesDNS(self.qname_field.text(),self.qtype_field.text(),self.qclass_field.text())
        drafting.saveDraft("DNS") 

    def saveDraftNTP(self):
        drafting.setVariablesEth(self.source.text(),self.dest.text(),self.type.text())
        drafting.setVariablesIP(self.srcad1.text(),self.dstad1.text(),self.ttl_box.text(),self.vrsn_box.text(),self.IHL_box.text(),self.tos_box.text(),self.id_box.text(),self.flags_box.text(),self.frag_box.text(),self.prtcl_box.text(),self.chksum_box.text(),self.opts.text(),self.len_box.text())
        drafting.setVariablesUDP(self.dest_box.text(),self.source_box.text(),self.chksum_box_2.text(),self.leng_box.text())
        drafting.setVariablesNTP(self.mode_field.text(),self.dispersion_field.text(),self.id_field.text(),self.delay_field.text(),self.poll_field.text(),self.sent_field.text(),self.stratum_field.text(),self.version_field.text(),self.precision_field.text(),self.leap_field.text(),self.referenceid_field.text(),self.recieve_field.text(),self.origin_field.text(),self.reference_field.text())
        drafting.saveDraft("NTP")  


    def getDrafts(self):
        drafts = drafting.getDrafts()
        row = 0
        i = 0
        self.tableDrafts.setRowCount(len(drafts))
        for draft in drafts:
                self.tableDrafts.setItem(row,0,QtWidgets.QTableWidgetItem(draft[0]))
                self.tableDrafts.setItem(row,1,QtWidgets.QTableWidgetItem(draft[1].strftime('%Y-%m-%d')))
                self.tableDrafts.setItem(row,2,QtWidgets.QTableWidgetItem(draft[9]))
                self.tableDrafts.setItem(row,3,QtWidgets.QTableWidgetItem(draft[22]))
                self.btn_send = QPushButton('Send')
                self.tableDrafts.setCellWidget(row,4,self.btn_send)
                self.btn_send.clicked.connect(lambda: self.sendDraft(self.tableDrafts.currentRow()))
                row = row + 1

    def alert1(self):
        self.alert_pkt = QLabel()
        self.alert_pkt.setObjectName(u"alert_pkt")
        self.alert_pkt.setGeometry(QRect(1270, 710, 491, 31))
        self.alert_pkt.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 italic 13pt \"Franklin Gothic Cond\";\n"
"background: transparent;")
        self.alert_pkt.setText(QCoreApplication.translate("MainWindow", u"Please complete all the fields before proceeding.", None))

    def sendDraft(self,index):
        index = index +1 
        draft = drafting.getSelectedDraft(index)
        sPacket.setEthernet(draft[3],draft[4],draft[5])
        sPacket.setIP(draft[6], draft[7],draft[8],draft[9],draft[10],draft[11],draft[12],draft[13],draft[14],draft[15],draft[16],draft[16],draft[17])  
        sPacket.setUDP(draft[19], draft[20], draft[21] )
        if draft[22] == "DNS":
                drafts2 = drafting.getSelectedDraftType(index,"DNS")
                self.qname_field.setText(drafts2[1])
                self.qtype_field.setText(str(drafts2[2]))
                self.qclass_field.setText(str(drafts2[3]))
                self.sPacketType = 1
                self.setListValues()
        elif draft[22] == "NTP":
                drafts2 = drafting.getSelectedDraftType(index,"NTP")
                self.leap_field.setText(drafts2[1])
                self.version_field.setText(drafts2[2])
                self.mode_field.setText(drafts2[3])
                self.stratum_field.setText(drafts2[4])
                self.poll_field.setText(drafts2[5])
                self.precision_field.setText(drafts2[6])
                self.delay_field.setText(drafts2[7])
                self.dispersion_field.setText(drafts2[8])
                self.id_field.setText(drafts2[9])
                self.referenceid_field.setText(drafts2[10])
                self.reference_field.setText(drafts2[11])
                self.origin_field.setText(drafts2[12])
                self.recieve_field.settext(drafts2[13])
                self.sent_field.settext(drafts2[14])
                self.sPacketType = 2
                self.setListValues()
        else:
                drafts2 = drafting.getSelectedDraftType(index,"SSDP")
                self.host_field.setText(drafts2[1])
                self.port_field.setText(drafts2[2])
                self.man_field.setText(drafts2[3])
                self.mx_field.setText(drafts2[4])
                self.st_field.setText(str(drafts2[5]))
                self.sPacketType = 3 
                self.setListValues()

        

    def slideleft(self):
        width = self.side_menu.width()

        if width == 63:
                width = 200

        elif width == 200:
                width = 63

        self.side_menu.setFixedWidth(width)
        self.animation = QPropertyAnimation(self.side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def changebg(self):
        
        self.home.setStyleSheet(u"background-image: url(:/bg1/dark_welc.png);")
        self.packets.setStyleSheet(u"background-image: url(:/bg1/new_eth.png);")
        self.ETH.setStyleSheet(u"background-image: url(:/bg1/dark_eth.png);")
        self.IP.setStyleSheet(u"background-image: url(:/bg1/dark_ip.png);")
        self.UDP.setStyleSheet(u"background-image: url(:/bg1/dark_udp.png);")
        self.NTP.setStyleSheet(u"background-image: url(:/bg1/dark_ntp.png);")
        self.DNS.setStyleSheet(u"background-image: url(:/bg1/dark_dns.png);")
        self.SSDP.setStyleSheet(u"background-image: url(:/bg1/dark_ssdp.png);")
        self.drafts_pg.setStyleSheet(u"background-image: url(:/bg1/dark_drafts.png);")
        self.sent_pg.setStyleSheet(u"background-image: url(:/bg1/dark_sent.png);")
        self.recvd_pg.setStyleSheet(u"background-image: url(:/bg1/dark_recv.png);")
        self.Account.setStyleSheet(u"background: url(:/bg1/dark_settings.png);")
        self.autocreate.setStyleSheet(u"background: rgb(29, 108, 137);\n"
"background: url(:/bg1/dark_autc.png);")

    def changedbg(self):

        self.home.setStyleSheet(u"background-image: url(:/bg1/home.png);")
        self.packets.setStyleSheet(u"background-image: url(:/bg1/newpc.png);")
        self.ETH.setStyleSheet(u"background-image: url(:/bg1/eth.png);")
        self.IP.setStyleSheet(u"background-image: url(:/bg1/ip.png);")
        self.UDP.setStyleSheet(u"background-image: url(:/bg1/udp.png);")
        self.NTP.setStyleSheet(u"background-image: url(:/bg1/ntp.png);")
        self.DNS.setStyleSheet(u"background-image: url(:/bg1/dns.png);")
        self.SSDP.setStyleSheet(u"background-image: url(:/bg1/ssdp.png);")
        self.drafts_pg.setStyleSheet(u"background-image: url(:/bg1/drafts.png);")
        self.sent_pg.setStyleSheet(u"background-image: url(:/bg1/sent.png);")
        self.recvd_pg.setStyleSheet(u"background-image: url(:/bg1/recvd.png);")
        self.Account.setStyleSheet(u"background: url(:/bg1/settingss.png);")
        self.contacts.setStyleSheet(u"background-image: url(:/bg1/contactss.png);")
        self.autocreate.setStyleSheet(u"background: rgb(29, 108, 137);\n"
"background: url(:/bg1/autocreate.png);")

    def recieve_page(self):
        
        #self.stackedWidget.setCurrentIndex(11)
        startSniffing(self.currentUser) #start capturing packets

    def startRandomSelection(self):
        #     t1 = threading.Thread(target=startSsdpGA, args=(self,))
        #     t1.start()
        if self.choice == 'SSDP':
                self.worker = WorkerThread(self.sorc_ad.text())
                self.worker.start()
                self.worker.update_progress.connect(self.helpUi)
        elif self.choice == 'DNS':
                self.worker = WorkerThreadDns(self.sorc_ad.text(),self.dest_ad.text())
                self.worker.start()
                self.worker.update_progress.connect(self.helpUi)
        elif self.choice == 'NTP':
                self.worker = WorkerThreadNTP(self.sorc_ad.text(),self.dest_ad.text())
                self.worker.start()
                self.worker.update_progress.connect(self.helpUi)

        #startSsdpGA(self)   

    def helpUi(self, message):
            
        #self.stackedWidget.setCurrentIndex(0)
        msg = QMessageBox()
        msg.setWindowTitle(" ")
        msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">"+message+"</span></p></body></html>")
        msg.setIcon(QMessageBox.Question)
        msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

        x = msg.exec_()

#     def helpUi(self):
            
#         self.stackedWidget.setCurrentIndex(0)
#         msg = QMessageBox()
#         msg.setWindowTitle(" ")
#         msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">Autocreate Completed!</span></p></body></html>")
#         msg.setIcon(QMessageBox.Question)
#         msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

#         x = msg.exec_()

    def sendPacket(self):

        msg = QMessageBox()
        msg.setWindowTitle(" ")
        msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">Packet Sent</span></p></body></html>")
        msg.setIcon(QMessageBox.Question)
        msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

        x = msg.exec_()

    def makeDraft(self):

        msg = QMessageBox()
        msg.setWindowTitle(" ")
        msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">Packet Draft Saved</span></p></body></html>")
        msg.setIcon(QMessageBox.Question)
        msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

        x = msg.exec_()
    def printHelp(self):

        page = self.stackedWidget.currentIndex()
        if page == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Home - Help ")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the home page, you can perform two types of packet actions:\n Send a packet\nRecieve a packet\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 1:
                msg = QMessageBox()
                msg.setWindowTitle("Network Packet Selection - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Network Packet Selection Page, you can select the network you want to send the packet through:\n - NTP\n - DNS\n - SSDP</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 2:
                msg = QMessageBox()
                msg.setWindowTitle("Ethernet - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Ethernet Packet Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 3:
                msg = QMessageBox()
                msg.setWindowTitle("IP - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the IP Packet Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 4:
                msg = QMessageBox()
                msg.setWindowTitle("UDP - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the UDP Packet Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 5:
                msg = QMessageBox()
                msg.setWindowTitle("NTP - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the NTP Network Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 6:
                msg = QMessageBox()
                msg.setWindowTitle("DNS - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the DNS Network Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 7:
                msg = QMessageBox()
                msg.setWindowTitle("SSDP - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the SSDP Network Page, you can enter your desired packet values or use the default values.\n To know more about each field, hover your cursor over it!\n</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 8:
                msg = QMessageBox()
                msg.setWindowTitle("Settings - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Settings Page, you can edit your details and preferences here.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 9:
                msg = QMessageBox()
                msg.setWindowTitle("Drafts - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Drafts Page, you can find your saved and unsent packets here.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 10:
                msg = QMessageBox()
                msg.setWindowTitle("Sent - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Sent Page, you can find all of your previously sent packets here.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 11:
                msg = QMessageBox()
                msg.setWindowTitle("Recieved - Help ")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Recieved Page, you can find of all your recieved packets here.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 12:
                msg = QMessageBox()
                msg.setWindowTitle("Contacts - Help ")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is your Contacts Page, you can find your contacts here.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
        elif page == 13:
                msg = QMessageBox()
                msg.setWindowTitle("AutoCreate - Help")
                msg.setText("<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Franklin Gothic Raw'; font-size:10.8pt; font-weight:496;\">This is the Autocreate Page, you can send an auto-created packet right away to and from the address of your choice.</span></p></body></html>")
                msg.setIcon(QMessageBox.Question)
                msg.addButton(QPushButton('Done'), QMessageBox.YesRole)

                x = msg.exec_()
    def goback(self):

        self.stackedWidget.setCurrentIndex(1)

    def goeth(self):

        self.stackedWidget.setCurrentIndex(2)


