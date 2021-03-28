#!/usr/bin/env python

# libraries
import pyfiglet 
import terminal_banner  as tb
import subprocess as sub
import socket
import sys
from datetime import datetime 



#clear terminal
sub.call('clear',shell=True)

#-----------------------TOOL HEADER------------------------------
print(pyfiglet.figlet_format('H3yScan',font='banner3-D'))

#-----------------------BANNER------------------------------
banner = " {Description}: A simple port scanner for detecting open ports on a host.  \n Disclaimer :!!! This tool is to be used for educational purposes only,the author will take no responsibility if its put to other use.!!!  \n Author: h£¥N3t \n Version: 1.0.0 \n Email: heynet101@hotmail.com"
banner_new = tb.Banner(banner)
print (banner_new)







#------------------------------------SCANNING FUNCTION-----------------------------------

def scanner(ip):

	# Inform the user that scan has started 

	print(pyfiglet.figlet_format('HAPPY SCANNING HOST {}'.format(ip),font='digital'))
	


	try:
		for i in range(1,30):    #Make port dynamic
			ip_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			sock_result = ip_sock.connect_ex((ip,i))
			#print ('scanning port {}'.format(i))

			if sock_result == 0:
				print("Port {} is open".format(i))

			ip_sock.close()



	except KeyboardInterrupt:
		print ("Program exited")
		sys.exit()
			
	except socket.error:
		print("Sorry could not reach host {}".format(ip))
		sys.exit()

	





while True:

	try :
	
		# Ask user for IP or Domain

		ip_or_domain = input("Enter  1 for ip or 2 for Domain:")


		# for IP option
		if ip_or_domain == '1':
			ip = input("Enter IP address:")   #Check if string is valid ip
			scanner(ip)
			

		elif ip_or_domain =='2':
			domain = input("Enter domain address: ") 

			try:
				ip = socket.gethostbyname(domain)    #Check if domain resolved properly to ip
				print (ip)
				scanner(ip)

			except socket.gaierror:
				print("Sorry hostname could not be resolved")

			
			


		else:
			print("Wrong input {}".format(ip_or_domain))

	except KeyboardInterrupt:
		print("Program exited")
		sys.exit()
			







