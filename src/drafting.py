import scapy.all as scapy
import sys
from mysql.connector import MySQLConnection, Error
from scapy.utils import checksum
from python_mysql_dbconfig import read_db_config

primarykey = 0
Size = 20
senderAd = ""
recAdd = ""
srcEth = ""
dstEth = ""
type = ""
version = ""
ihl = ""
tos = ""
totallength = 60
id = ""
flgs = ""
frag = ""
ttl = 60
protocol = ""
headersum = ""
srcip = ""
dstip = ""
options = ""
srcport = ""
dstport = ""
cheksum = ""

def setVariables1(srcip1,dstip1,totallength1,version1,ihl1,tos1,id1,flgs1,frag1,protocol1,headersum1,options1):
    srcip = srcip1
    dstip = dstip1
    totallength = totallength1
    version = version1
    ihl = ihl1
    tos = tos1
    id = id1
    flgs = flgs1
    frag = frag1
    protocol = protocol1
    headersum = headersum1
    options = options1

def setVariables2(srcEth1, dstEth1, type1, userid1):
    srcEth = srcEth1
    dstEth = dstEth1
    type = type1
    UserID = userid1

def setVariables3(dstport1, srcport1, checksum1, senderAd1, recAdd1):
    dstport = dstport1
    srcport = srcport1
    checksum = checksum1
    senderAd = senderAd1
    recAdd = recAdd1



def saveDraft():
    query = "INSERT INTO Drafts(ID,Size,SenderAdd,ReceiverAdd,SourceETH,DestinationETH,Type,Version,IHL,TOS,TotalLength,Identification,Flags,FragmentOffset,TTL,Protocol,HeaderChecksum,SourceIP,DestinationIP,Options,SourcePort,DestinationPort,Checksum) " \
            "VALUES(%s,%d,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%s,%d,%s,%s)"
    args = (primarykey,Size, senderAd, recAdd, srcEth, dstEth, type, version, ihl, tos, totallength, id, flgs, frag,ttl,protocol,headersum,srcip,dstip,options,srcport,dstport,cheksum)
    primarykey = primarykey + 1
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def sendUDP():
    scapy.sr(scapy.IP(dst=dstip, ttl = totallength)/scapy.UDP_SERVICES())

def sendEther():
    scapy.sr(scapy.IP(dst=dstip, ttl = totallength)/scapy.Ether())

def sendIP():
    scapy.sr(scapy.IP(dst=dstip, ttl = totallength))


