from scapy.all import *
import os
import json
import mysql.connector
from mysql.connector import errorcode
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime

'''
Purpose: Capture packets and calculation amplification if any
Author: Samrah
Last Modified Date: 06/11/2021
'''
packets = []
def startSniff(num):
	print('thread created')
	
	
	received = sniff(filter="udp and (dst port 6700 or src port 53 or src port 123 or src port 1900)", prn=lambda pkt: trafficIdentifier(pkt))
	
def trafficIdentifier(pkt):
	print('inside traffic')
	print('src port '+str(pkt.getlayer(IP).sport))
	dictOfPkts = {}
	if pkt.haslayer(UDP) and pkt.haslayer(Raw) and pkt.getlayer(UDP).dport==6700 and pkt.getlayer(UDP).sport==6700:
		if "size" in json.loads(pkt.getlayer(Raw).load.decode('utf-8')): 
			print('inside size determinator')
			dictOfPkts["size"] = convertToDict(pkt)['size']
			dictOfPkts["dport"] = convertToDict(pkt)['QID']
			dictOfPkts['type'] = convertToDict(pkt)['Type']
			
			packets.append(dictOfPkts)
			print(packets)
	elif pkt.getlayer(IP).sport == 53:
		print('inside pkt.getlayer(IP).src == 53')
		handleDNS(pkt)
	elif pkt.getlayer(IP).sport == 1900:
		print('inside pkt.getlayer(IP).src == 1900')
		handleSSDP(pkt)
	elif pkt.getlayer(IP).sport == 123:
		print('inside pkt.getlayer(IP).src == 123')
		handleNTP(pkt)

def handleNTP(ntpPacket):
	print('inside handleNTP')
	print('ntpPacket dport '+str(ntpPacket.getlayer(UDP).dport))
	#global packets
	respSize = ntpPacket.getlayer(UDP).len
	
	for packet in packets:
		print('dport in list of packets: '+str(packet["dport"]))
		if packet["dport"] == ntpPacket.getlayer(UDP).dport and packet['type'] == 'NTP':
			ampFactor = dnsAmplificationFactor(packet['size'], ntpPacket.getlayer(UDP).len)

def handleSSDP(ssdpPacket):
	print('inside handleSSDP')
	print('ssdpdnsPacket dport '+str(ssdpPacket.getlayer(UDP).dport))
	#global packets
	respSize = ssdpPacket.getlayer(UDP).len
	
	for packet in packets:
		print('dport in list of packets: '+str(packet["dport"]))
		if packet["dport"] == ssdpPacket.getlayer(UDP).dport and packet['type'] == 'SSDP':
			ampFactor = dnsAmplificationFactor(packet['size'], ssdpPacket.getlayer(UDP).len)


def handleDNS(dnsPacket):
	print('inside handleDNS')
	#print(repr(dnsPacket))
	#print('dnsPacket dport '+str(dnsPacket.getlayer(UDP).dport))
	#global packets
	respSize = dnsPacket.getlayer(UDP).len
	#print(packets)
	for packet in packets:
		#print('dport in list of packets: '+str(packet["dport"]))
		if packet["dport"] == dnsPacket.getlayer(UDP).dport and packet['type'] == 'DNS':
			dateReceived = datetime.today().strftime('%Y-%m-%d')
			ampFactor = dnsAmplificationFactor(packet['size'], dnsPacket.getlayer(UDP).len)
			insertDB(dnsPacket.getlayer(IP).dst, dateReceived, packet['size'],dnsPacket.getlayer(UDP).len , ampFactor)
	#dnsPackets = sniff(filter = "dst port 6700 ", prn= lambda x: x.haslayer(DNSQR) or x.haslayer(DNSRR), timeout=20)

def dnsQAlengthCal(dnsQPkt):
    dnsQPacketLength = dnsQPkt.getlayer(UDP).len
    return dnsQPacketLength


#calculate dns amplification
def dnsAmplificationFactor(qLength, rlength):
    ampFactor = (float((rlength - qLength))/float(qLength))*100
    print("***The Amplification for dns is****"+str(ampFactor)+"%")
    return ampFactor


def convertToDict(pkt):
	infoDict = json.loads(pkt.getlayer(Raw).load.decode('utf-8'))
	return infoDict



#to insert received values into database
def insertDB(receiverAddr, dateRec, initSize, respSize, ampFactor):
	
	#figure out how to add the unique id
	try:
		cnx = mysql.connector.connect(user='me', password='myUserpassword',host='127.0.0.1',database='PAAT')
		uniqueID = generateID(cnx)
		
		cursor = cnx.cursor()
	
		add_pkt = ("INSERT INTO Received "
				"(ID, Sizee, Datee,ReceiverAdd, FinalSize, Amplification) "
				"VALUES (%s,%s, %s, %s, %s, %s)")
		
		data_pkt = (uniqueID, initSize, dateRec,receiverAddr, respSize, ampFactor)
		
		cursor.execute(add_pkt, data_pkt)
		
		#adding relation between user and received packet
		add_rel = ("INSERT INTO Receives "
				"(Username, ID) "
				"VALUES (%s, %s)")
		data_rel = ('samrahtahir123',uniqueID)#need to figure out how to get the name of the user logged in
		cursor.execute(add_rel, data_rel)
		cnx.commit()
		print('done inserting')

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cnx.close()

#generates a unique id based on the database table
def generateID(conn):
	query = ("select ID from Received")
	ids = conn.cursor()
	insertID = 1
	ids.execute(query)
	recvIDs = [item[0] for item in ids.fetchall()]
	print(recvIDs)

	while True:
		if str(insertID) not in recvIDs:
			break
		else:
			insertID = insertID + 1

	# #print(recvIDs)
	# # recvID = 1
	# # for ID in ids:
	# # 	if ID == recvID:
	# # 		recvID = recvID + 1
		
	
	return str(insertID)


if __name__ == '__main__':
    startSniff(10)


