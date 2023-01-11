
#Thanks To TheyAreNot666#9377
#Built By Little Developer

import os
import time
from colorama import Fore

def Home():
    os.system("cls")
print(f''' {Fore.MAGENTA}

██╗   ██╗██╗   ██╗    ██╗  ██╗██╗   ██╗██╗     ██╗     ███████╗██████╗ 
██║   ██║╚██╗ ██╔╝    ██║ ██╔╝╚██╗ ██╔╝██║     ██║     ██╔════╝██╔══██╗
██║   ██║ ╚████╔╝     █████╔╝  ╚████╔╝ ██║     ██║     █████╗  ██████╔╝
╚██╗ ██╔╝  ╚██╔╝      ██╔═██╗   ╚██╔╝  ██║     ██║     ██╔══╝  ██╔══██╗
 ╚████╔╝    ██║       ██║  ██╗   ██║   ███████╗███████╗███████╗██║  ██║
  ╚═══╝     ╚═╝       ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

{Fore.YELLOW}[!] Note if Veyon is already Killed the tool don't work
                                                                       
''')

input(f"{Fore.CYAN}Type Yes for start:  ")

time.sleep(0.6)
print(f"{Fore.YELLOW}[!] SYSTEM: Searching Veyon On PC (Server)")
time.sleep(0.9)
print(f"{Fore.CYAN}[!] Please Wait 5 Seconds")
time.sleep(4.5)
print(f"{Fore.GREEN}[!] SYSTEM: Found Veyon!")
time.sleep(2)
print(f"{Fore.BLUE}[!] SYSTEM: Closing Veyon (exe & server)")
time.sleep(3)
os.system("taskkill /im Veyon /f")
os.system("taskkill /im Veyon_Server /f")
os.system("taskkill /im Veyon_Service")
print(f"{Fore.LIGHTGREEN_EX}[!] SYSTEM: Closed Succesfully!")
time.sleep(2)
Home()