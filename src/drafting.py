import scapy.all as scapy
import sys


srcip = ""
dstip = "192.1.168.1"
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

scapy.sr(scapy.IP(dst=dstip, ttl = totallength)/scapy.ICMP())


