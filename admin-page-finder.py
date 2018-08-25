#!/usr/bin/env python

import os
import time

from urllib2 import Request, urlopen, URLError, HTTPError

def welcome():
	os.system("clear")
	print """\033[1m
     _       _           _         _____ _           _
    / \   __| |_ __ ___ (_)_ __   |  ___(_)_ __   __| | ___ _ __
   / _ \ / _` | '_ ` _ \| | '_ \  | |_  | | '_ \ / _` |/ _ \ '__|
  / ___ \ (_| | | | | | | | | | | |  _| | | | | | (_| |  __/ |
 /_/   \_\__,_|_| |_| |_|_|_| |_| |_|   |_|_| |_|\__,_|\___|_|
"""

def find_admin():
	global time
	CRED = '\033[91m'
	CGREEN = '\33[32m'
	CWHITE = '\33[37m'
	CBOLD = '\33[1m'
	CYELLOW2 = '\33[93m'
	number_admin_page = 0
	all_admin_page = 0
	cnt = 0
	valid_admin_page = []
	admin_list = open("admin-page-list.txt","r");
	print(CRED + "\n[!] Press [CTRL + Z] To Stop While Scanning!\n")
	link = raw_input(CWHITE + "Enter Site Name (ex : example.com or www.example.com ): ")
	print("\nAvilable Links : \n")
	starttime = time.time();
	while True:
		sub_link = admin_list.readline()
		if not sub_link:
			break
		all_admin_page += 1
		req_link = "http://" + link + "/" + sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			print(CRED + "[-] " + req_link)
			continue
		except URLError as e:
			print(CRED + "[-] " + req_link)
			continue
		else:
			print(CGREEN + "[+] " + req_link)
			valid_admin_page.append(req_link)
			cnt += 1
			number_admin_page += 1
	print CBOLD + CYELLOW2 + "\n[:)] Scan Finished Successfully!"
	if number_admin_page > 0:
		time.sleep(2)
	print "\n" + CWHITE + "[=]" , number_admin_page , "Admin Page Found From" , all_admin_page , "URLs Scanned!\n"
	i = 0
	while i < cnt:
		print CGREEN + "[+] " + valid_admin_page[i]
		i += 1
		time.sleep(0.1)
	print CWHITE + "[=] Time Elapsed : %.2f seconds" % float(time.time() - starttime) + "\n"

welcome()

find_admin()
