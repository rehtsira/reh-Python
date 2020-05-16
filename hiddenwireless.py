from scapy.all import *
import os

#wireless interface must be able to run in monitor mode
iface = "your-wireless-interface-here"

def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssoReq):
        print("SSID identified " + packet.info)

os.system("iwconfig " + iface + " mode monitor")

print("Sniffing traffic on interface " + iface)
sniff(iface=iface, prn=h_packet)
