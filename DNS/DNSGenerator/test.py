from scapy.all import *

#resp = sr1(IP(dst="192.168.45.20")/ICMP())

#print(resp[0].summary)
result = sr1(IP(src="192.168.45.200",dst="192.168.55.2")/UDP()/DNS(rd=1,qd=DNSQR(qname="kdn.cyberdrill.my")),timeout=10,verbose=0,iface='ens34')

print(result[DNS].summary())