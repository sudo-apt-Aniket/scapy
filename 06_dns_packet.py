from scapy.all import *

print("\n=== SCAPY DEMO 6: DNS PACKET CONSTRUCTION ===\n")

packet = IP(dst="8.8.8.8") / UDP(dport=53) / DNS(
    rd=1,
    qd=DNSQR(qname="example.com")
)

print("DNS packet structure:")
packet.show()

print("\nSummary:")
print(packet.summary())

print("\nThis demo constructs the DNS packet but does NOT transmit it.")
