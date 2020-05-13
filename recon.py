#checks headers, IP information, location, region, city, and country when given a URL

import sys
import requests
import socket
import json

#if URL is not specified, print usage and exit
if len(sys.argv)<2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

#sends a request to URL specified and print headers
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#retrieves the IP address of a host using socket module
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

#retrieve geographic information of the IP address using ipinfo.io
req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)

print("Location: " + resp_["loc"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"])
print("Country: " + resp_["country"])
print("Organization: " + resp_["org"])
print("Host Name: " + resp_["hostname"])
