from scapy.all import *

print("\n=== SCAPY DEMO 7: RAW PACKET BYTES ===\n")

packet = Ether() / IP(dst="8.8.8.8") / ICMP()

print("Human-readable packet:")
packet.show2()

print("\nRaw hexadecimal representation:")
hexdump(packet)
