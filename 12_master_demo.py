from scapy.all import *

print("""
========================================
        SCAPY CLASSROOM DEMO
========================================
1. Build packet
2. Inspect fields
3. Send ICMP + receive response
4. Sniff ICMP
5. Hex dump
6. Show interfaces
0. Exit
""")

while True:
    choice = input("\nChoose demo: ").strip()

    if choice == "1":
        p = Ether() / IP(dst="8.8.8.8") / ICMP()
        p.show()

    elif choice == "2":
        p = IP(dst="8.8.8.8", ttl=64) / ICMP()
        print("Destination:", p[IP].dst)
        print("TTL:", p[IP].ttl)
        p.show2()

    elif choice == "3":
        print("Sending ICMP to 8.8.8.8...")
        r = sr1(IP(dst="8.8.8.8") / ICMP(), timeout=3, verbose=0)
        if r:
            r.show()
        else:
            print("No response.")

    elif choice == "4":
        print("Capture 5 ICMP packets. Generate traffic with ping 8.8.8.8")
        p = sniff(filter="icmp", count=5)
        p.nsummary()

    elif choice == "5":
        p = Ether() / IP(dst="8.8.8.8") / ICMP()
        hexdump(p)

    elif choice == "6":
        conf.ifaces.show()
        print("\nDefault interface:", conf.iface)

    elif choice == "0":
        print("Exiting.")
        break

    else:
        print("Choose 0-6.")
