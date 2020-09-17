import urllib.request, colorama, os, ctypes
from colorama import Fore

os.system('cls')
os.system("title [Bin checker] By Nayfer")



print(f'''{Fore.BLUE}
  ____  _          _____ _               _             
 |  _ \(_)        / ____| |             | |            
 | |_) |_ _ __   | |    | |__   ___  ___| | _____ _ __ 
 |  _ <| | '_ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |_) | | | | | | |____| | | |  __/ (__|   <  __/ |   
 |____/|_|_| |_|  \_____|_| |_|\___|\___|_|\_\___|_|                                                                                                       
                    github.com/cha-afk {Fore.RESET}''')
headers = {
    'Accept-Version': '3',
}

bin = input('Your bin = ')
a = urllib.request.urlretrieve(f'https://lookup.binlist.net/'+bin, f'Bin.txt',)
print(f'{Fore.BLUE}> {Fore.RESET}Successfully Grabbed Bin infos')
input()
exit()