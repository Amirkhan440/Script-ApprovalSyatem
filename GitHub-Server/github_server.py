#!/usr/bin/python3
import os
try:
	import requests
except ImportError:
	print('\n[->] Installing Module Requests ')
	os.system('pip install requests')
banner = " "
def logo():
	os.system("clear")
	print(banner)
	
import datetime
import random
import requests 
import re
import json
import sys
import platform
import time 
import uuid
id1 = uuid.uuid4().hex[:7].upper()
id2 = uuid.uuid4().hex[:7].upper()
id3 = uuid.uuid4().hex[:7].upper()

id4 = uuid.uuid4().hex[:1].upper()
id5 = uuid.uuid4().hex[:1].upper()
id6 = uuid.uuid4().hex[:1].upper()
id7 = uuid.uuid4().hex[:1].upper()
id8 = uuid.uuid4().hex[:1].upper()
id9 = uuid.uuid4().hex[:1].upper()


key1 = id1 + '-' +id2 + '-' + id3
key2 = id4 + '-' + id5 + '-' + id6 + '-' + id7 + '_' + id8 + '-' + id9
key3 = uuid.uuid4().hex[:25].upper()
key4 = uuid.uuid4().hex[:25].lower()

my_key = key1

try:
	key_chack = open('/data/data/com.termux/files/usr/.key.txt', 'r').read()
except:
	save = open('/data/data/com.termux/files/usr/.key.txt', 'w')
	save.write(my_key)
	save.close()

try:
	user_key = open('/data/data/com.termux/files/usr/.key.txt', 'r').read()
	approvedkey = requests.get('https://raw.githubusercontent.com/BilalHaiderID/Script-ApprovalSyatem/main/GitHub-Server/Server.txt').text
	if user_key in approvedkey:
		logo()
		print("    Congratulation, Your Key Is Approved ")
		pass
	else:
		logo()
		print("        Sorry Sir !  Your Key Is Not Approved ")
		print("\n[->] Your Key : " + user_key )
		print("")
		print("[->] Copy Your Key And Send To Owner ")
		input("[>>] Press Enter  ")
		os.system("xdg-open https://www.facebook.com/")
		time.sleep(2)
		exit()
except IOError:
	print("\n\n[×] Chack Your Internet Connection ")
	exit()
    

