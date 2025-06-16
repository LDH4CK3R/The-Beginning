import math
import random

class Player:
    def __init__(self, letter):
        # letter  is x or o
        self.letter = letter

    # we want all players to get their next more
    def get_move(self, game):
        pass

class RandomComputer(Player):
    def _init_(self, letter):
        super()._init_(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter) 

    def get_move(self, game):
        pass           