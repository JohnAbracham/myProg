#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
	(options, arguments) = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	answered = scapy.srp(broadcast/arp_request, timeout=1, verbose=False)[0]

	client_list = []
	for element in answered:
		client_dict = {"ip":element[1].psrc, "mac": element[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_result(result_list):
	print("IP\t\t\tMAC Address\n-------------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
