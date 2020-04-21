#!/usr/bin/python3
import socket

IP = "127.0.0.1" # ip 
PORT = 1234		#port number 

x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet and the UDP
x.bind((IP, PORT))
while True:			#runs while true 
    data, addr = x.recvfrom(1024)  # buffer
    print("received message:" + data.decode()) 
    ret = "recieved"						#returns a recieved
    x.sendto(ret.encode(), addr)
    print('done')								# finished
