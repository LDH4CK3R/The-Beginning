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
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter) 

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. input move (0-9):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its in valid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successful, then yay!
            except ValueError:
                print('invalid square. Try again.')

        return val           