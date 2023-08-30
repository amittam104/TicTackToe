import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # All player should get thier next move
    def get_move(self, game):
        pass
 
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # get a random valid spot for the next move of computer
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # We will check whether the values is correct or not.
            # If it is not then will return Invalid input
            # If the spot is not available then will return Invalid input
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again. ")
        return val

