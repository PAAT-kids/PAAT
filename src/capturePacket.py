from scapy.all import sniff, Raw, UDP,DNSQR,DNSRR

recvIP = "127.0.0.1" #replace with host comps IP
srcIP = ""
dnsIP = "8.8.8.8" #replace with our own dns server
def checkSelectedOption():
    rawPacket=''
    #option = sniff(stop_filter= lambda x: x.haslayer(Raw))
    
    while(True):
       
        option = sniff(filter = "udp and dst host 1.2.3.4", stop_filter= lambda x: x.haslayer(Raw))
        print("outside sniff that was in while.")
        for rawPacket in option[UDP]:
            if rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'DNS':
                 break #breaking for loop
	    elif rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'NTP':
		 break
	    elif rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'SSDP':
		 break
        if rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'DNS':
            print("found dns")
            printDNSVal(rawPacket) #printDNSValues
            break #breaking while loop
	elif rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'NTP':
            print("found ntp")
            #printDNSVal(rawPacket) #printDNSValues
            break #breaking while loop
	elif rawPacket.haslayer(Raw) and rawPacket.getlayer(Raw).load == 'SSDP':
            print("found ssdp")
            printSSDPVal(rawPacket) #printDNSValues
            break #breaking while loop
        print("continuing while loop")
        
    
    
    #print(option[0][Raw].load)

#ssdp packet handle
#sport for ssdp query is 65165 and dport is ofc 1900
def printSSDPVal(ssdpPacket):
	ssdpQPacket = None
	ssdpAnsPacket = []
	#various packets may be captured in one sniff
	ssdpPackets = sniff(filter="udp and port 65165", timeout=5) #sniffs for at most 5 secs
	
	for ssdpPacket in ssdpPackets[UDP]:
		if ssdpPacket.sport == 65165 and ssdpPacket.dport == 1900:
			ssdpQPacket = ssdpPacket#should be the ssdp Q packet
		elif ssdpPacket.dport == 65165 and ssdpPacket.sport == 1900:
			ssdpAnsPacket.append(ssdpPacket)#should be the ssdp Ans packets

		
	if ssdpQPacket and ssdpAnsPacket:
		print("Length of SSDP Q Packet is: "+str(dnsQAlengthCal(ssdpQPacket)))
		print("total length of ssdp Ans packets is: "+str(ssdpAlengthCal(ssdpAnsPacket)))
		print("Amplification :"+str(dnsAmplificationFactor(dnsQAlengthCal(ssdpQPacket), ssdpAlengthCal(ssdpAnsPacket))))

#calculate length of ssdp responses in total
def ssdpAlengthCal(ssdpPacket):
	total = 0
	for ssdpPkt in ssdpPacket:
		total = total + dnsQAlengthCal(ssdpPkt)
	return total
'''
NTP notes: can know whether its a query or answer by looking at the sport and dport
'''
def printNTPVal(ntpPacket):
	ntpQPacket = None
	ntpAnsPacket = None

	print("inside printNTPVal")
	
	
#for printing dns values
def printDNSVal(dnsPacket):
    dnsQPacket = None
    dnsAnsPacket = None
    print("inside printDNSVal")
    dnsPackets = sniff(filter = "host "+dnsIP, prn= lambda x: x.haslayer(DNSQR) or x.haslayer(DNSRR))
    print("dnsqpacket stopped sniffing.")
    for dnsPacket in dnsPackets[UDP]:
        if dnsPacket.haslayer(DNSQR) and dnsPacket.getlayer(UDP).dport==53:
            dnsQPacket = dnsPacket #getting the dns query packet
        elif dnsPacket.haslayer(DNSRR) and dnsPacket.getlayer(UDP).sport==53:
            dnsAnsPacket = dnsPacket#getting the dns response record packet
    #dnsAnsPacket = sniff(filter = "dst host 192.168.231.173", prn= lambda x: x.haslayer(DNSRR), timeout=5,quiet=True)
    if dnsQPacket and dnsAnsPacket:

        #functions for dnsq length calculations
        print("dnsQ length: "+str(dnsQAlengthCal(dnsQPacket)))
        #functions for dnsa length calculations
        print("dnsAns length: "+str(dnsQAlengthCal(dnsAnsPacket)))
        #function to calculate the amplification
        dnsAmplificationFactor(dnsQAlengthCal(dnsQPacket),dnsQAlengthCal(dnsAnsPacket))

        print("dnsQPacket: ")
        print(repr(dnsQPacket))
        print("dnsAnsPacket: ")
        print(repr(dnsAnsPacket))

#calculate length of dnsq
def dnsQAlengthCal(dnsQPkt):
    dnsQPacketLength = dnsQPkt.getlayer(UDP).len
    return dnsQPacketLength

#calculate dns amplification
def dnsAmplificationFactor(qLength, rlength):
    ampFactor = (float((rlength - qLength))/float(qLength))*100
    print("***The Amplification for dns is****"+str(ampFactor)+"%")












def checkLayer(pkt):
    if(pkt.haslayer(Raw) and pkt[0][Raw].load == 'DNS'):
        sniffDNSPackets()
        #print(pkt[0][Raw].load)

        return 1


def sniffDNSPackets():
    print("1")
    sniff(filter = "udp and host "+recvIP, prn=extractDNSInfo)
   

def extractDNSInfo():
     print("2")
     print("sniffing packets")
checkSelectedOption()
