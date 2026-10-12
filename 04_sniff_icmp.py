from scapy.all import *

print("\n=== SCAPY DEMO 4: PACKET SNIFFING ===\n")
print("Waiting for 5 ICMP packets...")
print("Generate traffic from another Command Prompt with:")
print("    ping 8.8.8.8")
print("\nPress Ctrl+C to stop early.\n")

packets = sniff(filter="icmp", count=5)

print("\nCaptured packets:")
packets.nsummary()
