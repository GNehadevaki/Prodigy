from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def analyze_packet(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet:")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        # Check for specific protocols and extract relevant information
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print(f"Flags: {tcp_layer.flags}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"Type: {icmp_layer.type}")
            print(f"Code: {icmp_layer.code}")

def start_sniffing(interface=None):
    print("Starting packet capture...")
    sniff(iface=interface, filter="ip", prn=analyze_packet)

if _name_ == "_main_":
    # Interface can be specified if needed, e.g., "eth0", "wlan0", etc.
    interface = input("Enter the interface to sniff on (leave blank for default): ")
    start_sniffing(interface if interface else None)