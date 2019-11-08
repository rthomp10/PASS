#!/usr/bin/python3

import socket as socket
import RPi.GPIO as GPIO
import time
import threading

# Timer setup
def reaction():
    global stop_threads
    for i in range(50):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
        if stop_threads:
            break

timer = threading.Thread(target=reaction)


# UDP receive setup
UDP_IP = '192.168.1.2'
UDP_PORT = 5005
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.bind((UDP_IP, UDP_PORT))

# LED setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

while True:
    data, addr = udp_client.recvfrom(1024)
    print("received message: " + data.decode('ascii'))
    stop_threads = True
    time.sleep(0.5)
    stop_threads = False

