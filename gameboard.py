"""
GAME BOARD FOR CONNECT 4 PROJECT

This is the game-board class which will:
    -- model the board [][]
    -- check for wins
    -- execute moves

"""

import numpy

class GameBoard():

    def __init__(self) -> None:
        
        # create a board width,height = 7,6 of zeros
        # zeros will represent an empty space
        # 1s and 2s will represent players and moves
        self.board = numpy.zeros((6, 7), dtype=int)

        # winner will be integer (1 for p1 and 2 for p2)
        self.winner = 0


    '''
    Make the move that the player wants
      - if it's invalid return false to ask for another move
      - else make the move and check for the win and return true for successful move
    '''
    def move(self, player: int, col: int) -> bool:
        # check if move is in valid range
        # if invalid return false and allow them to remove
        # else make the move and return true
        if col > 7 or col < 1 or self.board[0,col-1] != 0:
            # if out of range or column full return false
            return False
        # else, move was valid
        else: 
            # go through the column to find the next open space, 5 is constant because board is only 6 rows in height
            for i in range(5, -1, -1):
                if self.board[i,col-1] == 0:
                    # make the move when open space is found
                    self.board[i,col-1] = player
                    # now that move is made, check if the player won with that move
                    if self.check_win():
                        self.winner = player
                    # return true because move has been made
                    return True
        
        return False
            
                

    """
    Checks for wins in the board
     - first checks vertical
     - 2nd checks horizontal
     - then diagonally in both directions
    """
    def check_win(self) -> bool:
        # check for wins in the board
        # check vertical wins
        for i in range(7):
            for j in range(3):
                if self.board[j,i] != 0 and self.board[j,i] == self.board[j+1,i] == self.board[j+2,i] == self.board[j+3,i]:
                    return True
        # now check horizontal wins
        for i in range(6):
            for j in range(4):
                if self.board[i,j] != 0 and self.board[i,j] == self.board[i,j+1] == self.board[i,j+2] == self.board[i,j+3]:
                    return True
        # more difficult, check diagonals
        for i in range(3, 6, 1):
            for j in range(4):
                if self.board[i,j] != 0 and self.board[i,j] == self.board[i-1,j+1] == self.board[i-2,j+2] == self.board[i-3,j+3]:
                    return True
        
        for i in range(3, 6, 1):
            for j in range(3, 7, 1):
                if self.board[i,j] != 0 and self.board[i,j] == self.board[i-1,j-1] == self.board[i-2,j-2] == self.board[i-3,j-3]:
                    return True
        
        return False
    
    def check_space(self) -> bool:
        # check top row for space 
        # if no space return false else true
        if 0 not in self.board[0]:
            return False
        else:
            return True    
               
