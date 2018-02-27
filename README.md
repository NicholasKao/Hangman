Hangman
Developed - Summer 2015
Implemented in Python3.

I independently developed a hangman game in Python3 after one semester of computer science classes. I have minimally cleaned up this project since, only changing text prompts and formatting.

The game tracks the state of the board, toggles between users (either Human vs. Human or Human vs. Computer), and runs validation logic to ensure only legal moves are carried out. Due to playing against a human, there is not validation that the chosen word is in the dictionary.

To play the game agains a human opponent, use the command "python Hangman.py" and the game flow is as follows;

1) Player 1 is prompted to chose a word for player 2 to guess.
2) Upon entering a word, the game board shift up (by printing blank lines) and warns not to scroll up, then prompts Player 2 to select a level (easy, medium, or hard), which corresponds to how many missed guesses are permitted.
3) After selecting the level, Player 2 will be informed how many strikes (missed guesses) he/she has remaining and will be presented with an empty board with blanks indicating the word to guess.
4) After guessing a letter, if the guess is legal and correct:
    - The guess will be displayed
    - "Good Guess" will be displayed
    - The letter will fill in the correct blank spots
    - Player 2 will be prompted to guess again
  if the guess is legal and incorrect:
    - The guess will be displayed
    - "[Player's guess] is not in the word" will be displayed
    - The board will be updated with an additional body part hanging
    - Player 2 will be prompted to guess again
  if the guess is illegal (already been guess or not a letter):
    - The guess will be displayed
    - "[Player's guess] is not a valid guess" will be displayed
    - The current board will be displayed
    - Player 2 will be prompted to guess again
5) The game will end in one of three ways;
    1) Player 2 will correctly guess all the letters of the word before running out of strikes. In this case:
        -Prompts for a successful guess will be displayed as above
        -The current board (with the completed word) will be displayed
        -"Player 2 win!" will be displayed
        -Users are prompted to play again by entering either "y" or "n"
    2) Player 2 will run out of strikes before successfully guessing the word. In this case:
        -Prompts for an unsuccessful guess will be displayed as above
        -"Strikes Left" will be 0
        -The current game board (with the completed hanging man) will be displayed
        -"Player 1 Wins! The word is [Player 1's word]" will be displayed
        -Users are prompted to play again by entering either "y" or "n"
    3) The program is canceled by a keyboard interrupt
    
    
The source code is adequately commented in order to follow my logic.
        
        
        
        
        
        
        
        
     
