import scapy.all as scapy

packet = scapy.IP(dst="1.1.1.1")/scapy.UDP(dport=65)

scapy.send(packet)

test = scapy.sr(scapy.IP(dst='8.8.8.8')/scapy.UDP(dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname='www.google.com',qtype='A')))