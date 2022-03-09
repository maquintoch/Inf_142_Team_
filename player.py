import json


class players:
    players = []

    def add(name):
        players.append(name)

    def from_string(pString):
        obj = players()
        obj.__dict__ = json.loads(pString)
        return obj

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)


class player:
    def __init__(self, name,
                 rock: float = 1,
                 paper: float = 1,
                 scissors: float = 1) -> None:
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.name = name
