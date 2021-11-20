from scapy.all import *
from localAddress import *
import threading
import random

popSize = 10
population = []
localIpAddresses = [ client for client in findLocalIps()]


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
					candidate.append(totalFitness)
					population.append(candidate)

						#print(repr(response))
		print(population)
				
def normalizeFitness():
	pass

if __name__ == '__main__':
    createInitPop()
#x.join()
