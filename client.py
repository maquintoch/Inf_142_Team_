'''
client script for stablishing a communication to a server
'''
# Comand
from rich.table import Table
from rich.prompt import Prompt
from rich import print
from player import *
import socket
# 1. List> list,None > String
# 2. Add Player -> add,Marco ->

players = None


def get_current_cmd():
    if players == None:
        return "list"
    return "add"


def print_players(pString):
    # Create a table containing available champions
    available_champs = Table(title='Available champions')
    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

    players = players.from_string(pString)

    # Populate the table
    for player in players:
        tuple_object = (player.name, player.rock,
                        player.paper, player.scissors)
        available_champs.add_row(*tuple_object)
    players = available_champs
    print(available_champs)


def chat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = "localhost"
        port = 8001

        s.connect((host, port))
        if players != None:
            name = input('Input Name: ')
            cmd = "add," + name
            s.sendall(b'' + str.encode(cmd))

        else:
            cmd = "list,None"
            s.sendall(b'' + str.encode(cmd))

            print_players(str(s.recv(4096), 'utf-8'))

    chat()


chat()
