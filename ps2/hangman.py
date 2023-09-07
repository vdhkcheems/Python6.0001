# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count=0
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                count+=1
                break

    if count == len(secret_word):
        return True

    return False       



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ans=""
    for i in secret_word:
        if i in letters_guessed:
            ans+=i
        else:
            ans+='_ '
    return ans


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    x = string.ascii_lowercase
    y=""
    for i in x:
        if i not in letters_guessed:
            y+=i

    return y
            
    
    
    

def hangman(secret_word, warnings=3):
    length = len(secret_word)
    guesses = length + 5
    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {length} letters long\n")

    letters_guessed = []

    while guesses > 0:

        print(f"You have {guesses} {'guess' if guesses == 1 else 'guesses'} left")
        print(f"You have {warnings} {'warning' if warnings == 1 else 'warnings'} left")
        letters = get_available_letters(letters_guessed)
        print(f"Available letters: {letters}")
        letter = input("Give me a letter: ")

        if len(letter) != 1 or not letter.isalpha():
            print(f"WARNING: Please enter exactly one letter. You've lost a warning.")
            warnings -= 1
            continue

        letter = letter.lower()

        if letter in letters_guessed:
            print(f"Oops! You've already guessed that letter: {current_guess}")
        elif letter in secret_word:
            letters_guessed.append(letter)
            current_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {current_guess}")
        else:
            letters_guessed.append(letter)
            current_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Wrong guess: {current_guess}")
            guesses -= 1

        if '_' not in current_guess:
            print("Congratulations, you won!")
            return

        print()

    print(f"\nYou ran out of guesses. The word was {secret_word}")

# Example usage:
# Replace 'get_available_letters' and 'get_guessed_word' with your actual functions
# secret_word = "example"  # Replace with your word
# hangman(secret_word)


# Example usage:
# Replace 'get_available_letters' and 'get_guessed_word' with your actual functions
# secret_word = "example"  # Replace with your word
# hangman(secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = "".join(my_word.split())
    if len(my_word)!=len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] == '_ ':
                continue
            elif my_word[i] == other_word[i]:
                continue
            else:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = "".join(my_word.split())
    words = []
    for j in wordlist:
        count = 0
        if len(j) != len(my_word):
                continue
        else:
          for i in range(len(my_word)):
              if my_word[i] == '_':
                  count+=1
              elif my_word[i] == j[i]:
                  count+=1
              else:
                  continue
        if count == len(my_word):
            words.append(j)
        else:
            continue
    
    for word in words:
        print(f"{word} ", end="")
    print()
               



def hangman_with_hints(secret_word, warnings=3):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(secret_word)
    guesses = length + 5
    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {length} letters long\n")

    letters_guessed = []

    while guesses > 0:

        print(f"You have {guesses} {'guess' if guesses == 1 else 'guesses'} left")
        print(f"You have {warnings} {'warning' if warnings == 1 else 'warnings'} left")
        letters = get_available_letters(letters_guessed)
        print(f"Available letters: {letters}")
        letter = input("Give me a letter: ")

        if not letter.isalpha():
            print(f"WARNING: Please enter exactly one letter. You've lost a warning.")
            warnings -= 1
            continue
        elif letter == 'hint':
            show_possible_matches(current_guess)

        letter = letter.lower()

        if letter in letters_guessed:
            print(f"Oops! You've already guessed that letter: {current_guess}")
        elif letter in secret_word:
            letters_guessed.append(letter)
            current_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {current_guess}")
        else:
            letters_guessed.append(letter)
            current_guess = get_guessed_word(secret_word, letters_guessed)
            print(f"Wrong guess: {current_guess}")
            guesses -= 1

        if '_' not in current_guess:
            print("Congratulations, you won!")
            return

        print()

    print(f"\nYou ran out of guesses. The word was {secret_word}")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
