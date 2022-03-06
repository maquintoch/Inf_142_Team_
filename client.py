'''
client script for stablishing a communication to a server
'''
from socket import socket
from zoneinfo import available_timezones
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from team_local import print_available_champs
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
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
champions = load_some_champs()
ListOfChampions = print_available_champs(champions)
ListOfChampions = json.dumps(ListOfChampions)
#ListOfChampions = json.dumps(ListOfChampions)
# conn.send(ListOfChampions.encode())
# conn.sendall(bytes(ListOfChampions.encode()))


####
ListOfChampions = json.loads(ListOfChampions)

#ListOfChampions = json.JSONDecoder().decode(ListOfChampions)

###
# Converting a rich table to a data frame for printing

#df = table_to_df(ListOfChampions)
# print(df)
###
#ListOfChampions = dict(ListOfChampions)
#ListOfChampions = json.loads(ListOfChampions)
print(type(ListOfChampions))
#ListOfChampions = dict(ListOfChampions)
print(f"From Server : {ListOfChampions}")
#print(f"From Server: {df}")
sock.close()


""" def table_to_df(rich_table: Table) -> pd.DataFrame:
    available_timezones.data = {
        x.header: [Text.from_markup(y).plain for y in x.cells] for x in available_timezones.columns
    }
    return pd.DataFrame(available_timezones)
"""
