from scapy.all import *

print("\n=== SCAPY DEMO 1: BASIC PACKET LAYERS ===\n")

packet = Ether() / IP(dst="8.8.8.8") / ICMP()

print("Packet summary:")
print(packet.summary())

print("\nDetailed packet structure:")
packet.show()
