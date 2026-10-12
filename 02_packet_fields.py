from scapy.all import *

print("\n=== SCAPY DEMO 2: INSPECTING PACKET FIELDS ===\n")

packet = IP(dst="8.8.8.8", ttl=64) / ICMP()

print("Destination IP:", packet[IP].dst)
print("Source IP (before build):", packet[IP].src)
print("TTL:", packet[IP].ttl)
print("Protocol number:", packet[IP].proto)

print("\nFull packet:")
packet.show2()
