from scapy.all import *

print("\n=== SCAPY DEMO 11: TCP AND UDP CONSTRUCTION ===\n")

tcp_packet = IP(dst="192.0.2.1") / TCP(dport=80, flags="S")
udp_packet = IP(dst="192.0.2.1") / UDP(dport=53)

print("TCP packet - constructed only, NOT sent:")
tcp_packet.show2()

print("\nUDP packet - constructed only, NOT sent:")
udp_packet.show2()

print("\nThe destination 192.0.2.1 is a documentation/test address.")
