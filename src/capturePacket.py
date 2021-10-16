from scapy.all import *

'''
#Author: Samrah Tahir				 			              
#LAST MODIFIED: 16 Oct 2021			  			          
#PURPOSE: To capture the packets and calculate 	  
#amplificaiton 				           	 		            
'''
DNSQuery = {"src": '', "dst": '', "sport": ''} #temporary data structures
NTPQuery = {"src": '', "dst": '', "mode": 0}
NTPQueryList = []

'''
Purpose: captures packets on all interfaces
Input: None
Output: capturedPacket, 1 when unsuccessful
'''
def capturePackets():
	capturedPacket = sniff(stop_filter= lambda pkt: testLayer(pkt))
	
	if len(capturedPacket) == 0:
		return 1
'''
	for packet in capturedPacket:
		if packet.haslayer(DNS):
			handleDNS(packet)
		elif packet.haslayer(NTPHeader):
			handleNTP(packet)

'''

'''
Purpose: calculate ssdp packet length
Input: packet
Output: none
'''

def handleSSDP(packet):
	if packet.haslayer(UDP) and packet[UDP].dport == 1900 and packet.haslayer(Raw):
		ssdpQueryLen = len(packet[Raw])
	elif packet.haslayer(UDP) and packet[UDP].sport == 1900 and packet.haslayer(Raw):
		ssdpRespLen = len(packet[Raw])
	
	ampFactor = calculateAmpFactor(ssdpQueryLen, ssdpRespLen)
	print("ssdp ampfactor: ", ampFactor)

'''
Purpose: Comparing query packet and response packet
to calculate amplification
Input: packet
Output: none
'''
def handleDNS(packet):
	if packet.haslayer(DNS) and packet.haslayer(DNSQR) and not packet.haslayer(DNSRR):
		DNSQuery["src"] = packet[IP].src
		DNSQuery["dst"] = packet[IP].dst
		DNSQuery["len"] = packet[UDP].len
		DNSQuery["sport"] = packet[UDP].sport
   	elif packet.haslayer(DNS) and packet.haslayer(DNSRR):
		if packet[IP].dst == DNSQuery["src"] and packet[IP].src == DNSQuery["dst"] and packet[IP].dport == DNSQuery["sport"]:
			print("Amplification factor is ", calculateAmpFactor(DNSQuery["len"], getLength(packet)))
		#print("OG: ",DNSQuery["len"])#len w udp header 
			#print("resp ",getLength(packet))#len w udp header

'''
Purpose: calculates amplification percentage
Input: origLength, resLength
Output: ampFactor(%)
'''
def calculateAmpFactor(origLength, resLength):
	ampFactor = ((resLength - origLength)/origLength)*100
	return ampFactor

'''
Purpose: handles NTP packet
Input: packet
Output: None
'''
def handleNTP(packet):
	#if it is NTP and it a request from client
	if packet.haslayer(NTP) and packet[NTPHeader].mode == 3:
		NTPQuery["src"] = packet[IP].src
		NTPQuery["dst"] = packet[IP].dst
		NTPQuery["mode"] = packet[NTPHeader].mode
		NTPQuery["len"] = getLength(packet)
		NTPQueryList.append(NTPQuery)
		
	elif packet.haslayer(NTP) and packet[NTPHeader].mode == 4:
		if NTPQueryList[0]["src"] == packet[IP].dst:
			print(getLength(packet))

'''
Purpose: calculate length of NTP and DNS packets
(including UDP header bytes)
Input: pkt(packet)
Output: pkt[UDP].len(length of packet)
'''
def getLength(pkt):
	return pkt[UDP].len

'''
Purpose: testing the type of packet it is
Input: pkt(packet)
Output: None
'''
def testLayer(pkt):

	if pkt.haslayer(DNS):
		handleDNS(pkt)
	elif pkt.haslayer(NTP):
		print("ntp")
		handleNTP(pkt)
	elif pkt.haslayer(UDP):
		if pkt[UDP].dport ==1900 or pkt[UDP].sport == 1900:
			handleSSDP(pkt)
   

if __name__ == '__main__':
	if capturePackets() == 1:
		print("No packets captured.")

#def testFunc(pkt):
#	print(repr(pkt))

#print(len(capturedPacket))
#print(repr(capturedPacket))



