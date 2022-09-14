import scapy.all as scapy
import optparse

#1- arp request
#2- broadcast
#3- response

def input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest = "ip", help="ip range")
    (user_input, arguments) =  parse_object.parse_args()
    if not user_input.ip:
        print("Enter IP address")

    return user_input

def scanner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether("ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_input = input()
scanner(user_input.ip)