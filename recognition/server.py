import socket  
import time

# get local machine name and decide max time
host = '192.168.1.3'
port = 9999
timer = 8 # coutdown starts here


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                      

# bind to the port
serversocket.bind((host, port))                               

# queue up to 5 requests
serversocket.listen(5)                                           

# Statistics setup
# f = open("latency.txt", "w+")
# f.write("Maximum Detection Latency w/ Live Feed\r\n")
try:
	while True:
	    # establish a connection and halts all other processes
	    start = time.time()
	    clientsocket,addr = serversocket.accept()
	    # print("Pedestrian flag received %s" % str(addr))
	    end = time.time()
	    # f.write("%f\r\n" % (end-start))

	    msg = 'Return hand shake recieved'+ "\r\n"
	    clientsocket.send(msg.encode('ascii'))
	    clientsocket.close()
except KeyboardInterrupt:
	# f.close()
	pass
