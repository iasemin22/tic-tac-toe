# Tic-Tac-Toe


###  Write your code
#### a) Getting started
Open the [tic_tac_toe.py](tic_tac_toe.py) file in VS Code.   
The first lines are already there - when you run the script name in the command line, your game will be started.  
Inside the main function structure you can call all the other functions to perform their tasks.   
**Hints**:   
- Since a game of Tic-tac-toe is basically repeating the same tasks over and over again (like asking the players for input) a `while True` loop can help you to get the game running. You have to make sure, however, that in case of certain events (win, draw,...) the loop will break so that the game will come to an end.
- Another challenge to think about is how to allow each player to take turns at making their moves. Here the **modulo operator** could be helpful.

#### b) Display the board 
To play a round of tic-tac-toe, we need a game board. We should start by defining a function that will display the board on the screen when it is called. There are several ways to display a tic-tac-toe board. Choose the implementation that you can work best with as we proceed.  

Maybe like this...  
1, 2, 3    
4, 5, 6   
7, 8, 9   

or this...   
(0, 0), (1, 0), (2, 0)   
(0, 1), (1, 1), (2, 1)   
(0, 2), (1, 2), (2, 2)   


#### c) Ask for player input 
Before we can start playing define what the markers will be for each player. Usually we just use "X" or "O".  
Now you need a function that asks the player (whose turn it is) where they want to put their marker.  
**Hint**:   
The built-in function `input()` will do this task for you.   
If you want, you can directly add a control mechanism that checks if the desired position was already occupied in a previous turn. 

#### d) Check for Winner
At the end of each turn, your script will have to determine if the most recent play resulted in a win. If it did, it should break the game loop, the player that just played will be declared the winner, the game will be over, and the script will terminate. If a winner is not found, play will continue. Keep in mind that there are 8 different ways for a player to get three in a row. The function you write to solve this part of the problem will have to implement a lot of logic.   

#### e) Check for Draw
There is a chance that a draw will occur in the game. If this happens, your script should be aware. If all of the squares have been filled in, and there is no winner, it should break the game loop and a draw should be declared. 

