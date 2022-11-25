import socket
import time
import sys
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Device Name is : " + hostname)
print("Your Device IP Address is: " + IPAddr)
print("Your Device Platform is : " + sys.platform) 
time.sleep(5)