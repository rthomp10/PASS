#!/usr/bin/python3

# Zachary Rangel, Pedestrian Acknowledgment Smart System

import socket as socket
import time

BUFFER_SIZE = 1024

# Receiver setup (udp)
UDP_IP = '192.168.1.2' # this is a DESTINATION IP
UDP_PORT = 5005 # this must match receiver info
udp_message = 'Pedestrian Detected'


# Recognition unit setup (tcp)
TCP_IP = '192.168.1.1' # The IP address of this computer = the  interfaces file on this machine
TCP_PORT = 9999 # recognition unit port #
return_message = 'Hand has been shook'

# Creates the TCP socket object
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds tcp socket to the port
tcp_server.bind((TCP_IP, TCP_PORT))

# Max qeue of 5 requests
tcp_server.listen(5)

print('UDP Pack Sent\n Info\n')
print('\tDestination Pack: ', UDP_IP)
print('\tDestination Port: ', UDP_PORT)
print('Packet contents: ', udp_message)

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True: 
    client_socket, addr = tcp_server.accept()
    print("Pedestrian flag received %s" % str(addr))
    client_socket.send(return_message.encode('ascii'))
    client_socket.close()
    #transmit_start = time.time()
    #while time.time()-transmit_start < 5: 
    udp_server.sendto(udp_message.encode('UTF-8'), (UDP_IP, UDP_PORT))

