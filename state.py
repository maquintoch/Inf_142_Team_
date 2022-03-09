from copy import PyStringMap
from champlistloader import load_some_champs
from player import *
import json
import csv
from core import *


class state:
    players = players()
    champions = load_some_champs()

    def get_list_str(self):
        return str(self.players)

    def add_player(self, pName):
        champions_a = [x for x in self.champions if x.name == pName]
        if len(champions_a) <= 0:
            print(f'The champion {pName} is not available. Try again.')
            return
        rock = champions_a[0].str_tuple()[1]
        paper = champions_a[0].str_tuple()[2]
        sicssors = champions_a[0].str_tuple()[3]
        players.add(pName,
                    rock,
                    paper,
                    sicssors)
        self.save()

    def from_string(pString):
        obj = state
        obj.__dict__ = json.loads(pString)
        return obj

    def save_players(self):
        players_rows = []
        filename = "players.csv"
        with open(filename, 'r+') as f:
            f.truncate(0)

        for p in players:
            with open(filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([p.name])

    def save(self):
        self.save_players()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)
