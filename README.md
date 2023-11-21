# QUIXO
The QUIXO game is a simple board game that is played with 2 players (but it can handle up to 4 players).
The board is composed of a 5 ∗ 5 square of small cubes. These cubes have a circle symbol on one side, a cross
symbol on another, and blank faces on the other four, see Figure 1. We start a game by placing the 25 cubes
with blanks face-up.
![image](https://github.com/CaiYingzhi/QUIXO/assets/124078521/1277b937-842c-4ded-a6a7-387c782660e9)

Figure 1: Example board of a QUIXO game (image taken from www.boardgamegeek.com
.
One player uses cross symbols, while the other uses circle symbols, and the players goal is to be the first
to form a line of their own symbol (similar to Tic-Tac-Toe). Each turn, the active player takes a cube that is
blank or bearing his own symbol from the outer ring of the grid (see left figure of Figure 2), rotates it so that
it shows his symbol (in case it was blank), then adds it back to the grid by pushing it into one of the rows from
which it was removed (note that you are not allowed to place the cube back in the position from which it was
taken originally, see right figure of Figure 2). Thus, a few pieces of the grid change places each turn, and the
cubes slowly go from blank to crosses and circles. Play continues until someone forms an horizontal, vertical or
diagonal line of five cubes bearing his symbol, with this person winning the game. Note that there is no draw.
Moreover if both players form a line at the very same time, the player who played that move loses the game.
You can for example view a video of the game rules here: https://www.youtube.com/watch?v=cZT5N6hIFYM
2 Objectives
The objective of the project is to write in Python a working QUIXO program that allows a human player to
play QUIXO against another human player or against a computer player through a menu. Be VERY careful to
implement EXACTLY the game rules (test your program thoroughly and try to think of all the special cases).
The program must allow the user to configure:
 the size n of the board (i.e. the number of rows and the number of columns of the board, the default
values being n = 5). Note that the board must always be square. One always have that the number N of
consecutive same-symbol cubes required for a player to win is equal to n.
 the type of the two players (human or computer), and the difficulty level in case of a computer player.
You have to use the skeleton file quixo.py provided on NTU Learn. Moreover, note that every time you
add a feature to your program, you should test it thoroughly before continuing. Testing your program only at
the very end is the best way to render the bug hunting close to impossible !
2
Figure 2: Rules of the QUIXO game: the left-hand side figure represents in green the cubes that can be played
(outer ring), the right-hand side figure represents the pushes that can be played (it is forbidden to put back the
cube to its original place).
