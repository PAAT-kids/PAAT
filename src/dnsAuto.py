"""
FILENAME: autoSend.py
AUTHOR: Majid Jafar
PURPOSE: contains the genetic algorithm for auto creat functionality
DATE CREATED: 25/10/2021
LAST EDITED DATE: 01/12/2021
"""
import random

import scapy.all as scapy
from arpCost import getMac

from sendPacket import sendPacketClass

#Object for sendpacket.py file
sPacket = sendPacketClass()

#required list variables to store values for feilds
global packetFinal 

packetFinal = ( scapy.Ether()
                        /scapy.IP(
                                version=4,
                                ihl=5,
                                tos=0,
                                #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                                id=1,
                                flags=0,
                                frag=0,
                                ttl=64,
                                proto=17,
                                #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                                src= "1.1.1.1",
                                dst= "8.8.8.8",
                                #options=ipOptions
                                )
                        /scapy.UDP(
                                sport=53,
                                dport=53,
                                #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                                )
                        )
qnameList = [' h c l g t i x c . 6 7 . t l d' , 'p i r u z c o a . 6 7 . t l d' , 'n d h p q u o f . 6 7 . t l d' , 'klmgudbx . 6 7 . t l d' , 's t f v c q l e . 6 7 . t l d' , 'e p h p s f f z g b . 2 0 5 8 5 1 . t l d', 's o r z q l o e p v . 2 5 6 6 8 1 . t l d' , 'niqvmmygdo . 2 3 9 1 7 8 . t l d' , ]
qclassList = ['IN', 'CH' , 'HS' , 'ANY']
qtypeList = ['A' , 'NS' , 'MD' , 'MF' , 'CNAME' , 'SOA', 'MB' , 'MG' , 'MR' , 'NULL' , 'WKS' , 'PTR' , 'HINFO' , 'MINFO' , 'MX' , 'TXT', 'RP' , 'AFSDB' , 'X25' , 'ISDN' , 'RT' , 'OPT' , 'NSEC' , 'URI' , 'TA']
solutions = [""] * 100
rankedSolutions = [""] * 50
rankedQNAME = [""] * 10
rankedQCLASS = [""] * 10
rankedQTYPE = [""] * 10
ipSource = ""
ipDestination = ""

"""
FUNCTION NAME: sendAutoPacket
PURPOSE: Calls the function to be tested
INPUT: Single list variable which conatins information of the packet
OUTPUT: int size of sent packet
"""
def sendAutoPacket(valuesList):
    packet = (scapy.IP(
                            version=4,
                            ihl=5,
                            tos=0,
                            #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                            id=1,
                            flags=0,
                            frag=0,
                            ttl=64,
                            proto=17,
                            #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                            src= ipSource,
                            dst= "8.8.8.8",
                            #options=ipOptions
                            )
                    /scapy.UDP(
                            sport=53,
                            dport=53,
                            #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                            )
                    /scapy.DNS(     rd=1,
                                    qd=scapy.DNSQR(
                                                qname=valuesList[1],
                                                qtype=valuesList[2],
                                                qclass=valuesList[3]
                                            )
                            )
                    )

    packetSize = int(sPacket.autoSendDNS(packet))

    return packetSize
    
"""
FUNCTION NAME: fitness
PURPOSE: Determines the fitness of a particular combination
INPUT: Single list variable which conatins information of the packet
OUTPUT: int fitness of the combination
"""
def fitness(valuesList):
    finalSize = sendAutoPacket(valuesList)

    return abs(finalSize)


"""
FUNCTION NAME: getSolutions
PURPOSE: Reads an input file to get the values
INPUT: none
OUTPUT: none
"""
def getSolutions():
    for x in range (0 , 100):
        solutions[x] = [0 , random.choice(qnameList) , random.choice(qtypeList) , random.choice(qclassList)]


"""
FUNCTION NAME: getRankedSolutions
PURPOSE: Reads an input file to get the values
INPUT: none
OUTPUT: none
"""
def getRankedSolutions():
    for x in range (0 ,10):
        rankedQNAME[x] = solutions[x][1]
        rankedQCLASS[x] = solutions[x][3]
        rankedQTYPE[x] = solutions[x][2]
        

    for x in range (0 , 50):
        rankedSolutions[x] = [0 , random.choice(rankedQNAME) , random.choice(rankedQTYPE) , random.choice(rankedQCLASS)]


"""
FUNCTION NAME: runSolutions
PURPOSE: Main function of the genetic algorithm
INPUT: none
OUTPUT: none
"""
def runSolutions():
    for i in range(len(solutions)):
        solutions[i][0] = fitness(solutions[i])
        
    solutions.sort()

    solutions.reverse()

"""
FUNCTION NAME: runRankedSolutions
PURPOSE: Main function of the genetic algorithm
INPUT: none
OUTPUT: none
"""

def runRankedSolutions():
    for i in range(len(rankedSolutions)):
        rankedSolutions[i][0] = fitness(rankedSolutions[i])
        
    rankedSolutions.sort()

    rankedSolutions.reverse()



def startDNSAuto(source,destination):

    ipSource = source
    ipDestination = destination

    getSolutions()
    runSolutions()

    getRankedSolutions()
    runRankedSolutions()

    print("THE BEST SOLUTION IS")
    print(rankedSolutions[0])
    prompt = '<div> <h1> DNS Best Fields: </h1>' +'<p> Qname: '+ rankedSolutions[0][1]+'</p>'+'<p> Qtype: '+ rankedSolutions[0][2]+'<p> Qclass: '+ rankedSolutions[0][3]+'</p>'+'</div>'

    sendFinalPacket(source,destination)

    return prompt

def sendFinalPacket(source,destination):
    srcMac = getMac(source)
    dstMac = getMac(destination)
    
    if srcMac is not None and dstMac is not None:
        packetFinal = ( scapy.Ether(
                                src = srcMac,
                                dst = dstMac
                        )
                        /scapy.IP(
                                version=4,
                                ihl=5,
                                tos=0,
                                #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                                id=1,
                                flags=0,
                                frag=0,
                                ttl=64,
                                proto=17,
                                #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                                src= ipDestination,
                                dst= "8.8.8.8",
                                #options=ipOptions
                                )
                        /scapy.UDP(
                                sport=53,
                                dport=53,
                                #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                                )
                        )
    else:
        packetFinal = (scapy.Ether(
                                src = srcMac,
                                dst = dstMac
                        )
                        /scapy.IP(
                                version=4,
                                ihl=5,
                                tos=0,
                                #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                                id=1,
                                flags=0,
                                frag=0,
                                ttl=64,
                                proto=17,
                                #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                                src= ipDestination,
                                dst= "8.8.8.8",
                                #options=ipOptions
                                )
                        /scapy.UDP(
                                sport=53,
                                dport=53,
                                #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                                )
                        )

    sendlist = [rankedSolutions[0][1],rankedSolutions[0][2],rankedSolutions[0][3]]
    sPacket.sendPacketDNS(packetFinal, sendlist)