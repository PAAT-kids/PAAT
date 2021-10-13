import scapy.all as scapy

#scapy.send(packet)

def sendPacket(type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,ipOptions,udpSport,udpDport,udpChksum,listValues):
    #Ethernet Variables ethSrc ,ethDst

    packet = (scapy.Ether(src=ethSrc,dst=ethDst,type=ethType)
                /scapy.IP(version=ipVersion,ihl=ipIhl,tos=ipTos,len=ipLen,id=ipId,flags=ipFlags,frag=ipFrag,ttl=ipTtl,proto=ipProto,chksum=ipChksum,src=ipSrc,dst=ipDst,options=ipOptions)
                /scapy.UDP(sport=udpSport,dport=udpDport,chksum=udpChksum))

    if(type == 1):
        sendPacketDNS(packet,listValues)

    elif(type == 2):
        sendPacketNTP(packet,listValues)

    elif(type == 3):
        sendPacketSSDP(packet,listValues)

def sendPacketDNS(packet,listValues):

    packet = packet/scapy.DNS(rd=listValues[0],qd=listValues[1])



#def sendPacketNTP(packet,listValues):


#def sendPacketSSDP(packet,listValues):


    

scapy.send(scapy.IP(dst='8.8.8.8')/scapy.TCP(dport=53,flags='S'))

scapy.send(scapy.IP(dst="8.8.8.8")/scapy.UDP(dport = 53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="null.co.in")))


pkt = scapy.Ether(dst="01:01:01:01:01:01")/scapy.IP(dst="1.2.3.4")

pkt = pkt/scapy.IP(ttl=10)

pkt.show()