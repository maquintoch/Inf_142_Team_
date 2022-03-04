'''
client script for stablishing a communication to a server
'''
from socket import socket

# Creating constans: Server Ip address and the port number used
SERVER_ADDR = "localhost"
PORT = 5550

sock = socket()
sock.connect(SERVER_ADDR, PORT)
