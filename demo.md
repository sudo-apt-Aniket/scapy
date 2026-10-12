Aniket, let's make this your Scapy classroom demo sheet: 10 commands, copy-paste ready, with a simple explanation of what each does and exactly what you can say to your teacher. You won't need to memorise code.

The demo will cover packet construction, protocol layers, packet testing, sniffing, filtering, and Wireshark integration. That gives you a good mix of practical work without making the presentation unnecessarily complicated.

# Scapy Network Security Demo Sheet

## Introduction to say before starting

Good morning, sir. Today, I am going to demonstrate Scapy, a Python-based network packet manipulation and analysis tool.

Scapy allows us to construct network packets, inspect their protocol layers, send and receive packets, and capture network traffic. Unlike Wireshark, which primarily provides a graphical interface for analysing packets, Scapy allows us to perform these operations programmatically using Python.

For this demonstration, I will show how packets are constructed, how different protocol layers are combined, how ICMP communication works, and how network traffic can be captured and analysed using Scapy and Wireshark.

## Before you begin

You already have Scapy installed. Open Command Prompt, not the Scapy interactive shell.

If your screen shows `>>>`, type:

```
exit()
```

Once you see a Windows prompt such as `C:\Users\anike>`, navigate to the folder containing your demo files, if applicable.

You can run the following commands individually in the Scapy shell, or use the equivalent standalone Python files where provided. For the interactive commands below, first enter Scapy using:

```
python -m scapy
```

Wait for the `>>>` prompt before pasting the Scapy commands.

## The 10 commands for your live demo

### 1. Inspect an IP packet

Command 1 — Packet inspection

Begin here

```
IP().show()
```

What it does: Creates an IPv4 packet object and displays its fields, such as TTL, source address and destination address.

Say this:

“First, I am using Scapy to create and inspect an IP packet. We can see that a packet contains several fields, and Scapy allows us to examine them individually rather than treating the packet as a black box.”

### 2. Construct a packet with multiple layers

Command 2 — Packet construction

```
packet = Ether()/IP(dst="8.8.8.8")/ICMP()packet.show()
```

What it does: Builds a packet containing Ethernet, IPv4 and ICMP layers. The `/` operator stacks the layers together.

Say this:

“Here, I am combining three protocol layers. Ethernet handles local network framing, IP handles addressing and routing, and ICMP is used for network control messages such as ping. Notice how Scapy allows us to construct the packet using a simple expression.”

### 3. Inspect specific packet fields

Command 3 — Field analysis

```
packet[IP].dstpacket[IP].ttlpacket.show2()
```

What it does: Reads the destination IP and TTL fields, then displays the packet with fields that can be calculated during packet construction.

Say this:

“Scapy also allows us to access individual fields directly. The destination identifies the intended IP address, while TTL, or Time to Live, limits how many router hops a packet can traverse before being discarded. The show2 method calculates fields that can be derived when the packet is built.”

### 4. Send a packet and receive a response

Command 4 — ICMP testing

```
response = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=3, verbose=0)print(response.summary() if response else "No response received")
```

What it does: Sends an ICMP echo request and waits up to three seconds for one matching response.

Say this:

“Now I am using Scapy to send an ICMP echo request to a public DNS server. The sr1 function sends a packet and waits for one response. If a reply arrives, I can inspect it. If no reply arrives, it could be due to network restrictions or the destination not responding.”

Note: Run Command Prompt as Administrator if required by your Windows/Npcap setup. Test this command before the lecture because public ICMP responses are not guaranteed.

### 5. Capture ICMP traffic

Command 5 — Packet sniffing

```
packets = sniff(filter="icmp", count=5)
```

What it does: Captures five ICMP packets visible to Scapy on the selected interface. It waits until five matching packets are captured.

Say this:

“So far, we have constructed and sent packets. Scapy can also passively capture network traffic. Here, I am filtering for ICMP so that we can focus on ping-related communication rather than unrelated background traffic.”

Before running this, start the capture and then generate traffic by running `ping 8.8.8.8` in a separate Windows Command Prompt. Packet capture on Windows may require Administrator privileges and a working Npcap installation.

### 6. Display captured packet summaries

Command 6 — Analyse captured traffic

```
packets.nsummary()
```

What it does: Prints a compact summary of each captured packet, making the results easier to read.

Say this:

“After capturing the packets, I can summarise them to understand what was observed. This is useful when analysing multiple packets because I can review the traffic without displaying every field of every packet.”

### 7. Construct a DNS query

Command 7 — DNS packet construction

```
dns_packet = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com"))dns_packet.show()
```

What it does: Constructs a DNS query for `example.com` using UDP destination port 53. It only builds and displays the packet; it does not send it.

Say this:

“Scapy is not limited to ICMP. Here, I am constructing a DNS query using IP, UDP and DNS layers. This demonstrates how the same layer-stacking technique can be used to examine different network protocols.”

### 8. Display the raw hexadecimal bytes

Command 8 — Hexadecimal analysis

```
hexdump(packet)
```

What it does: Displays the packet's raw byte representation in hexadecimal form.

Say this:

“Until now, we have been looking at decoded protocol fields. Scapy can also display the raw bytes that make up a packet. This is useful for low-level protocol analysis and understanding how packet data is represented.”

This uses the `packet` variable created in Command 2.

### 9. Save a packet for Wireshark

Command 9 — PCAP export

```
wrpcap("scapy_demo.pcap", [packet])
```

What it does: Saves the constructed packet to a PCAP file that Wireshark can open.

Say this:

“Scapy supports exporting packets in PCAP format. This makes it possible to move from programmatic packet construction to graphical analysis in Wireshark. The saved packet is a constructed example, not proof that it was transmitted over the network.”

### 10. Read a PCAP file back into Scapy

Command 10 — Read saved traffic

```
captured = rdpcap("scapy_demo.pcap")captured.nsummary()
```

What it does: Reads the saved PCAP file and displays a summary of the packets it contains.

Say this:

“Finally, Scapy can read previously saved packet captures. This is useful for offline analysis because we can inspect packet data after a capture has finished, without having to generate the traffic again.”

## How to run the demo smoothly

Use two windows during the presentation:

Window 1: Scapy

Run `python -m scapy` from Windows Command Prompt, then paste Commands 1–4, 7–10 at the `>>>` prompt. Run Command 5 separately when you are ready to demonstrate sniffing.

Window 2: Wireshark / Command Prompt

Use Wireshark to capture live traffic with the display filter `icmp`. Use a second Windows Command Prompt to generate ping traffic while Scapy is sniffing.

Important: Commands 5 and 6 belong together, as do Commands 9 and 10. Commands 1–4 and 7–9 are otherwise independent, provided their referenced variables exist in your current Scapy session.

## Conclusion to say

To conclude, Scapy is a flexible tool for network security because it allows us to construct packets, inspect protocol fields, send and receive traffic, and capture packets for analysis. Its ability to export and import PCAP files also makes it useful alongside Wireshark. Through this demonstration, we can see how Scapy helps us understand network communication at the packet level and supports network troubleshooting, protocol analysis and authorised security testing. Thank you.

My recommendation: practise Commands 1, 2, 4, 5, 6 and 9 first. Those give you the strongest practical demonstration. Keep the remaining commands as additional examples if your teacher asks you to show more Scapy functionality.