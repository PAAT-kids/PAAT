"""
FILENAME: sendPacket
AUTHOR: Majid Jafar
PURPOSE: Conatains methods to craft and send a complete packet
DATE CREATED: 01/10/2021
LAST EDITED DATE: 13/10/2021
"""

import scapy.all as scapy

"""
FUNCTION NAME: sendPacket
PURPOSE: Crafts the first three layers.
INPUT: String all the necessary value and a single list variable which conatins information of the specific UDP packet type
OUTPUT: Int result (1 = sent , 0 = error)
"""
def sendPacket(type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,udpSport,udpDport,udpChksum,listValues):


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
                        #options=ipOptions
                        )
                /scapy.UDP(
                        sport=udpSport,
                        dport=udpDport,
                        chksum=udpChksum
                        )
                    )

    if(type == 1):
        print("hi")
        sendPacketDNS(packet,listValues)

    elif(type == 2):
        sendPacketNTP(packet,listValues)

    elif(type == 3):
        sendPacketSSDP(packet,listValues)

"""
FUNCTION NAME: sendPacketDNS
PURPOSE: Crafts the final layer of the packet (DNS)
INPUT: Single list variable which conatins information of DNS packet
OUTPUT: Int result (1 = sent , 0 = error)
"""
def sendPacketDNS(packet,listValues):

    packet = packet/scapy.DNS(  rd=1,
                                qd=scapy.DNSQR(
                                            qname=listValues[0],
                                            qtype=listValues[1],
                                            qclass=listValues[2]
                                            )
                              )

    scapy.send(packet)

    packet.show()

    return 1

"""
FUNCTION NAME: sendPacketNTP
PURPOSE: Crafts the first three layers.
INPUT: Single list variable which conatins information of NTP packet
OUTPUT: Int result (1 = sent , 0 = error)
"""
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

    return 1

                                    

"""
FUNCTION NAME: sendPacketSSDP
PURPOSE: Crafts the first three layers.
INPUT: Single list variable which conatins information of the specific UDP packet type
OUTPUT: Int result (1 = sent , 0 = error)
"""
def sendPacketSSDP(packet,listValues):

    #packet = packet/

    return 0


 #Temproray sample input, Doesnt give the desired output yet   
DNSlist =["b'www.example.com'",1,1]
sendPacket(1,"f4:d1:08:0f:84:12","c4:e9:0a:54:be:01","IPv4",4,None,0x0,None,1,"",0,64,4,0x2a2c,"192.168.0.130","1.2.3.4",53627,27025,0x0d93,DNSlist)
