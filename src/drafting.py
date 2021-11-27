import scapy.all as scapy
import sys
import mysql.connector
from mysql.connector import Error
from scapy.utils import checksum
from datetime import datetime
from datetime import date
import random

lastID = 0
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
Qtype = ""
Qclass = ""
leap = 1
versionNTP = 2
modee = ""
stratum = 3
poll = 4
precision = 5
delay = 0
dispersion = 0
IDNTP = ""
refID = 2
ref = ""
Origin = ""
rev = ""
sent = ""



def setVariablesIP(srcip1,dstip1,totallength1,version1,ihl1,tos1,id1,flgs1,frag1,protocol1,headersum1,options1, ttl1):
    global srcip
    global dstip
    global totallength
    global version
    global ihl
    global tos
    global id
    global flgs
    global frag
    global protocol
    global headersum
    global options
    global ttl
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

def setVariablesEth(srcEth1, dstEth1, type1):
    global srcEth
    global dstEth
    global type
    srcEth = srcEth1
    dstEth = dstEth1
    type = type1

def setVariablesUDP(dstport1, srcport1, checksum1, length1):
    global dstport
    global srcport
    global cheksum
    global length
    dstport = dstport1
    srcport = srcport1
    cheksum = checksum1
    length = int(length1)

def setVariablesSSDP(mx1,st1,man1,host1,port1):
    global mx
    global st
    global man
    global host
    global port
    mx = mx1
    st = st1
    man = man1
    host = host1
    port = port1

def setVariablesNTP(modee1,disp1,IDNTP1,delay1,poll1,sent1,stra1,versn1,prec1,leap1,RefID1,rec1,org1,ref1):
    global leap
    global versionNTP
    global stratum
    global poll
    global precision
    global delay
    global dispersion
    global IDNTP
    global refID
    global ref
    global Origin
    global rev
    global sent
    global modee
    leap = leap1
    versionNTP = versn1
    modee = modee1
    stratum = stra1
    poll = poll1
    precision = prec1
    delay = delay1
    dispersion = disp1
    IDNTP = IDNTP1
    refID = RefID1
    ref = ref1
    Origin = org1
    rev = rec1
    sent = sent1

def setVariablesDNS(Qname1,Qtype1,Qclass1):
    global Qname
    global Qtype
    global Qclass
    Qname = Qname1
    Qtype = Qtype1
    Qclass = Qclass1

def saveDraft(type1):
    randomID = getID()
    now = datetime.now()
    date_object = date.today()
    current_time = now.strftime("%H:%M:%S")
    print(date_object)
    print(randomID, date_object,current_time, srcEth, dstEth,type, version, ihl, tos, totallength,id, flgs, frag, ttl, protocol, headersum, srcip, dstip, options, srcport, dstport, cheksum,type1, length)
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = """INSERT INTO Drafts(ID,Datee,Time,SourceETH,DestinationETH,Type,Version,IHL,TOS,TotalLength,Identification,Flags,FragmentOffset,TTL,Protocol,HeaderChecksum,SourceIP,DestinationIP,Options,SourcePort,DestinationPort,Checksum,PacketType,Length) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(add_draft, (randomID, date_object,current_time, srcEth, dstEth,type, version, ihl, tos, totallength,id, flgs, frag, ttl, protocol, headersum, srcip, dstip, options, srcport, dstport, cheksum,type1, length))
    conn.commit()
    if type1 == "SSDP":
        saveSSDP(randomID)
    elif type1 == "DNS":
        saveDNS(randomID)
    else:
        saveNTP(randomID)

    

def saveSSDP(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO SSDP2(ID,Hostt,Port,MAN,MX,ST) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(add_draft, (randomID,host,port, man,mx,st))
    conn.commit()

def saveNTP(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO NTP2(ID,Leap,Version,Modee,Stratum,Poll,Precisionn,Delay,Dispersion,ID2,ReferenceID,Reference,Origin,Receive,Sent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(add_draft, (leap,versionNTP,modee, stratum,poll,precision,delay,dispersion,IDNTP,refID,ref,Origin,rev,sent))
    conn.commit()


def saveDNS(randomID):
    conn = connectToDatabase()
    cursor = conn.cursor()
    add_draft = "INSERT INTO DNS2(ID,Qname,Qtype,Qclass) VALUES(%s,%s,%s,%s)"
    cursor.execute(add_draft, (randomID, Qname,Qtype,Qclass))
    conn.commit()


def getDrafts():
    conn = connectToDatabase()
    cursor = conn.cursor()
    Getdraft = "SELECT * FROM Drafts"
    cursor.execute(Getdraft)
    results = cursor.fetchall()
    return results

def getSelectedDraft(index):
    conn = connectToDatabase()
    cursor = conn.cursor()
    Getdraft = "SELECT * FROM Drafts WHERE ID = %s"
    cursor.execute(Getdraft, (index,))
    results = cursor.fetchone()
    return results

def getSelectedDraftType(index, type):
    conn = connectToDatabase()
    cursor = conn.cursor()
    if type == "DNS":
        Getdraft = "SELECT * FROM DNS2 WHERE ID = %s"
    elif type == "NTP":
        Getdraft = "SELECT * FROM NTP2 WHERE ID = %s"
    else:
        Getdraft = "SELECT * FROM SSDP2 WHERE ID = %s"

    cursor.execute(Getdraft, (index,))
    results = cursor.fetchone()
    return results

def getID():
    my_list = []
    if not my_list:
        n = random.randint(1,99)
        my_list.append(n)
        my_list = list(set(my_list))
    return my_list.pop(0)

def connectToDatabase():
	try:
		connection = mysql.connector.connect(host='127.0.0.1',database='paat',user='ahmed',password='1234')
		print('connection complete')
	except Error as e:
		print('Error while connecting')

	return connection	
