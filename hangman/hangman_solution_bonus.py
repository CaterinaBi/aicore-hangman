import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    round: int
        The number of the round being played
    list_visual: list
        A list of rudimentary visuals to be displayed to mimic the original on-paper drawings
    ascii_messages: list
        A list of messages created using ASCII characters to be displayed in crucial moments

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # initialises the attributes as indicated in the docstring
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.list_letters = []
        self.round = 0
        self.list_visual = [
            '''
            __________
              |      |
              |    \ O /
              |      |
              |     /\\
            __|____
            ''',''' 
            __________
              |      |
              |      O
              |      |
              |     /\\
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |     /
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |
            __|____
            ''','''
             __________
              |      |
              |      O
              |
              |
            __|____
            ''']
        self.ascii_messages = [
            '''
            %%    %%   %%%%%%%%   %%         %%         %%%%%%%%   
            %%    %%   %%         %%         %%         %%    %%   
            %%%%%%%%   %%%%%      %%         %%         %%    %%   
            %%    %%   %%         %%         %%         %%    %%           
            %%    %%   %%%%%%%%   %%%%%%%%   %%%%%%%%   %%%%%%%%   
            ''','''
            %%    %%   %%%%%%%%   %%    %%       %%         %%%%%%%%   %%%%%%%%   %%%%%%%%
            %%    %%   %%    %%   %%    %%       %%         %%    %%   %%         %%
            %%%%%%%%   %%    %%   %%    %%       %%         %%    %%   %%%%%%%%   %%%%%
                  %%   %%    %%   %%    %%       %%         %%    %%         %%   %%
            %%%%%%%%   %%%%%%%%   %%%%%%%%       %%%%%%%%   %%%%%%%%   %%%%%%%%   %%%%%%%%
            ''','''
            %%    %%   %%%%%%%%   %%    %%       %%      %%   %%   %%     %%
            %%    %%   %%    %%   %%    %%       %%      %%   %%   %%%%   %%
            %%%%%%%%   %%    %%   %%    %%       %%  %%  %%   %%   %% %%  %%
                  %%   %%    %%   %%    %%       %%  %%  %%   %%   %%  %% %%
            %%%%%%%%   %%%%%%%%   %%%%%%%%        %%%%%%%     %%   %%   %%%%
            '''
        ]
        # prints messages upon initialisation
        print(f"{self.ascii_messages[0]}")
        print("WELCOME TO THE GAME OF FRUIT HANGMAN")
        print(f"The mistery word is the name of a fruit and has {len(self.word)} characters.")
        print("Can you guess it?")
        print(f"{self.word_guessed}\n")
        #print(f"**************** ROUND NUMBER {self.round} ****************\n")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # checks if the input letter is in the random word
        # uses the lower() method to convert the input letter to lowercase
        letter = letter.lower()
        if letter in self.word:
            print(f"Nice job! The letter '{letter}' is in the word to be guessed!")
            # replaces the '_' in the word_guessed list with the input letter when the input letter is in the random word
            letter_index = 0
            for position, char in enumerate(self.word):
                if char == letter:
                    letter_index = position
                    self.word_guessed[letter_index] = letter
            # print(f"Nice! {letter} is in the word!")
            print(f"These are the letters that you have guessed: {self.word_guessed}\n")
            # the number of unique letters in the input word that have not been guessed yet is reduced by 1
            self.num_letters -= 1
        # reduces the number of lives by 1 if the input letter is not in the random word
        else:
            self.num_lives -= 1
            print(f"Sorry, '{letter}' is not in the word.")
            print(f"{self.list_visual[self.num_lives]}")
            if self.num_lives == 1:
                print(f"You have {self.num_lives} life left.\n")
            else:
                print(f"You have {self.num_lives} lives left.\n")
        # appends input letter to list_letters
        self.list_letters.append(letter)

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # asks the user for a letter and assigns it to a variable called `letter`
        # prints message if the input is more than one letter
        while True:
            letter = input("Please enter a letter. Don't use numbers and ASCII characters: ")
            print("")
            if len(letter) != 1:
                print("Please, enter just one character!")
                continue
            # prints message if the input letter has already been tried
            elif letter in self.list_letters:
                print(f"{letter} was already tried.")
                continue
            # calls the check_letter method if the input letter is valid
            else:
                self.check_letter(letter)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    # iteratively asks the user for an input letter until the user guesses the word or runs out of lives
    # prints messages accordingly
    while True:
        #game.round = 0
        if game.num_lives == 0:
            print(f"{game.ascii_messages[1]}")
            print(f"The word was '{game.word}'.\n")
            break
        elif game.num_letters > 0:
            game.round += 1
            print(f"**************** ROUND NUMBER {game.round} ****************\n")
            game.ask_letter()
        else:
            print(f"{game.ascii_messages[2]}")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 
    'tangerine', 'lychee', 'avocado', 'mango', 'papaya', 'cherry', 'kiwi', 'melon',
    'dragonfruit', 'blueberry', 'blackberry', 'cranberry', 'grapes', 'raspberry']
    play_game(word_list)
# %%