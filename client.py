#receive message from an established server via socket module
#made to run simultaneously with server.py

import socket

#create an INET, STREAMing socket
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect to local machine on port 2020
sock_.connect((socket.gethostname(),2020))
#receive 1024 bytes
msg = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))
