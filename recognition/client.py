#!/usr/bin/python3

import socket

# get local machine name
broadcast_ip = '192.168.1.1'
port = 9999


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hostname on the port.
s.connect((broadcast_ip, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()
print (msg.decode('ascii'))
