from scapy.all import *

#PURPOSE: calculate the cost that goes into sending and receiving arp msgs
def get_arp_cost(destinationIP,serverIP):
	#step1: send an arp broadcast to get the mac address of the receiver machine(src)
	#step2: receive the mac address and calculate the response size
	#step3: send an arp broadcast to get the mac address of the servers(dns,ntp, ssdp)
	#step4: receive the mac address and calcualte the response size
	#step5: get total of request and response sizes
	serverARPResp=None 
	receiverResp=None
	receiverARPReq = Ether()/ARP()
	arppkt = Ether()/ARP()
	receiverResp = sendARPPacket(receiverARPReq,destinationIP)
			
	serverARPResp = sendARPPacket(arppkt,serverIP)	

	if serverARPResp == -1 and receiverResp == -1:
		print('No Additional Cost Calculated.')
	elif serverARPResp == -1:
		print('No Additional Cost for destination calculated.')
	elif receiverResp == -1:
		print('No Additional Cost for Source calculated.')	
	elif serverARPResp != -1 and receiverResp != -1:
		totalReqSize = len(arppkt) + len(receiverARPReq)
		totalResponse = len(serverARPResp) + len(receiverResp)
		print('Total Req Size: '+str(totalReqSize))
		print('Total Response '+str(totalResponse))

#PURPOSE: send arp broadcast packet and receive response
def sendARPPacket(arpPkt,destinationIP):
	arpPkt[ARP].hwsrc = '00:0c:29:4a:f5:5b' #sender mac address
	arpPkt[ARP].pdst = destinationIP #receiver machine ip address
	arpPkt[Ether].dst = "ff:ff:ff:ff:ff:ff"
	rans,runans = srp(arpPkt, filter='arp',timeout=3,verbose=False)
	
	if len(rans) != 0:
		if rans[ARP][0][1].haslayer(ARP):
			return rans[ARP][0][1]
	
	return -1

#Purpose: get mac of local ip address
def getMac(ip):
	arppkt = Ether()/ARP()
	resp = sendARPPacket(arppkt,ip)

	if resp != 1:
		if resp.haslayer(ARP):
			return resp.getlayer(ARP).hwsrc
	return -1

#Purpose: caller function
def arpAdditionalCost(source,dest):
	get_arp_cost(source,dest)

if __name__ == '__main__':
	arpAdditionalCost("0.0.0.0","0.0.0.0")
