import pyfiglet
import socket
import subprocess
import sys
from datetime import datetime

#Shows the banner and clear shell
subprocess.call('clear', shell=True)
ascii_banner = pyfiglet.figlet_format("LOCALHOST SCANNER")
print(ascii_banner)

#Shows more banner detais
t1 = datetime.now()  
print("-" * 50)
print("Scanning Localhost")
print("Scanning started at:" , t1)
print("-" * 50)

try:     
# will scan hosts between 1 to n
    for ping in range(1,15):
        address = "127.0.0." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            print( "ping to", address, "OK")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")

#Exceptions
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
t2 = datetime.now()   
total = t2 - t1
print ('Scanning Completed in: ', total)