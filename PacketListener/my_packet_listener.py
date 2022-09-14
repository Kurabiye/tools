import scapy.all as scapy
from scapy_http import http

print("Starting...")

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_packets)

def analyze_packets(packet):
    # packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
sniffing("eth0")