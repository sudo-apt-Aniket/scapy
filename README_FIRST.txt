SCAPY DEMO KIT - WINDOWS + WIRESHARK
====================================

You already have Scapy installed.

IMPORTANT:
- "python -m scapy" opens the Scapy interactive shell.
- Once you see ">>>", you are INSIDE Scapy.
- Commands such as "python scapy_demo.py", "cd", "pwd", and "clear" are Windows/PowerShell commands, NOT Scapy commands.
- To leave Scapy and return to Command Prompt, type:
      exit()
  or press Ctrl+Z and Enter.

HOW TO RUN A FILE
-----------------
1. Exit the Scapy shell:
      exit()

2. In Command Prompt, go to this folder, for example:
      cd C:\Users\anike\Downloads\scapy_demo_kit

3. Run a script:
      python 01_basic_layers.py

RECOMMENDED LIVE DEMO
---------------------
1. 01_basic_layers.py       -> show packet layers
2. 02_packet_fields.py      -> modify/inspect fields
3. 03_icmp_ping.py          -> send ICMP and receive response
4. Wireshark                 -> filter with: icmp
5. 04_sniff_icmp.py         -> capture ICMP packets
6. 07_hex_dump.py           -> show raw bytes

QUICK MENTAL MODEL
------------------
show()/show2()   = inspect a packet
/               = stack protocol layers
sr1()            = send and receive one response
sniff()          = capture packets
nsummary()       = summarize captured packets
hexdump()        = show raw packet bytes
wrpcap()         = save packets as PCAP
rdpcap()         = read a PCAP

SAFETY
------
Use packet transmission only on systems/networks you are authorized to test.
The demo kit intentionally avoids Wi-Fi deauthentication, beacon flooding,
ARP spoofing, credential capture, and other disruptive demonstrations.

WIRESHARK
---------
Start a capture on your active Wi-Fi/Ethernet interface.
Useful display filters:
    icmp
    tcp
    udp
    dns
    arp

If sniffing fails on Windows:
- Run Command Prompt as Administrator.
- Make sure Npcap is installed.
- Check the interface with 08_interfaces.py.
