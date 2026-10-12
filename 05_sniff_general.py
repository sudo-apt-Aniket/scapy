from scapy.all import *

print("\n=== SCAPY DEMO 5: GENERAL PACKET SNIFFING ===\n")
print("Capturing 10 packets. This may include normal background traffic.\n")

packets = sniff(count=10)

print("\nPacket summary:")
packets.nsummary()
