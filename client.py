'''
client script for stablishing a communication to a server
'''
from socket import socket
from rich import print
from rich.prompt import Prompt
from rich.table import Table

from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
import json

# Creating constants: Server Ip address and the port number used
SERVER_ADDR = ("localhost", 5550)


sock = socket()
sock.connect(SERVER_ADDR)
word = "Hola"
sock.send(word.encode())
#new_word = sock.recv(2048).decode()
ListOfChampions = sock.recv(2048*2).decode()
#ListOfChampions = json.loads(ListOfChampions)
print(f"From Server : {ListOfChampions}")
sock.close()
