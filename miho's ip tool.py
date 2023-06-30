import pyfiglet
import colorama
from colorama import Fore, Back, Style
from tkinter import N
import geocoder
import os

from time import sleep
from progressbar import progressbar

import socket
import re






colorama.init(autoreset= True)
ascii_banner = pyfiglet.figlet_format(  "IP tool")
print(ascii_banner)
print (Fore.BLUE + "Code and design by M.Mzhavia")
print (Fore.GREEN + ''' 
   Hello friend it seems you want to use IP TOOL that i created, so here are some instructions for you
1. Make sure that IP adress is valid 
2. When you see input - enter port range, enter there range of ports that you want to scan (Max: 60000)
EXAMPLE:
  Enter port range: 60-120
''')
print ( Fore.RED  + '''                                                                                                                                       
   WARNING!!! 
This tool was created for educational purposes only! Do not use it to hack  
anyone without there permision                    
''')


IP = input ('IP:')

ip = geocoder.ip(IP)
print ("Getting IP info")


    
    





print (ip.city)
print (ip.latlng)
print ("IP location ^^^^^")
#You get ip location.



ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535




open_ports = []
while True:
    ip_add_entered = IP
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           
            s.settimeout(0.5)
           
            s.connect((ip_add_entered, port))
            
            open_ports.append(port)

    except:
        
        pass


for port in open_ports:
   
    print(f"Port {port} is open on {ip_add_entered}.")


answer = input("Do you want to save results? (Y/N): ")

match answer:
    case "Y" :
 
     cit = str (ip.city)
     coo = str (ip.latlng)
     por = str (port)

     file = open ('IPinfo.txt', 'w')

     file.write ("Taget ip: " + IP )
     file.write ("\nlocation: " + cit )
     file.write ("\ncoordinates: " + coo )
     file.write (" \n |")
     file.write ("\nPort range: " + port_range )  
     file.write ("\nOpen ports " + por)
     file.close()
    
    case "N":
        print("OK")


