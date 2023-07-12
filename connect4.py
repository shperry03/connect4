from gameboard import GameBoard
from player import Player
from montecarlo import MonteCarlo
import csv


board = GameBoard()
player1 = Player(1)
player2 = MonteCarlo()

mydict = {}
with open('map_playing_itself1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:
            mydict[row[0]] = row[1]

player2.policy_map = mydict 

while (board.winner == 0):
    player1.make_move(board=board)
    if board.winner != 0:
        break
    board.move(col=player2.follow_policy(board,player2.policy_map),player=2)

print()
print(board.board)
print()
print('Player ', board.winner,' Wins!')
