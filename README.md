# Eight_Puzzle

Eight Puzzle
The Eight Puzzle is a classic sliding puzzle game, also known as the 3x3 puzzle. 
The game consists of a 3x3 grid with eight tiles numbered from 1 to 8 and one empty tile. 
The objective is to rearrange the tiles in numerical order, with the empty tile in the bottom right corner, 
by sliding them one at a time into the empty space.

Implementation
This implementation of the Eight Puzzle uses Python and the A* search algorithm to find the optimal solution to the puzzle. 
The A* search algorithm uses a heuristic function to estimate the cost of reaching the goal state from the current state. 
The heuristic function used in this implementation is the Manhattan distance, 
which is the sum of the horizontal and vertical distances between each tile and its goal position.

To run the program, simply run the eight_puzzle.py file in a Python environment. 
The program will prompt you to enter the initial state of the puzzle as a string of numbers separated by spaces. 
For example, the initial state of the puzzle below would be entered as 1 3 4 8 6 2 7 _ 5.

Copy code

1 3 4

8 6 2

7 _ 5

Once you enter the initial state, the program will use the A* search algorithm to find the optimal solution to the puzzle and print the solution steps to the console.

Files
eight_puzzle.py: the main program file containing the implementation of the Eight Puzzle and A* search algorithm

test_eight_puzzle.py: a test file for the eight_puzzle.py program

README.md: this file
Dependencies
This program requires Python 3.x to run. There are no other external dependencies.
