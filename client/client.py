'''
client script for stablishing a communication to a server
'''
from socket import socket

# Creating constans: Server Ip address and the port number used
SERVER_ADDR = ("localhost", 5550)


sock = socket()
sock.connect(SERVER_ADDR)
word = "Hola"
sock.send(word.encode())
new_word = sock.recv(2048).decode()
print(f"From Server : {new_word}")
sock.close()
