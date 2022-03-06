'''
Server script 
'''
from encodings import utf_8
import os
from selectors import DefaultSelector, EVENT_READ
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
from team_local import print_available_champs
import json


def accept(sock):
    conn, address = sock.accept()  # Should be ready
    print('Accepted', conn, 'from', address)
    conn.setblocking(False)
    sel.register(conn, EVENT_READ)


def read(conn):

    data = conn.recv(2048*2)  # Should be ready
    if data:
        word = data.decode()
        #new_word = word.upper()

        champions = load_some_champs()
        #ListOfChampions = print_available_champs(champions)
        #ListOfChampions = json.dumps(ListOfChampions)
        #ListOfChampions = json.dumps(ListOfChampions)
        # conn.send(ListOfChampions.encode())
        # conn.sendall(bytes(ListOfChampions.encode()))
        conn.send("Holade vuelta".encode())
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sel = DefaultSelector()
sock = socket()
# Reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("localhost", 5550))
sock.listen()
sock.setblocking(False)
sel.register(sock, EVENT_READ, True)

while True:
    events = sel.select()
    for key, _ in events:
        if key.data:
            accept(key.fileobj)
        else:
            read(key.fileobj)
