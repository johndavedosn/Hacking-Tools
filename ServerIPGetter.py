import socket
URL = input("URL --> ")
try:
    IPAddr = socket.gethostbyname(URL)
except socket.gaierror:
    print("Server Not Found...")
    
