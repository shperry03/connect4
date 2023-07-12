# Connect 4
Implementation of the popular game Connect 4 with different AI algorithms. Monte Carlo Simulation and Deep Reinforcement Learning (soon to be added)

# Game
The game is programmed in the gameboard class which tracks the board, checks for wins, and allows players to move. 

# Gameplay
Players can play against the AI or other players by just creating a new Player using the Player class (example found in connect4.py). There are example of how to create players of different types using the other AI implementations (right now only the Monte Carlo simulation is completed). 

# ML Implementations
- ~~Monte Carlo Simulation~~
<br> <br> &nbsp;&nbsp;&nbsp;&nbsp;To run the Monte Carlo Simulation agent, adjust the code in montecarlo.py to fit your project and run the code. With no value mapping already generated, you need to set self.adversary_map to a blank dictionary (this is just randomly generated moves). After running the file, a value map will be generated in a csv file which maps board positions to a value that was generated from the monte carlo simulation. The follow_policy can be changed to fully follow the policy generated. <br> <br>
- Deep Reinforcement Learning (TensorFlow)
- Deep Reinforcement Leanring (PyTorch)
