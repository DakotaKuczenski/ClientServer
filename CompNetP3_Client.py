#!/usr/bin/python3
import socket

IP = "127.0.0.1" #ip change to yours
PORT = 1234 #port
MESSAGE = "GTO457 Dakota Kuczenski" #message to send

print("UDP IP: " + IP + '\n' + "UDP port: " + str(PORT) + '\n' + "message: " + MESSAGE) #formatting 

x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet & UDP
x.sendto(MESSAGE.encode(), (IP, PORT))      #send to the corrent ip and port
print("received: " + x.recv(1024).decode())

