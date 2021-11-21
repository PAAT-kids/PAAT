"""
FILENAME: autoSend.py
AUTHOR: Majid Jafar
PURPOSE: contains the genetic algorithm for auto creat functionality
DATE CREATED: 25/10/2021
LAST EDITED DATE: 05/11/2021
"""
import fileinput
from sendPacket import sendPacket

#Object for sendpacket.py file
sPacket = sendPacket()

#required list variables to store values for feilds
solutions = []
rankedSolutions = []

"""
FUNCTION NAME: sendAutoPacket
PURPOSE: Calls the function to be tested
INPUT: Single list variable which conatins information of the packet
OUTPUT: int size of sent packet
"""
def sendAutoPacket(valuesList):
    return sPacket.autoSend(valuesList)
    
"""
FUNCTION NAME: fitness
PURPOSE: Determines the fitness of a particular combination
INPUT: Single list variable which conatins information of the packet
OUTPUT: int fitness of the combination
"""
def fitness(valuesList):
    finalSize = sendAutoPacket(valuesList)

    amplificationFactor = 10 - finalSize #Function will be called to calculate amplification factor

    return abs(amplificationFactor)

"""
FUNCTION NAME: processLine
PURPOSE: splits the csv file into valyes for each feild
INPUT: String Line
OUTPUT: List test
"""
def processLine(line):
    test = line.split(",")
    return test


"""
FUNCTION NAME: getSolutions
PURPOSE: Reads an input file to get the values
INPUT: none
OUTPUT: none
"""
def getSolutions():
    for line in fileinput.input(files ='autoCreate.txt'):
        solutions.append(processLine(line))


"""
FUNCTION NAME: runSolutions
PURPOSE: Main function of the genetic algorithm
INPUT: none
OUTPUT: none
"""
def runSolutions():
    for i in len(solutions):

        for s in solutions:
            rankedSolutions.append(fitness(solutions[s]) , s)
        
        rankedSolutions.sort()

"""
FUNCTION NAME: displayResult
PURPOSE: Temprory function to display the resulst of the genetic algorithm
INPUT: none
OUTPUT: none
"""
def displayResult():
    for x in rankedSolutions:
        print(x)
