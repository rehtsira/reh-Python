#send message to a connecting client
#made to run simultaneously with client.py

import socket

host = socket.gethostname()
port = 2020

#create an INET, STREAMing socket
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.bind((host,port))

#Queue up one connection request before refusing outside connections
sock_.listen(1)

print("\nServer started...\n")

conn,addr= sock_.accept()

print("Connection established with:",str(addr))

message = "\nHello, friend... " + str(addr) + "\nIt's an exciting time in the world."
conn.send(message.encode("ascii"))
print("Message Sent: " + message)
conn.close()
