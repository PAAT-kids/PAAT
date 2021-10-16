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

    out = 0

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
        out = sendPacketDNS(packet,listValues)

    elif(type == 2):
        out = sendPacketNTP(packet,listValues)

    elif(type == 3):
        out = sendPacketSSDP(packet,listValues)

    return out

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

    scapy.sendp(packet)

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
                                #ref_id=listValues[9],
                                ref=listValues[10],
                                orig=listValues[11],
                                recv=listValues[12],
                                sent=listValues[13]
                                
                                )

    scapy.sendp(packet)


    return 1

                                    

"""
FUNCTION NAME: sendPacketSSDP
PURPOSE: Crafts the first three layers.
INPUT: Single list variable which conatins information of the specific UDP packet type
OUTPUT: Int result (1 = sent , 0 = error)
"""
def sendPacketSSDP(packet,listValues):


    payload = "M-SEARCH * HTTP/1.1\r\n" \
        "HOST:" + listValues[0] + ":" + listValues[1] + "\r\n" \
        "ST:"+ listValues[2] + "\r\n" \
        "MAN:" + "\""+ listValues[3] +"\" \r\n" \
        "MX:" + str(listValues[4]) +"\r\n\r\n"                

    packet = packet/payload

    scapy.sendp(packet)

    return 1

DNSlist =["b'www.example.com'",1,1]

q = (scapy.IP(dst='8.8.8.8') / scapy.UDP(dport=53) / scapy.DNS(rd=1, qd=scapy.DNSQR(qname='www.thepacketgeek.com')))

answer = scapy.sr1(q, verbose=0)