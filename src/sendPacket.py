import scapy.all as scapy

#scapy.send(packet)

def sendPacket(type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,ipOptions,udpSport,udpDport,udpChksum,listValues):
    #Ethernet Variables ethSrc ,ethDst

    packet = (scapy.Ether(
                        src=ethSrc,
                        dst=ethDst,
                        type=ethType
                        )
                /scapy.IP(
                        version=ipVersion,
                        ihl=ipIhl,
                        tos=ipTos,
                        len=ipLen,
                        id=ipId,
                        flags=ipFlags,
                        frag=ipFrag,
                        ttl=ipTtl,
                        proto=ipProto,
                        chksum=ipChksum,
                        src=ipSrc,
                        dst=ipDst,
                        options=ipOptions
                        )
                /scapy.UDP(
                        sport=udpSport,
                        dport=udpDport,
                        chksum=udpChksum
                        )
                    )

    if(type == 1):
        sendPacketDNS(packet,listValues)

    elif(type == 2):
        sendPacketNTP(packet,listValues)

    elif(type == 3):
        sendPacketSSDP(packet,listValues)

def sendPacketDNS(packet,listValues):

    packet = packet/scapy.DNS(  rd=1,
                                qd=scapy.DNSQR(
                                        qname=listValues[0],
                                        qtype=listValues[1],
                                        qclass=listValues[2]
                                        )
                              )

    scapy.send(packet)


def sendPacketNTP(packet,listValues):

    packet = packet/scapy.NTPHeader(
                                        leap=listValues[0],
                                        version=listValues[1],
                                        mode=listValues[2],
                                        stratum=listValues[3],
                                        poll=listValues[4],
                                        precision=listValues[5],
                                        delay=listValues[6],
                                        dispersion=listValues[7],
                                        id=listValues[8],
                                        ref_id=listValues[9],
                                        ref=listValues[10],
                                        orig=listValues[11],
                                        recv=listValues[12],
                                        sent=listValues[13]
                                        
                                        )

    scapy.send(packet)

                                    


#def sendPacketSSDP(packet,listValues):


    

scapy.send(scapy.IP(dst='8.8.8.8')/scapy.TCP(dport=53,flags='S'))

scapy.send(scapy.IP(dst="8.8.8.8")/scapy.UDP(dport = 53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="null.co.in")))


pkt = scapy.Ether(dst="01:01:01:01:01:01")/scapy.IP(dst="1.2.3.4")

pkt = pkt/scapy.IP(ttl=10)

pkt.show()