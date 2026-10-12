from scapy.all import *

print("\n=== SCAPY DEMO 9: CAPTURE AND SAVE AS PCAP ===\n")
print("Capturing 5 ICMP packets.")
print("Generate traffic with: ping 8.8.8.8\n")

packets = sniff(filter="icmp", count=5)

output = "scapy_capture.pcap"
wrpcap(output, packets)

print(f"\nSaved {len(packets)} packets to: {output}")
print("You can open this PCAP directly in Wireshark.")
