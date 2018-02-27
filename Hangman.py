def hangman():

    word = input('Player 1: Please select a word or phrase: ').lower() #word to play with in lower case
    
    letters = [] # to be used later for the letters in the selected word

    ### function for player 1 to select a word
    def selectWord(word):
        for x in range(len(word)): # iterate though each letter of the word
            letters.append(word[x]) # add each letter to a list of letters
        return(letters) # return the list of letters

    #implementation of above function
    selectWord(word)

    # formatting to player2 cannot see player 1's word and showing strikes left:
    print('\n' * 50)
    print('Please do not scroll up.')
    print('\n' * 20)
    level = input('Player 2: Please select a level; easy, medium, or hard? ').lower() # selecting a level, which corresponds to allowed strikes

    if level[0] == 'e': #just the first letter to account for typos
        strikes = 13 # sets the easy level to miss 12 times
    elif level[0] == 'm':
        strikes = 10 # medium level gives 9 misses
    elif level[0] == 'h':
        strikes = 6 # hard level gives 6 misses

    misses = strikes
    print('You have ' + str(strikes) + ' strikes remaining.')

    ### function to display the length of the word or phrase
    def showSize(letters):
        size = []
        for x in letters: # iterates through the characters in the word
            if x.isalpha() == True: #if the character is a letter
                size.append('_') # then add an underscore to the 'board'
            else: #otherwise
                size.append(x) # keep the character as is
        return(size) #return the board
            
    # implamentation of above function and scaffolding for man to hang from
    board = showSize(letters)
    print('  _____\n |     |\n |\n |\n |\n_|_' + '\n')
    print(board)
        
    # list of possible letters to guess from
    possibles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    
    man = ['  _____\n |     |\n |\n |\n |\n_|_', '  _____\n |     |\n |    ( )\n |\n |\n_|_', '  _____\n |     |\n |    ( )\n |     *\n |\n_|_', '  _____\n |     |\n |    ( )\n |    \*\n |    \n_|_', '  _____\n |     |\n |    ( )\n |    \*/\n |    \n_|_', '  _____\n |     |\n |    ( )\n |    \*/\n |    /\n_|_', '  _____\n |     |\n |    ( )\n |    \*/\n |    / \\\n_|_', '  _____\n |     |\n |    ( )\n |   -\*/\n |    / \\\n_|_', '  _____\n |     |\n |    ( )\n |   -\*/-\n |    / \\\n_|_', '  _____\n |     |\n |    ( )\n |   -\*/-\n |   _/ \\\n_|_', '  _____\n |     |\n |    ( )\n |   -\*/-\n |   _/ \\_\n_|_', '  _____\n |     |\n |    (")\n |   -\*/-\n |   _/ \\_\n_|_', '  _____\n |     |\n |    (")\n |  o-\*/-\n |   _/ \\_\n_|_', '  _____\n |     |\n |    (")\n |  o-\*/-o\n |   _/ \\_\n_|_']  
    while strikes > 0: #while player 2 has strikes left
        if '_' not in board:
            print('Player 2 wins!\n ')
            response = input('Play Again? Y/N\n').lower()
            if response == 'y':
                print('\n')
                hangman()
            else:
                break
        letter = input('Please guess again: ').lower() #prompt the user to guess
        print('\n'*5) #spacing for easier reading
        print("Player 2's Guess: " + letter) #display player 2's guess
        positions = [] # create an empty list that will correspond to the positions of the letters
        if letter in possibles: #if the guess is in the letters left
            possibles.remove(letter) # remove the letter from the list of letters left
            if letter in letters: #if the guess is in the word
                print('Good Guess!')
                for x in range(len(letters)): #iterate through the word
                    if letter == letters[x]: #find the position of the matching letter
                        positions.append(x) #add the position of the matching letter to the list of positions
            else: #if the guessed letter is not in the word
                strikes = strikes - 1 #remove a strike
                print(letter + ' is not in the word.')
                print('Strikes left: ' + str(strikes))
                if strikes == 0: # if player 2 has no strikes left
                    print(man[misses-strikes])
                    print('Player 1 wins! The word is ' + word)
                    break #end the game
        else: # if the character guessed is not available
            print(letter + ' is not a valid guess. ')
        print(man[misses-strikes])



        ### displays the new board after each guess
        def newBoard(letters, positions, letter):
            for x in positions: # iterates through the index of letters
                board[x] = letter #adds the letter guessed to the corresponding index on the board
            return(board) #returns the new board


        print(newBoard(letters, positions, letter)) #prints the board


hangman() #implement the game
