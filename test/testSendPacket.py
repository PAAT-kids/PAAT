"""
FILENAME: testSendPacket
AUTHOR: Majid Jafar
PURPOSE: Testfile for sendPacket.py
DATE CREATED: 05/10/2021
LAST EDITED DATE: 13/10/2021
"""

#To Access the file in src directory
import sys
sys.path.insert(0, 'src')

from sendPacket import sendPacketClass , sendPacket

#Testing sendPacket (DNS)
print("----------- TESTING DNS -----------\n")
print("Input: DNS PACKET INFORMATION\nExpected Output: Packet Confirmation and '1'\n")
print("Actual Output: ")
DNSlist =["b'www.example.com'",1,1]
print(sendPacket(1,"f4:d1:08:0f:84:12","c4:e9:0a:54:be:01","IPv4",4,None,0x0,None,1,"",0,64,"udp",None,"192.168.0.130","8.8.4.4","domain","domain",None,DNSlist))

print(sendPacket(1,"f4:d1:08:0f:84:12","c4:e9:0a:54:be:01","IPv4",4,None,0x0,None,1,"",0,64,"udp",None,"192.168.0.130","192.168.159.146","domain","domain",None,DNSlist))


#Testing sendPacket (NTP)
print("----------- TESTING NTP -----------\n")
print("Input: NTP PACKET INFORMATION\nExpected Output: Packet Confirmation and '1'\n")
print("Actual Output: ")
NTPList=[61,4,"client",2,10,0,0,0,"127.0.0.1",0,0,0,0,0]
print(sendPacket(2,"f4:d1:08:0f:84:12","c4:e9:0a:54:be:01","IPv4",4,None,0x0,None,1,"",0,64,"udp",None,"1.2.3.4","1.2.3.4","ntp","ntp",None,NTPList))

#Testing sendPacket (SSDP)
print("----------- TESTING SSDP -----------\n")
print("Input: SSDP PACKET INFORMATION\nExpected Output: Packet Confirmation and '1'\n")
print("Actual Output: ")
SSDPList = ["239.255.255.250.1900","1900","ssdp:all","ssdp:discover",2]
print(sendPacket(3,"f4:d1:08:0f:84:12","c4:e9:0a:54:be:01","IPv4",4,None,0x0,None,1,"",0,64,"udp",None,"1.2.3.4","1.2.3.4","ssdp","ssdp",None,SSDPList))

