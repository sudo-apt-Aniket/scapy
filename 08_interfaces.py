from scapy.all import *

print("\n=== SCAPY DEMO 8: NETWORK INTERFACES ===\n")

print("Scapy interfaces detected on this machine:\n")
conf.ifaces.show()

print("\nCurrent default interface:")
print(conf.iface)
