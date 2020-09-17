#!/usr/bin/python
import requests,os
from colorama import Fore
if os.name=='nt':
 #WINDOWS
 os.system('cls')
 os.system("title [Bin checker] By Nayfer")
else:
 #LINUX
 os.system('clear')
print(f'''{Fore.BLUE}
  __  _          ___ _               _             
 |  _ \(_)        / ____| |             | |            
 | |_) |_ _ _   | |    | |_   _  __| | ____ _ __ 
 |  _ <| | '_ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |_) | | | | | | |____| | | |  __/ (__|   <  __/ |   
 |____/|_|_| |_|  \_____|_| |_|\___|\___|_|\_\___|_|                                                                                                       
                    github.com/cha-afk {Fore.RESET}''')
bin = str(input('Your bin or cc = '))
if not(len(bin)<=6):
 Rbin=""
 for i in range(0,6):
  Rbin=Rbin+bin[i]
else:
 Rbin=bin
response=requests.get('https://lookup.binlist.net/'+str(Rbin)).json()
scheme=response['scheme']
typ=response['type']
country=response['country']['name']
bank=response['bank']['name']
print('Bin info : \nscheme : {a} \ntype : {b} \nCountry : {c} \nBank : {d}'.format(a=scheme,b=typ,c=country,d=bank))
