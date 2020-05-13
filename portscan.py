#checks port 21,22,80,443,8080 on a given URL

import nmap
import sys
import socket

target = str(sys.argv[1])
ports = [21,22,80,443,8080]

scan_v = nmap.PortScanner()

ip = socket.gethostbyname(sys.argv[1]) 

print("\nScanning",target,"for ports" + str(ports[0:]))

for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port," is ",portscan['scan'][ip]['tcp'][port]['state'])

print("\nHost",target," is ",portscan['scan'][ip]['status']['state'])

print("\nTarget's IPv4 address: " + portscan['scan'][ip]['addresses']['ipv4'])
