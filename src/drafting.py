import scapy.all as scapy
import sys


srcip = ""
dstip = ""
totallength = 60
len = ""
version = ""
ihl = ""
tos = ""
id = ""
flgs = ""
frag = ""
protocol = ""
cheksum = ""
options = ""

def setVariables(srcip1,dstip1,totallength1,len1,version1,ihl1,tos1,id1,flgs1,frag1,protocol1,cheksum1,options1):
    srcip = srcip1
    dstip = dstip1
    totallength = totallength1
    len = len1
    version = version1
    ihl = ihl1
    tos = tos1
    id = id1
    flgs = flgs1
    frag = frag1
    protocol = protocol1
    cheksum = cheksum1
    options = options1

def sendTCP():
    scapy.sr(scapy.IP(dst=dstip, ttl = totallength)/scapy.TCP_SERVICES())

def sendEther():
    scapy.sr(scapy.IP(dst=dstip, ttl = totallength)/scapy.Ether())






