import socket
from core import Match
import json
import team_local
import time
import pickle
from playerPrint import *

TCP_IP = '127.0.0.1'  # local host
TCP_PORT = 8000  # port number of the client
BUFFER_SIZE = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((TCP_IP, TCP_PORT))
    champions = pickle.loads(s.recv(BUFFER_SIZE * 2))
    print_available_champs(champions)
    while True:
        from_serverI = s.recv(BUFFER_SIZE * 2)
        try:
            from_server = from_serverI.decode()
        except:
            match = pickle.loads(from_serverI)
            print_match_summary(match)
        print("From server", from_server)
        if from_server == "Choose":
            print_available_champs(champions)
            print("Choose a champion player")
            valg = input("Player=>")
            s.send(valg.encode())
        elif from_server == "Correct":
            continue
        else:
            break
