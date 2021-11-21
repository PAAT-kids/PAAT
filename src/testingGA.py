import scapy.all as scapy

packet1 = scapy.IP(dst='8.8.8.8')/scapy.UDP(dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname='klmgudbx . 6 7 . t l d',qtype='ALL',qclass='IN'))

packet = (scapy.IP(
                            version=4,
                            ihl=None,
                            tos=0,
                            #len=ipLen, #length is calculated later in the program, user shouldnt enter it 
                            id=1,
                            flags=0,
                            frag=0,
                            ttl=64,
                            proto=17,
                            #chksum=ipChksum,#either have to find a way to calculate chksum or just let scapy do it
                            src="192.168.56.128",
                            dst="8.8.8.8",
                            #options=ipOptions
                            )
                    /scapy.UDP(
                            sport=53,
                            dport=53,
                            #chksum=udpChksum #either have to find a way to calculate chksum or just let scapy do it
                            )
                    /scapy.DNS(rd=1,qd=scapy.DNSQR(qname='klmgudbx . 6 7 . t l d',qtype='ALL',qclass='IN' )
                            )
                    )
packet.show()
packet1.show()
print(len(packet))


response, unans= scapy.sr(packet,timeout=1,verbose=0,multi=True)

if len(response[scapy.UDP]) != 0:
    for responses in response[scapy.UDP]:
						print(responses[1][scapy.UDP].len)

#print(test[0][scapy.UDP][0])
#print(len(test[0][scapy.UDP][0]))