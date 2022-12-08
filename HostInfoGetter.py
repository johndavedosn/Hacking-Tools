from tkinter import *
import sys
import socket
from requests import get
root = Tk()
root.geometry("400x200")
root.title("Host Info Getter")
HostName = socket.gethostname()
IPAddr = socket.gethostbyname(HostName)
Platform = sys.platform
Public_IPAdrr  = get('https://api.ipify.org').text
Text1 = Label(root, text="Your Host Name : " + str(HostName))
Text2 = Label(root, text="Your IP Address : " + str(IPAddr))
Text3 = Label(root, text="Your Platform : " + str(Platform))
Text4 = Label(root, text="Your Public IP Address : "   + str(Public_IPAdrr))
Text1.pack()
Text2.pack()
Text3.pack()
Text4.pack()
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Interputed...")