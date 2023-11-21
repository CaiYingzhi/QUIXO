1 The Quixo game The QUIXO game is a simple board game that is played with 2 players (but it can handle up to 4 players). The board is composed of a n ∗ n square of small cubes. These cubes have a circle symbol on one side, a cross symbol on another, and blank faces on the other four, see Figure 1,2. We start a game by placing the n^2 cubes with blanks face-up.

![image](https://github.com/CaiYingzhi/QUIXO/assets/124078521/51658239-9895-48e4-a10b-acbdd6267c78)

Figure 1: Example board of a QUIXO game (image taken from www.boardgamegeek.com) .

![image](https://github.com/CaiYingzhi/QUIXO/assets/124078521/0c931dbd-242b-4da6-9c95-b2a1d10701a2)

One player uses cross symbols, while the other uses circle symbols, and the players goal is to be the first to form a line of their own symbol (similar to Tic-Tac-Toe). Each turn, the active player takes a cube that is blank or bearing his own symbol from the outer ring of the grid (see left figure of Figure 2), rotates it so that it shows his symbol (in case it was blank), then adds it back to the grid by pushing it into one of the rows from which it was removed (note that you are not allowed to place the cube back in the position from which it was taken originally, see right figure of Figure 2). Thus, a few pieces of the grid change places each turn, and the cubes slowly go from blank to crosses and circles. Play continues until someone forms an horizontal, vertical or diagonal line of five cubes bearing his symbol, with this person winning the game. Note that there is no draw. Moreover if both players form a line at the very same time, the player who played that move looses the game.

You can for example view a video of the game rules here: https://www.youtube.com/watch?v=cZT5N6hIFYM
