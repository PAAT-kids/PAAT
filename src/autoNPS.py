"""
FILENAME: autoSend.py
AUTHOR: Majid Jafar
PURPOSE: contains the genetic algorithm for auto creat functionality
DATE CREATED: 25/10/2021
LAST EDITED DATE: 05/11/2021
"""
import random

import scapy.all as scapy

from sendPacket import sendPacketClass

#Object for sendpacket.py file
sPacket = sendPacketClass()

#required list variables to store values for feilds
mode = [1,2]
leaplist = 10
versionlist = [1,2,3]
stratumList = [1 , 2 , 3 , 4 , 5, 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15, 16,]
delayList = [0.00489807128906,0.00489807128906]
polllist = 10
solutions = [""] * 100
rankedSolutions = [""] * 50
rankedQNAME = [""] * 10
rankedQCLASS = [""] * 10
rankedQTYPE = [""] * 10

"""
FUNCTION NAME: sendAutoPacket
PURPOSE: Calls the function to be tested
INPUT: Single list variable which conatins information of the packet
OUTPUT: int size of sent packet
"""
def sendAutoPacket():
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
                            src="192.168.1.153",
                            dst="132.163.97.5",
                            #options=ipOptions
                            )
                    /scapy.UDP(
                            sport=4040,
                            dport=123,
                            #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                            )
                    /scapy.NTPHeader(
                                    #leap=leaplist,
                                    #version=versionlist[1],
                                    #mode=mode[1],
                                    #stratum=stratumList[3],
                                    #poll=polllist,
                                    #precision=235,
                                    #delay=delayList[0],
                                    #dispersion=0.0449066162109,  
                                    )

                    )

    srcPort = scapy.RandShort()._fix()
    #packet[scapy.UDP].sport = srcPort
    sizePkt = sizePacket('\"NTP\"',srcPort,packet[scapy.UDP].len)
    #print('\"NTP\"')
    #scapy.send(sizePkt)
    scapy.sr(packet)
    
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


def sizePacket(Type,QID, size):
        t = '\"Type\"'
        q = '\"QID\"'
        s = '\"size\"'
        ldDict = f"{{{t}:" +Type+f",{q}:"+str(QID)+f",{s}:"+str(size)+"}"
        print('QID: '+str(QID))
        sizePkt = scapy.IP(dst="132.163.96.5")/scapy.UDP(sport=4040,dport=123)/scapy.Raw(load=ldDict)
        return sizePkt



sendAutoPacket()