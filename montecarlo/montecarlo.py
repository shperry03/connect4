'''
Implementation of On-Policy Monte Carlo Simulation to solve Connect4

'''
import numpy as np
import copy
from gameboard import GameBoard
import csv

# because np arrays arent hashable, need to convert to string to use in dict
# I found this solution online at  https://stackoverflow.com/questions/46961952/how-to-make-a-tuple-including-a-numpy-array-hashable
# class KeySet():
#     def __init__(self, i, np_arr) -> None:
#         self.i = i
#         self.arr = np_arr

#     def __hash__(self) -> int:
#         return hash((self.i, hash(self.arr.tostring())))

class MonteCarlo():

    def __init__(self) -> None:
        # policy = map:
        # policy = { board position: what move to go based on value}
        self.policy_map = {}

        mydict = {}
        with open('map.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    mydict[row[0]] = row[1]
        self.adversary_map = mydict


    '''
    I dont need to initialize policy, if no policy exists in that board position, then make it random
    '''

    '''
    Return full episode and if win, lose, or draw
     win = +1
     lose = -1
     draw = -0.5
    '''
    def generate_episode(self):


        # episode will be an array of np arrays that represent the board
        episode = []

        board = GameBoard()

        while board.winner == 0 and board.check_space():
            P1, P2 = 1, 2
            '''
            record the board before player 1 makes a move, evaluating positions before the 
            Player 1 is monte carlo
                makes first move, check for win
            Player 2 will be a random move
            '''

            episode.append(board.board)
            # follow_policy returns a column number
            board.move(col=self.follow_policy(board,self.policy_map),player=P1)
            if board.winner != 0 or board.check_space() == False:
                episode.append(board.board)
                break
            # move randomly for player 2
            board.move(col=self.follow_policy(board,self.adversary_map), player=P2)

        if board.winner == 1:
            return episode, 1
        elif board.winner == 2:
            return episode, -1
        else:
            return episode, -0.5
        
        

    def follow_policy(self,board: GameBoard, policymap) -> int:
        '''
          make every next move and see which has the highest value?
          if all equal make random
          if it doesnt exist then it is 0
        '''
        # go through every column and pick max from policy map
        moves = []
    
        for i in range(1,8,1):
            board_copy = copy.deepcopy(board)
            # check to see if move is valid and make the move
            if board_copy.move(col=i,player=1):
                ks = board_copy.board.tostring()
                # if move was made then check its value
                # if its value exists then check it against current max
                if policymap.get(ks):
                    moves.append(policymap[ks])
                # if the value is greater, set the max_val to new max and that is the move for the moment
                else:
                    moves.append(0)
        # we want it to explore rather than play the "Best" move at every turn
        # 30% of the time will be random
        best_moves = []
        max_val = max(moves)
        count = 1
        for i in moves:
            if i == max_val:
                best_moves.append(count)
            count+=1
        # randomly sample from the tied best moves
        # that way it isnt always selecting 1 
        move = np.random.choice(a=best_moves,size=1)
        '''
        CHANGE THIS TO GET THE BEST PLAYS
        '''
        if np.random.randint(11) % 10 > 3:
            return move[0]
        else:
            num = np.random.randint(8)
            return num








    def get_value(self):

        returns = {}

        discount = 0.8
        # val map is mapping of board to value
        val_map = {}

        for _ in range(1000000):
            # update policy based on what you learned and then continue learning
            self.policy_map = val_map
            episode, result = self.generate_episode()
            #print(episode)
            # set the last position to the value of the result
            # this is what will propogate to the previous positions
            ks = episode[-1].tostring()
            val_map[ks] = result
            count = len(episode)

            G = 0
            for i in range(count-2,0,-1):
                state = episode[i].tostring()
                state_prev = episode[i+1].tostring()
                G = (discount)*val_map[state_prev]
                if (state) in returns:
                    returns[state].append(G)
                else:
                    returns[state] = []
                    returns[state].append(G)
                val_map[state] = (sum(returns[state])/len(returns[state]))




