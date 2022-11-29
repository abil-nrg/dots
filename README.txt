Usage
    -Open up dots.py and run it in a terminal\
    -Install the colorama python module 
    -Input the move you want to make, by typing in the (x,y) of the location of the line you want to play
    -Have fun
 
Objective
    -Design a game of Dots and Boxes in a terminal envirnoment and implement an AI oppenent
 
Game Description
    -Dots and Boxes is a 2 player game played on a n x n grid, set by the user. The objective of the game is to connect as many dots together that result in a box being made. Most boxes made wins.
 
Game Rules
    A player can decide on which two dots to connect each turn
        1. The human player (player 1) will chose a space to connect to dots in, the CPU player(player 2) will reciprocate.
        2. To move, think of each element on the board as an element in a square matrix of size n*2 - 1, where n is the grid size of our game. To then place a line connecting dots, you must enter its location within the matrix.      
        3. Player 1 and Player 2 will play until there are no more dots to connect 
        4. Dots can only be connected horizontally and vertically, no diagonals
        5. The player who closes a box (connects 4 dots together, making a box) will earn a point and the chance to have another turn right away.
        6. The game ends when all dots have been connected, the person with the most boxes made wins.
 
Implementation 
    The implementation of this game was divided into three steps: creating the game itself, creating an AI opponent, and printing a visual aide for the end-user.
 
    Game itself
        The standard procedure of each turn is to: accept user input and check if it is legal, updating the board state, and checking if a box has been made. The board state is saved as a 2d array, containing where a dot would be, where a line would be, and the inside of the boxes. Accepting user input, simply modified the 2d array. Check if a box has been made, 
 
    AI Algorithm
        The "AI" algorithm, goes through each "box" ( a set of four dots) and receives the amount of lines with in it. We then calculate the amount of moves necessary to "win" that box. The AI then picks the least amount of moves, if 2 is one of the amounts it is given the least amount of priority over other moves.
 
    Visual Aide
        Since our representation is a 2d array, each value is checked and printed from every single sub array, updating the color of the '-' or '|' depending on the which player made the move. 
 
 
Team Members
    Ali Gaineshev (https://github.com/ali-gaineshev)
    Omar Madhani (https://github.com/omarmadhani)
    Abil Nurgaliyev (https://github.com/abil-nrg)
    Sam Peets (https://github.com/sam-peets)
 
