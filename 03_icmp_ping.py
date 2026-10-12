from scapy.all import *

print("\n=== SCAPY DEMO 3: SEND + RECEIVE WITH ICMP ===\n")
print("Sending one ICMP echo request to 8.8.8.8...\n")

packet = IP(dst="8.8.8.8") / ICMP()
response = sr1(packet, timeout=3, verbose=0)

if response:
    print("Response received:")
    response.summary()
    print("\nDetailed response:")
    response.show()
else:
    print("No response received.")
    print("If internet ICMP is blocked, use the packet construction demos instead.")
