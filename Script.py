from socket import *
from requests import get
import sys
Hostname = gethostname()
ip = get('https://api.ipify.org').text
IPAddr = gethostbyname(Hostname)
PLatform = sys.platform
Data = {
    "Public IP": ip,
    "Private IP": IPAddr,
    "Platform": PLatform
}
