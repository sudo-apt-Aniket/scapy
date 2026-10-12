from scapy.all import *

# 1. Construct
packet = IP(dst="8.8.8.8") / ICMP()

# 2. Inspect
packet.show()

# 3. Send and receive
response = sr1(packet, timeout=3)
if response:
    response.show()
