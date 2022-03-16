import socket
import pickle
from threading import Thread
import time
import champlistloader
#import pandas as pd
# Server Data Base


TCP_IP = 'localhost'  # local host
TCP_PORT = 8500  # port number of the client-server
BUFFER_SIZE = 2048


data = champlistloader.load_some_champs()
databaseServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
databaseServer.bind((TCP_IP, TCP_PORT))
databaseServer.listen()

conn, adr = databaseServer.accept()

conn.send(pickle.dumps(data))

while True:
    match_results = conn.recv(BUFFER_SIZE).decode()
    if match_results != "":
        file = open("match_data", "a+")
        file.writelines(match_results)
        break
conn.close()


