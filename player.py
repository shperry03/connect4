'''
Class for players and making moves

 - Human Player will make moves themselves
 - Monte Carlo Player will play based on monte carlo simulation
 - Deep learning plauer will play based on neural network reinforcement learning 

'''
from gameboard import GameBoard


class Player():

    def __init__(self,number: int) -> None:
        # player number
        self.p_number = number

    def make_move(self, board: GameBoard):
        print("Player ", self.p_number, "'s Turn!\n")
        # ask to enter a column
        print(board.board)
        print()
        # scan in number and make move
        col = int(input("Enter a column number to make a move.\n"))
        while board.move(col=col, player=self.p_number) == False:
            col = int(input("Enter a valid column number to make a move.\n"))
        