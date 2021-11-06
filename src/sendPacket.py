"""
FILENAME: sendPacket.py
AUTHOR: Majid Jafar
PURPOSE: Conatains methods to craft and send a complete packet
DATE CREATED: 01/10/2021
LAST EDITED DATE: 16/10/2021
"""

import scapy.all as scapy

class sendPacket:

    ethSrc = ""
    ethDst =""
    ethType =""
    ipVersion =""
    ipIhl =""
    ipTos = ""
    ipLen = ""
    ipId = ""
    ipFlags = ""
    ipFrag = ""
    ipTtl =""
    ipProto = ""
    ipChksum = ""
    ipOpt = ""
    ipSrc =""
    ipDst =""
    udpSport ="" 
    udpDport = ""
    udpChksum = ""
    listValues = ""


    def setEthernet (self,ethSrc1,ethDst1,ethType1):
        self.ethSrc = ethSrc1
        self.ethDst = ethDst1
        self.ethType = ethType1
        print(self.ethSrc,self.ethDst,self.ethType)

    def setIP (self,ipVersion1,ipIhl1,ipTos1,ipLen1,ipId1,ipFlags1,ipFrag1,ipTtl1,ipProto1,ipChksum1,ipOpt1,ipSrc1,ipDst1):
        ipVersion = ipVersion1
        ipIhl = ipIhl1
        ipTos = ipTos1
        ipLen = ipLen1
        ipId = ipId1
        ipFlags = ipFlags1
        ipFrag = ipFrag1
        ipTtl = ipTtl1
        ipProto = ipProto1
        ipChksum = ipChksum1
        ipOpt = ipOpt1
        ipSrc = ipSrc1
        ipDst = ipDst1

        print(ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipOpt,ipSrc,ipDst)
        print(self.ethSrc,self.ethDst,self.ethType)

    def setUDP()
    """
    FUNCTION NAME: sendPacket
    PURPOSE: Crafts the first three layers.
    INPUT: String all the necessary value and a single list variable which conatins information of the specific UDP packet type
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacket(self,type,ethSrc,ethDst,ethType,ipVersion,ipIhl,ipTos,ipLen,ipId,ipFlags,ipFrag,ipTtl,ipProto,ipChksum,ipSrc,ipDst,udpSport,udpDport,udpChksum,listValues):

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
        
        initPacket = (scapy.Ether(
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
                            sport=6500,
                            dport=6500,
                            chksum=udpChksum
                            )
                        )

        if(type == 1):
            self.sendInitPacket(initPacket,"DNS")
            out = self.sendPacketDNS(packet,listValues)

        elif(type == 2):
            self.sendInitPacket(initPacket,"SSDP")
            out = self.sendPacketNTP(packet,listValues)

        elif(type == 3):
            self.sendInitPacket(initPacket,"NTP")
            out = self.sendPacketSSDP(packet,listValues)

        return out



    """
    FUNCTION NAME: sendInitPacket
    PURPOSE: Sends a packet to the destination informing the packet type
    INPUT: A packet with pre loaded information and a string determining the type of data
    OUTPUT: None
    """
    def sendInitPacket(self,packet,type):
        packet = packet/scapy.Raw(load=type)

        scapy.sendp(packet)

    """
    FUNCTION NAME: sendPacketDNS
    PURPOSE: Crafts the final layer of the packet (DNS)
    INPUT: Single list variable which conatins information of DNS packet
    OUTPUT: Int result (1 = sent , 0 = error)
    """
    def sendPacketDNS(self,packet,listValues):

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
    def sendPacketNTP(self,packet,listValues):

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
    def sendPacketSSDP(self,packet,listValues):


        payload = "M-SEARCH * HTTP/1.1\r\n" \
            "HOST:" + listValues[0] + ":" + listValues[1] + "\r\n" \
            "ST:"+ listValues[2] + "\r\n" \
            "MAN:" + "\""+ listValues[3] +"\" \r\n" \
            "MX:" + str(listValues[4]) +"\r\n\r\n"                

        packet = packet/payload

        scapy.sendp(packet)

        return 1
