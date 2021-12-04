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
# def displayReceiveLog(self):
	
# 	rowPosition = self.tableRecvd.rowCount()
# 	self.tableRecvd.insertRow(rowPosition)
# 	self.tableRecvd.setItem(rowPosition, 0, QTableWidgetItem(15))
# 	self.tableRecvd.setItem(rowPosition, 1, QTableWidgetItem("monday"))
# 	self.tableRecvd.setItem(rowPosition, 2, QTableWidgetItem(17))
# 	self.tableRecvd.setItem(rowPosition, 3, QTableWidgetItem(18))
# 	self.tableRecvd.setItem(rowPosition, 4, QTableWidgetItem(120))

def displayReceiveLog(self):
    currentRespSize = 0

    try:
        cnx = mysql.connector.connect(user='me', password='myUserpassword',host='127.0.0.1',database='PAAT')
        cursor = cnx.cursor()
        self.tableRecvd.setRowCount(0) #refreshing the table each time the receive log is viewed
        #select Sizee,Datee, ReceiverAdd, FinalSize,Amplification FROM Received JOIN Receives on Received.ID = Receives.ID JOIN Users on Users.Username = Receives.username
        query = ("SELECT Sizee, Datee,ReceiverAdd, FinalSize, Amplification FROM Received"
                 " JOIN Receives on Received.ID = Receives.ID where Receives.Username = %s")

        cursor.execute(query,(self.currentUser,))
        self.tableRecvd.setRowCount(0)
        #self.tableRecvd.sortByColumn(0,Qt.AscendingOrder)
        self.tableRecvd.setSortingEnabled(False)
        #print(cursor)
        for (initSize, dateRec,recAddr,respSize, ampFactor) in cursor:
            
            if currentRespSize < respSize:#display the current highest in resp
                self.rcvAd.setText(recAddr)
                self.rcvBox.display(str(respSize))
                self.intBox.display(str(initSize))
                self.ampBox.display(str(ampFactor))
                currentRespSize = respSize
                
            rowPosition = self.tableRecvd.rowCount()
            self.tableRecvd.insertRow(rowPosition)
            self.tableRecvd.setItem(rowPosition, 0, QTableWidgetItem(recAddr))
            self.tableRecvd.setItem(rowPosition, 1, QTableWidgetItem(dateRec.strftime('%Y-%m-%d')))
            self.tableRecvd.setItem(rowPosition, 2, QTableWidgetItem(str(initSize)))
            self.tableRecvd.setItem(rowPosition, 3, QTableWidgetItem(str(respSize)))
            self.tableRecvd.setItem(rowPosition, 4, QTableWidgetItem(str(ampFactor)))
        cursor.close()
        cnx.close()
    except Exception as e:
        pass


#sniff sniff
def startSniffing(currentUser):
    t1 = threading.Thread(target=startSniff, args=(currentUser,))
    t1.start()
    # displayReceiveLog(self)
    


#startSniffing()