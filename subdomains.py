import requests
import sys

#https://github.com/rbsec/dnscan/blob/master/subdomains-1000.txt
sub_list =open("subdomains-1000.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    url_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_check)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ",url_check)


#USAGE: python3 subdomains.py <url>
#example: python3 subdomains.py google.com