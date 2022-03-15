from asyncio import events
import socket
import pickle
from threading import Thread
from team_local import *
import pandas as pd
import selectors
import time

TCP_IP = '127.0.0.1'  # local host
TCP_PORT = 8000  # port number of the client
TCP_IP_DATABASE = 'localhost'
TCP_IP_DATABASE_PORT = 8500

BUFFER_SIZE = 2048


players = []
number_of_players = 2
# Receiving the clients that will be connected to the server.


database = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
database.connect((TCP_IP_DATABASE, TCP_IP_DATABASE_PORT))
some_champs = database.recv(BUFFER_SIZE)

champions = pickle.loads(some_champs)

player1 = []
player2 = []

players = []

sel = selectors.DefaultSelector()
Tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Tsock.bind((TCP_IP, TCP_PORT))
Tsock.listen()
# Tsock.setblocking(False)
sel.register(Tsock, selectors.EVENT_READ, True)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data:
            conn, adr = key.fileobj.accept()
            players.append(conn)
        else:
            continue
    if len(players) == 2:
        break

players[0].send(pickle.dumps(champions))
players[1].send(pickle.dumps(champions))

id_counter = 0
for i in range(2):
    while True:
        print("Sender til player 1")

        players[0].send(b"Choose")
        match players[0].recv(BUFFER_SIZE * 2).decode():
            case name if name not in champions:
                print(name)
                players[0].send(b"Choose")
                continue
            case name if name in player1:
                players[0].send(b"Choose")
                continue
            case name if name in player2:
                players[0].send(b"Choose")
                continue
            case _:
                print("It was correct")
                player1.append(name)
                players[0].send(b"Correct")
                break
    print("")
    while True:
        print("Sender til player 2")
        players[1].send(b"Choose")
        match players[1].recv(BUFFER_SIZE * 2).decode():
            case name if name not in champions:
                players[1].send(b"Choose")
                continue
            case name if name in player1:
                players[1].send(b"Choose")
                continue
            case name if name in player2:
                players[1].send(b"Choose")
                continue
            case _:
                player2.append(name)
                players[1].send(b"Correct")
                break

match = Match(
    Team([champions[name] for name in player1]),
    Team([champions[name] for name in player2])
)

match.play()

print("Sender finished")
send = pickle.dumps(match)
print(send)
players[0].send(send)
players[1].send(send)

database.send(print_match_summary(match).encode())

"""

class Client(Thread):

    def __init__(self, conn, addr, id):
        # Initializing the father class.
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.id = id  # 0 --> player1 and # 1 --> player2

    def run(self):
        global players
        global number_of_players

        # Receiving data from clients
        received = self.conn.recv(BUFFER_SIZE).decode("utf-8")
        print(received)
        if received != None:

            print('You are connected to the server for playing')
            infoserver = self.conn.recv(BUFFER_SIZE).decode("utf-8")
            players = []
            players = infoserver
            for i in players:
                players.append(i)

            # game should be here?

            self.conn.send()

    def handle_session(conn1, conn2):
        conn1 = True
        if conn1:
            pass
        pass

    def check_player_in_lista():
        data = pd.read_csv('some_champs.txt', delimiter="\t")
        print(data.read())
        search_word = input("enter a word you want to search in file: ")
        if(search_word in data.read()):
            print("word found")
        else:
            print("word not found")

        def updateDataBase(): pass

        def send_winner_team(): pass


def main():
    connections = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)

    while True:

        conn, addr = s.accept()
        c = Client(conn, addr, id)
        c.start()
    conn.close()
    s.close()


if __name__ == '__main__':
    print("Waiting for serving requests ...")
    main()

conn.close()
s.close()
"""
