from scapy.all import *

print("\n=== SCAPY DEMO 10: READ A PCAP ===\n")

filename = "scapy_capture.pcap"

try:
    packets = rdpcap(filename)
    print(f"Loaded {len(packets)} packets from {filename}\n")
    packets.nsummary()
except FileNotFoundError:
    print(f"{filename} was not found.")
    print("Run 09_save_pcap.py first.")
