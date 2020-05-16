#lsc() - look at scapy commands
pack_ = IP(dst="github.com",ttl=10)
pack_.show()
conf.color_theme=ColorOnBlackTheme()
#--Windows--
sniffer_ = sniff(iface="your-wifi-adapter-here", count=15) #count is for how many packets
sniffer_[5].load #shows in hex
hexdump(sniffer_[5])

sniffer = sniff(filter="port 443 and host 140.82.113.3", count=15,prn=lambda x:x.summary())
wrpcap("git.cap",sniffer)
rdpcap("git.cap")

read_cap = rdpcap("git.cap")
read_cap[5]

packet_t = IP(dst="github.com")/ICMP()/"You are not secured"
sr(packet_t)
resp - sr(packet_t)
res[0].summary()
