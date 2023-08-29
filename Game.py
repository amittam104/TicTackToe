class TicTackToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in[self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def empyt_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
def play(game, x_player, o_player, print_game=True)
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # itterate while game still have empty squares
    # No need to worry about winner we will just return it which will break the loop

    while game.empty_squares():
        # get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
    # let's define a function to make a move