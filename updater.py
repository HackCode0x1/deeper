import sys
from urllib.request import urlopen
from os import system as cmd
import platform
from time import sleep
import threading

System = platform.platform().split("-")[0]

loading = True 
loading_speed = 4  
loading_string = "." * 4

def Sp_Dots(text,stop):
	
	print(text,end="")
	while 1:
	    for index, char in enumerate(loading_string):
	        sys.stdout.write(char) 
	        sys.stdout.flush()  
	        sleep(1.0 / loading_speed)  
	    index += 1  
	    sys.stdout.write("\b" * index + " " * index + "\b" * index)
	    sys.stdout.flush()  # flush the output
	    if stop():
	    	break
 


	
def clear():
	if System=='Windows':
		cmd('cls')
	else:
		cmd('clear')



def updater():
	clear()
	stop_threads = False
	t1 = threading.Thread(target = Sp_Dots, args =('[*] Cheking For Updates',lambda : stop_threads, )) 
	t1.start() 
	sleep(2)

	
	Counter = '0'
	Crunt_Version = '3.0.0'
	try:
		Get_Version = urlopen('https://raw.githubusercontent.com/NoOAYe/deeper/main/Data/version.txt').read().decode('utf-8').strip()
		version	 = Get_Version[0:5]
		count = Get_Version[-1]
		


	except:
		print()
		print("[-] Can't reach Internet !!!")
		sys.exit(0)
	print()
	stop_threads = True
	t1.join() 

	if version != Crunt_Version:
		print("[+] New Version Is Available!")
		sleep(2)
		if System=='Linux':
			try:
				cmd('git clone https://github.com/NoOAYe/deeper')
			except:
				pass


	elif count != Counter	:
		print("[*] New Update Is Available!")
		sleep(2)
		if System=='Linux':
			try:
				cmd('git clone https://github.com/NoOAYe/deeper')
			except:
				pass

	else:
		print('[*] No Updates Found')






updater()