from scapy.all import *
from capturePacket import startSniff
import mysql.connector
import threading

#Qtablewidgetitem
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


# def receiveMain():
#     pass
'''
Purpose: display received packet info in received log
'''
def displayReceiveLog(self):
	
	rowPosition = self.tableRecvd.rowCount()
	self.tableRecvd.insertRow(rowPosition)
	self.tableRecvd.setItem(rowPosition, 0, QTableWidgetItem(15))
	self.tableRecvd.setItem(rowPosition, 1, QTableWidgetItem("monday"))
	self.tableRecvd.setItem(rowPosition, 2, QTableWidgetItem(17))
	self.tableRecvd.setItem(rowPosition, 3, QTableWidgetItem(18))
	self.tableRecvd.setItem(rowPosition, 4, QTableWidgetItem(120))
'''
def displayReceiveLog(self):
        cnx = mysql.connector.connect(user='me', password='myUserpassword',host='127.0.0.1',database='PAAT')
        cursor = cnx.cursor()
        self.tableRecvd.setRowCount(0) #refreshing the table each time the receive log is viewed
        query = ("SELECT Sizee, ReceiverAdd, FinalSize, Amplification FROM Received"
                 )
        cursor.execute(query)

        for (initSize, recAddr,respSize, ampFactor) in cursor:

            rowPosition = self.tableRecvd.rowCount()
            self.tableRecvd.insertRow(rowPosition)
            self.tableRecvd.setItem(rowPosition, 0, QTableWidgetItem(recAddr))
            self.tableRecvd.setItem(rowPosition, 1, QTableWidgetItem("monday"))
            self.tableRecvd.setItem(rowPosition, 2, QTableWidgetItem(str(initSize)))
            self.tableRecvd.setItem(rowPosition, 3, QTableWidgetItem(str(respSize)))
            self.tableRecvd.setItem(rowPosition, 4, QTableWidgetItem(str(ampFactor)))
        cursor.close()
        cnx.close()
'''
#sniff sniff
def startSniffing():
    t1 = threading.Thread(target=startSniff, args=(10,))
    t1.start()
    # displayReceiveLog(self)
    


#startSniffing()