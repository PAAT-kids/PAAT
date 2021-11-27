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
ntpip = "216.239.35.4"
mode = [0,1,2,3]
leaplist = [0]
versionlist = [1,2,3,4]
solutions = [""] * 100
rankedSolutions = [""] * 50
rankedmode = [""] * 10
rankedversion = [""] * 10
rankedleap= [""] * 10

"""
FUNCTION NAME: sendAutoPacket
PURPOSE: Calls the function to be tested
INPUT: Single list variable which conatins information of the packet
OUTPUT: int size of sent packet
"""
def sendAutoPacket(valuesList):
    packet = (scapy.IP(
                            #version=4,
                            #ihl=5,
                            #tos=0,
                            #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                            #id=1,
                            #flags=0,
                            #frag=0,
                            #ttl=64,
                            #proto=17,
                            #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                            src="192.168.1.153",
                            dst=ntpip,
                            #options=ipOptions
                            )
                    /scapy.UDP(
                            sport=50000,
                            dport=123,
                            #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                            )
                    /scapy.NTPHeader(
                                    leap=valuesList[1],
                                    version=valuesList[2],
                                    mode=valuesList[3],
                                    )

                    )


    packetSize = int(sPacket.autoSendNTP(packet))
    print(packetSize)
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
        solutions[x] = [0 , random.choice(mode) , random.choice(leaplist) , random.choice(versionlist)]


"""
FUNCTION NAME: getRankedSolutions
PURPOSE: Reads an input file to get the values
INPUT: none
OUTPUT: none
"""
def getRankedSolutions():
    for x in range (0 ,10):
        rankedmode[x] = solutions[x][1]
        rankedversion[x] = solutions[x][3]
        rankedleap[x] = solutions[x][2]
        

    for x in range (0 , 50):
        rankedSolutions[x] = [0 , random.choice(rankedmode) , random.choice(rankedversion) , random.choice(rankedleap)]


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
        sizePkt = scapy.IP(dst="216.239.35.4")/scapy.UDP(sport=50000,dport=123)/scapy.Raw(load=ldDict)
        print(sizePkt)
        return sizePkt



getSolutions()
runSolutions()

getRankedSolutions()
runRankedSolutions()
