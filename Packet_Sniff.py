import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        print(f"Packet: {src_ip} --> {dst_ip} Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            data = packet[scapy.Raw].load
            print(f"Raw Data: {data.hex()}")

# Usage example
if __name__ == "__main__":
    interface = input("Enter the interface to sniff on (e.g., eth0): ")
    sniff_packets(interface)
