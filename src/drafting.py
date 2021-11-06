from dns.rdatatype import MX
import scapy.all as scapy
import sys
import mysql.connector
from mysql.connector import Error
from scapy.utils import checksum
from datetime import datetime
from datetime import date


srcEth = ""
dstEth = ""
type = ""
version = 40
ihl = ""
tos = ""
totallength = ""
id = 30
flgs = ""
frag = 20
ttl = 30
protocol = ""
headersum = ""
srcip = ""
dstip = ""
options = ""
srcport = ""
dstport = ""
cheksum = ""
length = 10
mx = ""
st = ""
host = ""
port = ""
man = ""
Qname = ""
Qtype = 40
Qclass = 50



def setVariablesIP(srcip1,dstip1,totallength1,version1,ihl1,tos1,id1,flgs1,frag1,protocol1,headersum1,options1, ttl1):
    srcip = srcip1
    dstip = dstip1
    totallength = totallength1
    version = int(version1)
    ihl = ihl1
    tos = tos1
    id = int(id1)
    flgs = flgs1
    frag = int(frag1)
    protocol = protocol1
    headersum = headersum1
    options = options1
    ttl = int(ttl1)
    print("Here2")

def setVariablesEth(srcEth1, dstEth1, type1):
    srcEth = srcEth1
    dstEth = dstEth1
    type = type1

def setVariablesUDP(dstport1, srcport1, checksum1, length1):
    dstport = dstport1
    srcport = srcport1
    checksum = checksum1
    length = int(length1)

def setVariablesSSDP(mx1,st1,man1,host1,port1):
    mx = mx1
    st = st1
    man = man1
    host = host1
    port = port1

def setVariablesNTP(leap1,versn1,modee1,stra1,poll1,prec1,delay1,disp1,ID2,RefID1,ref1,org1,rec1,sent1):
    print("Hi")

def setVariablesDNS(Qname1,Qtype1,Qclass1):
    Qname = Qname1
    Qtype = int(Qtype1)
    Qclass = int(Qclass1)


def saveDraft(type1):
    randomID = getID()
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    print("Here")
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO Drafts(ID,Datee,Time,SourceETH,DestinationETH,Type,Version,IHL,TOS,TotalLength,Identification,Flags,FragmentOffset,TTL,Protocol,HeaderChecksum,SourceIP,DestinationIP,Options,SourcePort,DestinationPort,Checksum,PacketType,Length) VALUES(%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%d,%s,%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d)"
    cursor.execute(add_draft, (randomID, today,current_time,srcEth,dstEth,type,version,ihl,tos,totallength,id,flgs,frag,ttl,protocol,headersum,srcip,dstip,options,srcport,dstport,cheksum,type1,length))
    conn.commit()
    if type1 == "SSDP":
        print("Crashing here")
        saveSSDP(randomID)
    elif type1 == "DNS":
        saveDNS(randomID)
    else:
        saveNTP(randomID)

    

def saveSSDP(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO SSDP2(ID,Hostt,Port,MAN,MX,ST) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(add_draft, (randomID, host,port, man,mx,st))
    conn.commit()

def saveNTP(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO NTP2(ID,Hostt,Port,MAN,MX,ST) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(add_draft, (randomID, host,port, man,mx,st))
    conn.commit()


def saveDNS(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO DNS2(ID,Qname,Qtype,Qclass) VALUES(%s,%s,%d,%d)"
    cursor.execute(add_draft, (randomID, Qname,Qtype,Qclass))
    conn.commit()


def getID():
    for x in range(100):
        newID = "A"
        newID = newID + str(x)

    return newID

def connectToDatabase():
	try:
		connection = mysql.connector.connect(host='127.0.0.1',database='paat',user='ahmed',password='1234')
		print('connection complete')
	except Error as e:
		print('Error while connecting')

	return connection	








