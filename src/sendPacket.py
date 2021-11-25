"""
FILENAME: sendPacket.py
AUTHORS: Majid Jafar, Samrah Tahir, Anas Raafat
PURPOSE: Conatains methods to craft and send a complete packet
DATE CREATED: 01/10/2021
LAST EDITED DATE: 16/10/2021
"""

import scapy.all as scapy
from arpCost import arpAdditionalCost
import random
import mysql.connector
from mysql.connector import Error
from datetime import datetime
#Qtablewidgetitem
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

class sendPacketClass:

    ethSrc = ""
    ethDst =""
    ethType =""
    ipVersion = 0
    ipIhl = None
    ipTos = 0x0
    ipLen = None
    ipId = 1
    ipFlags = ""
    ipFrag = 0
    ipTtl = 64
    ipProto = ""
    ipChksum = None
    ipOpt = ""
    ipSrc =""
    ipDst =""
    udpSport ="" 
    udpDport = ""
    udpChksum = None
    listValues = []





    """
    FUNCTION NAME: setEthernet
    PURPOSE: setter
    INPUT: String all the necessary value and a single list variable which conatins information of the specific ethernet packet type
    OUTPUT: none
    """
    def setEthernet (self,ethSrc1,ethDst1,ethType1):
        print("Ethernet values in sendPacket class: "+ ethSrc1, ethDst1, ethType1)
        self.ethSrc = ethSrc1
        self.ethDst = ethDst1
        self.ethType = int(ethType1) #use integer values from ui, not hex



    """
    FUNCTION NAME: setIP
    PURPOSE: setter
    INPUT: String all the necessary value and a single list variable which conatins information of the specific IP packet type
    OUTPUT: none
    """
    def setIP (self,ipVersion1,ipIhl1,ipTos1,ipLen1,ipId1,ipFlags1,ipFrag1,ipTtl1,ipProto1,ipChksum1,ipOpt1,ipSrc1,ipDst1):
        print("IP values in sendPacket class: "+ipVersion1, ipIhl1, ipTos1, ipLen1, ipId1, ipFlags1, ipFrag1, ipTtl1, ipProto1, ipChksum1, ipOpt1, ipSrc1, ipDst1)
        self.ipVersion = int(ipVersion1)
        self.ipIhl = int(ipIhl1)
        self.ipTos = int(ipTos1)
        self.ipLen = int(ipLen1) #length is not set until the packet is actually created
        self.ipId = int(ipId1)
        self.ipFlags = int(ipFlags1)
        self.ipFrag = int(ipFrag1)
        self.ipTtl = int(ipTtl1)
        self.ipProto = int(ipProto1)
        self.ipChksum = ipChksum1
        self.ipOpt = ipOpt1 #not using options field
        self.ipSrc = ipSrc1
        self.ipDst = ipDst1


    """
    FUNCTION NAME: setUDP
    PURPOSE: setter
    INPUT: String all the necessary value and a single list variable which conatins information of the specific UDP packet type
    OUTPUT: none
    """
    def setUDP(self,udpSport1,udpDport1,udpChksum1):
        self.udpSport= int(udpSport1)
        self.udpDport= int(udpDport1)
        #self.udpChksum= udpChksum1


  
    """
    FUNCTION NAME: setListValues
    PURPOSE: setter
    INPUT: String all the necessary value and a single list variable which conatins information of the specific ListVAlues packet type
    OUTPUT: none
    """  
    def setListValues(self,listValues1,type):
        if(type == 1):
            self.listValues = [listValues1[0],listValues1[1],listValues1[2]]
        elif(type == 2):
            self.listValues = [listValues1[0],listValues1[1],listValues1[2],listValues1[3],listValues1[4]]
        elif(type == 3):
            self.listValues = [listValues1[0],listValues1[1],listValues1[2],listValues1[3],listValues1[4],listValues1[5],listValues1[6],listValues1[7],listValues1[8],listValues1[9],listValues1[10],listValues1[11],listValues1[12],listValues1[13]]

        self.sendPacket(type,self.ethSrc,self.ethDst,self.ethType,self.ipVersion,self.ipIhl,self.ipTos,self.ipLen,self.ipId,self.ipFlags,self.ipFrag,self.ipTtl,self.ipProto,self.ipChksum,self.ipSrc,self.ipDst,self.udpSport,self.udpDport,self.udpChksum,self.listValues)

    """
    FUNCTION NAME: sendPacket
    PURPOSE: Crafts the first three layers.
    INPUT: String all the necessary value and a single list variable which conatins information of the specific UDP packet type
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacket(self,type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,udpSport,udpDport,udpChksum,listValues):

        out = 0
        #testPkt = Ether(src=ethSrc,dst=ethDst,type=ethType)/IP(version=ipVersion,ihl=ipIhl,tos=ipTos,id=ipId,frag=ipFrag,ttl=ipTtl,proto=ipProto,dst='8.8.8.8')/UDP(sport=udpSport,dport=udpDport)/DNS(rd=1,qd=DNSQR(qname='www.google.com',qtype='ALL'))
        #sendp(testPkt)
        #newPkt =IP(version=4,ihl=5,tos=0,id=1,frag=0,ttl=64,proto=17,dst='8.8.8.8')/UDP(sport=6500,dport=53)/DNS(rd=1,qd=DNSQR(qname='www.google.com',qtype='ALL'))

        # print(type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,udpSport,udpDport,udpChksum,listValues)

        packet = (scapy.Ether(
                            src=ethSrc,
                            dst=ethDst,
                            type=ethType
                            )
                    /scapy.IP(
                            version=ipVersion,
                            ihl=ipIhl,
                            tos=ipTos,
                            #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                            id=ipId,
                            flags=ipFlags,
                            frag=ipFrag,
                            ttl=ipTtl,
                            proto=ipProto,
                            #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                            src=ipSrc,
                            dst=ipDst,
                            #options=ipOptions
                            )
                    /scapy.UDP(
                            sport=udpSport,
                            dport=udpDport,
                            #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                            )
                        )
        
        
        #                     src=ethSrc,
        #                     dst=ethDst,
        #                     type=ethType
        #                     )
        #             /scapy.IP(
        #                     version=ipVersion,
        #                     ihl=ipIhl,
        #                     tos=ipTos,
        #                     len=ipLen,
        #                     id=ipId,
        #                     flags=ipFlags,
        #                     frag=ipFrag,
        #                     ttl=ipTtl,
        #                     proto=ipProto,
        #                     chksum=ipChksum,
        #                     src=ipSrc,
        #                     dst=ipDst,
        #                     #options=ipOptions
        #                     )
        #             /scapy.UDP(
        #                     sport=6500,
        #                     dport=6500,
        #                     chksum=udpChksum
        #                     )
        #                 )
        my_list = []
        if not my_list:
            n = random.randint(1,99)
            my_list.append(n)
            my_list = list(set(my_list))
        now = datetime.now()
        date_now = now.strftime('%Y-%m-%d')
        current_time = now.strftime("%H:%M:%S")
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='paat',user='PAAT',password='1234')
            print("Connection To Database Established..\n")
        except Error as e:
            print("Connection To Database Failed!\n")

        cursor = conn.cursor()
        randomID = my_list.pop(0)
        temp = 'aaa'
        sizepacket = len(packet)
        add_packet = """INSERT INTO Sent(ID,Sizee,Datee,Time,SenderAdd,ReceiverAdd,SourceETH,DestinationETH,Type,Version,IHL,TOS,TotalLength,Identification,Flags,FragmentOffset,TTL,Protocol,HeaderChecksum,SourceIP,DestinationIP,Options,SourcePort,DestinationPort,Checksum) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(add_packet, (randomID, sizepacket,date_now,current_time, ipSrc, ipDst, ethSrc, ethDst,ethType, ipVersion, ipIhl, ipTos, ipLen, ipId, ipFlags, ipFrag, ipTtl, ipProto, ipChksum, ipSrc, ipDst, temp, udpSport, udpDport, udpChksum))
        conn.commit()
        if(type == 1):
            #self.sendInitPacket(initPacket,"DNS")
            out = self.sendPacketDNS(packet,listValues)
            add_draft = "INSERT INTO DNS(ID,Qname,Qtype,Qclass) VALUES(%s,%s,%s,%s)"
            cursor.execute(add_draft, (randomID,listValues[0],listValues[1],listValues[2]))
            conn.commit()

        elif(type == 3):
            #self.sendInitPacket(initPacket,"SSDP")
            out = self.sendPacketNTP(packet,listValues)
            add_draft = "INSERT INTO NTP(ID,Leap,Version,Modee,Stratum,Poll,Precisionn,Delay,Dispersion,ID2,ReferenceID,Reference,Origin,Receive,Sent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(add_draft, (randomID,listValues[0],listValues[1], listValues[2],listValues[3],listValues[4], listValues[5],listValues[6], listValues[7],listValues[8],listValues[9],listValues[10], listValues[11],listValues[12],listValues[13]))
            conn.commit()

        elif(type == 2):
            #self.sendInitPacket(initPacket,"NTP")
            out = self.sendPacketSSDP(packet,listValues)
            add_draft = "INSERT INTO SSDP(ID,Hostt,Port,MAN,MX,ST) VALUES(%s,%s,%s,%s,%s,%s)"
            cursor.execute(add_draft, (randomID,listValues[0],listValues[1], listValues[2],listValues[3],listValues[4]))
            conn.commit()

        return out



    """
    FUNCTION NAME: sendInitPacket
    PURPOSE: Sends a packet to the destination informing the packet type
    INPUT: A packet with pre loaded information and a string determining the type of data
    OUTPUT: None
    """
    def sendInitPacket(self,packet,type):
        packet = packet/scapy.Raw(load=type)

        scapy.sendp(packet)

    """
    FUNCTION NAME: sendPacketDNS
    PURPOSE: Crafts the final layer of the packet (DNS)
    INPUT: Single list variable which conatins information of DNS packet
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacketDNS(self,packet,listValues):

        packet = packet/scapy.DNS(  rd=1,
                                    qd=scapy.DNSQR(
                                                qname=listValues[0],
                                                qtype=listValues[1],
                                                qclass=listValues[2]
                                                )
                                )
        srcPort = scapy.RandShort()._fix()
        packet[scapy.UDP].sport = srcPort
        packet[scapy.IP].len =  len(packet[scapy.IP])
        packet[scapy.UDP].len = len(packet[scapy.UDP]) #setting the length field of the IP and UDP layers
        sizePkt = self.sizePacket('\"DNS\"',srcPort,packet[scapy.UDP].len,packet[scapy.IP].src)
        print('\"DNS\"')
        scapy.send(sizePkt)
        scapy.sendp(packet)

        arpAdditionalCost(packet[scapy.IP].src, packet[scapy.IP].dst)

        return 1

    """
    FUNCTION NAME: sendPacketNTP
    PURPOSE: Crafts the first three layers.
    INPUT: Single list variable which conatins information of NTP packet
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacketNTP(self,packet,listValues):

        packet = packet/scapy.NTPHeader(
                                    leap=int(listValues[0]),
                                    version=int(listValues[1]),
                                    mode=int(listValues[2]),
                                    #stratum=listValues[3],
                                    #poll=listValues[4], #polling field is used by server
                                    #precision=int(listValues[5]),#used by server
                                    #delay=listValues[6],
                                    #dispersion=listValues[7],
                                    #id=listValues[8],
                                    #ref_id=listValues[9],
                                    #ref=listValues[10],
                                    #orig=listValues[11], #when packet left the client
                                    #recv=listValues[12], #time req arrived at server
                                    #sent=listValues[13] #time when reply was sent by server
                                    
                                    )
        srcPort = scapy.RandShort()._fix()
        packet[scapy.UDP].sport = srcPort
        packet[scapy.IP].len =  len(packet[scapy.IP])
        packet[scapy.UDP].len = len(packet[scapy.UDP]) #setting the length field of the IP and UDP layers
        sizePkt = self.sizePacket('\"NTP\"',srcPort,packet[scapy.UDP].len,packet[scapy.IP].src)
        print('\"NTP\"')
        scapy.send(sizePkt)
        scapy.sendp(packet)

        arpAdditionalCost(packet[scapy.IP].src, packet[scapy.IP].dst)
        return 1

                                        

    """
    FUNCTION NAME: sendPacketSSDP
    PURPOSE: Crafts the first three layers.
    INPUT: Single list variable which conatins information of the specific UDP packet type
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacketSSDP(self,packet,listValues):


        payload = "M-SEARCH * HTTP/1.1\r\n" \
            "HOST:" + listValues[0] + ":" + listValues[1] + "\r\n" \
            "ST:"+ listValues[4] + "\r\n" \
            "MAN:" + "\""+ listValues[2] +"\" \r\n" \
            "MX:" + listValues[3] +"\r\n\r\n"                

        packet = packet/payload
        srcPort = scapy.RandShort()._fix()
        packet[scapy.UDP].sport = srcPort
        packet[scapy.IP].len =  len(packet[scapy.IP])
        packet[scapy.UDP].len = len(packet[scapy.UDP]) #setting the length field of the IP and UDP layers
        sizePkt = self.sizePacket('\"SSDP\"',srcPort,packet[scapy.UDP].len,packet[scapy.IP].src)
        print('\"SSDP\"')
        print(repr(packet))
        scapy.send(sizePkt)
        scapy.sendp(packet)

        arpAdditionalCost(packet[scapy.IP].src, packet[scapy.IP].dst)

        return 1
      
    def autoSend(listValue):
        print("Todo")

    def sizePacket(self,Type,QID, size, dest):
        t = '\"Type\"'
        q = '\"QID\"'
        s = '\"size\"'
        ldDict = f"{{{t}:" +Type+f",{q}:"+str(QID)+f",{s}:"+str(size)+"}"
        print('QID: '+str(QID))
        sizePkt = scapy.IP(dst=dest)/scapy.UDP(sport=6700,dport=6700)/scapy.Raw(load=ldDict)
        return sizePkt

def displaySent(self):
    cnx = mysql.connector.connect(user='PAAT', password='1234',host='127.0.0.1',database='paat')
    cursor = cnx.cursor()
    self.tableSent.setRowCount(0) #refreshing the table each time the sent log is viewed
    query = ("SELECT Users.Username, Sent.Datee, Sent.Sizee, Sent.ReceiverAdd FROM Users LEFT JOIN Sends ON Users.Username = Sends.Username LEFT JOIN Sent ON Sent.ID = Sends.ID;")
    cursor.execute(query)
    self.tableSent.setRowCount(0)
    self.tableSent.setSortingEnabled(False)
    for (Users, Date,Size,Addr) in cursor:
        print(Users, Date, Size, Addr)
        rowPosition = self.tableSent.rowCount()
        self.tableSent.insertRow(rowPosition)
        self.tableSent.setItem(rowPosition, 0, QTableWidgetItem(Users))
        self.tableSent.setItem(rowPosition, 1, QTableWidgetItem(Date.strftime('%Y-%m-%d')))
        self.tableSent.setItem(rowPosition, 2, QTableWidgetItem(Date.strftime('%Y-%m-%d')))
        self.tableSent.setItem(rowPosition, 3, QTableWidgetItem(str(Size)))
        self.tableSent.setItem(rowPosition, 4, QTableWidgetItem(Addr))
    cursor.close()
    cnx.close()
