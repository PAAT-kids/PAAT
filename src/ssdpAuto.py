from scapy.all import *
from localAddress import *
import threading
import random
from sendPacket import sendPacketClass

popSize = 10
totalGen = 7
gen = 0
population = []
fitness = []
localIpAddresses = [ client for client in findLocalIps()]
bestEver = ['0.0.0.0','']
fittest = 0


STHeaders = ["ssdp:all",
"upnp:rootdevice",
"urn:schemas-upnp-org:device:InternetGatewayDevice:1",
"urn:schemas-upnp-org:device:WANDevice:1",
"urn:schemas-upnp-org:device:WANConnectionDevice:1",
"urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1",
"urn:schemas-upnp-org:service:WANIPConnection:1",
"urn:schemas-upnp-org:service:Layer3Forwarding:1",
"urn:schemas-upnp-org:service:WANPPPConnection:1",
"urn:schemas-upnp-org:device:InternetGatewayDevice:",
"urn:schemas-upnp-org:device:WANDevice:",
"urn:schemas-upnp-org:service:WANCommonInterfaceConfig:",
"urn:schemas-upnp-org:device:WANConnectionDevice:",
"urn:schemas-upnp-org:service:WANPPPConnection:",
"urn:schemas-upnp-org:service:WANIPConnection:",
"urn:schemas-upnp-org:service:Layer3Forwarding:",
"urn:schemas-wifialliance-org:device:WFADevice:",
"urn:schemas-wifialliance-org:service:WFAWLANConfig:",
"uuid:IGD{8c80f73f-4ba0-45fa-835d-042505d052be}000000000000",
"urn:schemas-upnp-org:service:WANEthernetLinkConfig:1",
"uuid:WAN{84807575-251b-4c02-954b-e8e2ba7216a9}000000000000",
"urn:schemas-microsoft-com:service:OSInfo:1"]

def thread_function(num):
    ssdpR = sniff(filter='src host 192.168.1.1',timeout=num)
    print(ssdpR)
    for ssdp in ssdpR[UDP]:
    #print(ssdpR)
        print(repr(ssdp))
#step one: what is the ip address of the devices running the upnp services
#step two: what is the initial population
#x = threading.Thread(target=thread_function, args=(5,))
#x.start()
def createInitPop():
	global fittest
	print(localIpAddresses)
	if localIpAddresses:
		
		for ip in localIpAddresses:	
			for i in range(0,popSize):
				STHeader = random.choice(STHeaders)
				#ip = random.choice(localIpAddresses)
				query = IP(dst=ip)/UDP(sport=65165,dport=1900)/Raw(load='M-SEARCH * HTTP/1.1\r\nHOST: 239.    255.255.250:1900\r\nST: '+STHeader+'\r\n\r\nMAN: "ssdp:discover"\r\nMX: 1\r\n\r\n')
				response, unans= sr(query,timeout=1,verbose=0,multi=True)

				if len(response[UDP]) != 0:
					candidate = []
					totalFitness = 0
					for responses in response[UDP]:
						totalFitness += responses[1][UDP].len
					candidate.append(ip)
					candidate.append(STHeader)
					#candidate.append(totalFitness)
					population.append(candidate)
					fitness.append(totalFitness)
					if totalFitness > fittest:
						bestEver[0] = candidate[0]
						bestEver[1] = candidate[1]
						fittest = totalFitness
						#bestEver[2] = candidate[2]
						#print(repr(response))
			
		#print("parent population",population)
		#print("parent fitness", fitness)
				
#Purpose: Normalize the fitness values
def normalizeFitness():
	sum = 0
	for individual in fitness:
		sum += individual
		
	#print("sum is: "+str(sum))
	i = 0
	for i in range(0, len(population)):
		#print('pop[i][2]: ' +str(population[i][2]))
		print('sum: '+str(sum))
		normalizedFitness = float(fitness[i])/float(sum)
		fitness[i] = normalizedFitness
		#print(population[i][2])
		i = i + 1
	
		#print(normalizedFitness)
	print("Normalized pop:  ",population)
	print("fitness pop:  ",fitness)

	#print(sum)

#Purpose: make the next generation (new set of packets)
def nextGeneration():
	global population
	global fitness
	global fittest
	global gen
	newPopulation = []
	newFitness = []
	for i in range(0,len(population)):
		#parent1 = bestEver
		individual1 = bestEver
		individual2 = pickOne(population)
		individual = crossover(individual1, individual2)
		child = mutate(individual)
		query = IP(dst=child[0])/UDP(sport=65165,dport=1900)/Raw(load='M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nST: '+child[1]+'\r\n\r\nMAN: "ssdp:discover"\r\nMX: 1\r\n\r\n')
		response, unans= sr(query,timeout=1,verbose=0,multi=True)
		if len(response[UDP]) != 0:
			totalFitness = 0
			for responses in response[UDP]:
				totalFitness += responses[1][UDP].len
			#child[2] = totalFitness
			if totalFitness > fittest:
						bestEver[0] = child[0]
						bestEver[1] = child[1]
						fittest = totalFitness
		
			print("Kid fitness: "+str(totalFitness))
			newFitness.append(totalFitness)
			newPopulation.append(child)


	population = newPopulation
	fitness = newFitness
	gen = gen + 1

	#print("kid pop",population)

#Purpose: pick one from the parents based on fitness probably
def pickOne(population):
	index = 0
	r = random.random()
	
	while r  > 0 :
		if index < len(population):
			r = r - fitness[index]
			index = index + 1

	index = index - 1
	return population[index]

#Purpose: Mutate some value
def mutate(individual):
	if(random.random() < 0.1):
		individual[1] = random.choice(STHeaders)
	return individual

#Purpose: cross over values of parents
def crossover(parent1, parent2):
	child = []
	child.append(parent1[0])
	child.append(parent2[1])
	return child

if __name__ == '__main__':
	
	i = 0
	createInitPop()

	print("Parent New population: \n",population)
	
	while(i < totalGen):
		print("Current Best Ever:  ", bestEver, fittest)
		normalizeFitness()
		print("fitness: \n",fitness)
		# 	print('outside normalize')
		
		nextGeneration()
		print("Next gen New population: ",population)
		i = i + 1
	
	if bestEver[0] != '0.0.0.0' and bestEver[1] != '':
		queryPacket = Ether(src='94:65:9c:25:ef:40',dst='7c:8f:de:ab:cb:e0')/IP(src="192.168.1.16",dst=bestEver[0])/UDP(sport=4565,dport=1900)
		#payload = Raw(load='M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nST: '+bestEver[1]+'\r\n\r\nMAN: "ssdp:discover"\r\nMX: 1\r\n\r\n')
		listValue = ["239.255.255.250","1900","ssdp:discover","2",bestEver[1]]
		sendPkt = sendPacketClass()
		sendPkt.sendPacketSSDP(queryPacket,listValue)
		#packet = queryPacket/payload
		#send(packet)
		print("Best Ever:  ", bestEver, fittest)
		print("Total Gen: "+str(gen))
	else:
		print("No upnp services.")
#x.join()
