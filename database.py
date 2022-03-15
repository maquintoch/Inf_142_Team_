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


""" class Client(Thread):
    def __init__(self, conn, addr):
        # Initializing the father class
        threading.Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def getListofChampions(self):
        data = open('some_champs.txt', 'r').read()
        return data

    def run(self):
        print(" There is a client that is asking for the list of champions")

        streaming = self.conn.recv(BUFFER_SIZE*2).decode("utf-8")
        print(" Received Data", streaming)
        self.conn.sendall(json.dumps(
            self.getListofChampions()).encode("utf-8"))
        isTrue = True
        while isTrue:
            incomingMessages = streaming.recv(2048*2).decode()
            print(incomingMessages)
            while incomingMessages != '':
                SavingFileIncomingMessages = open("Scores.txt", 'a+')
                SavingFileIncomingMessages.write(
                    incomingMessages + 'It is a victory\n')
                print(incomingMessages.read())
                break


def main():
	
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_server.connect(('127.0.0.1', 8000))
    cliente_server.send('<'.encode("UTF-8"))
    time.sleep(1)
    # cliente_server.send(direccion.encode("UTF-8"))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)

	conn, addr = s.accept()
	c = Client(conn, addr)
	c.run()
	conn.close()
	s.close()


if __name__ == "__main__":
    print("Server database listening...")
    main()
conn.close()
s.close() """
