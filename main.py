"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Martin Šenk
email: oshenny@icloud.com
"""

# This file is part of the Engeto online python academy.

import random


INTRO_TEXT = """Hi there! 
I've generated a random 4 digit number for you. 
 Let's play a bulls and cows game."""

# ________________________________________________
# ________________________________________________
# ________________________________________________
# Below are functions that help to separate sentences and calculate their lengths. Functions are not used in the game, but they are useful for the intro text and were educationally included.

SENTENCE_ENDING_CHARS = ["!", "?", "."]

LENGTH_LIMIT = 4


def separate_sentences(
        text: str, 
        ending_characters: list = ["!", "?", "."]) -> list:
   
    """
    Return text split into sentences, each kept with its original
    end-punctuation.

    Example
    -------
    >>> separate_sentences("Hi there! How are you? Fine.")
    ['Hi there!', 'How are you?', 'Fine.']
    """

    sentences = []
    helper_sentence = ""

    for character in text:
        helper_sentence += character
        if character in ending_characters:
            sentences.append(helper_sentence.strip())
            helper_sentence = ""
    
    return sentences

def calculate_sentence_lengths(
        sentences:list) -> list:
    
    """
    Return the character count of every sentence in sentences.

    Example
    -------
    >>> calculate_sentence_lengths(['Hi there!', 'How are you?'])
    [9, 11]
    """

    return [
        len(sentence)
        for sentence
        in sentences
    ]

def create_separator(text: str, char: str = "-") -> str:

    return char * max(calculate_sentence_lengths(separate_sentences(text)))

def print_sep(printed_text: str):

    print(create_separator(printed_text))

# ________________________________________________
# ________________________________________________
# ________________________________________________
# Below starts the main part of the game, which generates a random number, checks user input, calculates bulls and cows, and provides feedback until the user guesses the number correctly.

def generate_game_number() -> str:
    
    """
    Generate a random 4-digit number with no repeating digits.
    """

    first_number = random.choice(range(1, 10))
    other_numbers = random.sample([number for number in range(10) if number != first_number], 3)

    return str(first_number) + "".join(str(number) for number in other_numbers)


def check_user_input() -> str:

    """
    Check user input for the game number.
    Return the input if it is valid, otherwise prompt the user again.
    """

    while True:
        user_input = input("What is your guess? \n >>> ").strip()
        print_sep(INTRO_TEXT)

        if len(user_input) == 0:
            print("You didn't enter anything. Please do so.")
            print_sep(INTRO_TEXT)
        
        elif not user_input.isdigit():
            print("Your input should only contain digits.")
            print_sep(INTRO_TEXT)

        elif len(user_input) != LENGTH_LIMIT:
            print("Please enter a 4-digit number.")
            print_sep(INTRO_TEXT)

        elif user_input[0] == "0":
            print("First digit cannot be 0. Please try again.")
            print_sep(INTRO_TEXT)

        elif len(set(user_input)) != LENGTH_LIMIT:
            print("Each digit in the number must be unique. Please try again.")
            print_sep(INTRO_TEXT)
        else: 
            return user_input



def check_bulls_and_cows(guess: str, game_number: str, guesses: list[str]) -> tuple:

    """
    Check the user's guess against the generated game number.
    Return the number of bulls, cows and the number of guesses made.
    """

    while True:
        if guess not in guesses:
            guesses.append(guess)

            bulls = sum(1 for position in range(LENGTH_LIMIT) if guess[position] == game_number[position])
            cows = sum(1 for digit in guess if digit in game_number) - bulls
            number_of_guesses = len(guesses)
            break


        else:
            print("You've already guessed that number. Try again.")
            print_sep(INTRO_TEXT)
            guess = check_user_input()

    return bulls, cows, number_of_guesses


def choose_word(bulls: int, cows: int) -> tuple:

    """
    Choose the correct word for bulls and cows based on their count.
    Return a tuple with the correct words.
    """

    if bulls == 1:
        bulls_word = "bull"
    else:
        bulls_word = "bulls"

    if cows == 1:
        cows_word = "cow"
    else:
        cows_word = "cows"

    return bulls_word, cows_word


def main():

    """
    Main function to run the Bulls and Cows game.
    :args: None

    This function inits the game, generates a random number,
    checks user input, calculates bulls and cows, and provides feedback
    until the user guesses the number correctly.
    """

    introduction_sentences = separate_sentences(INTRO_TEXT)
    
    for sentence in introduction_sentences:
        print(sentence)
        print_sep(INTRO_TEXT)
    
    generated_game_number = generate_game_number()

    guesses = []

    print(f"""The rules are simple:
- You will guess a 4-digit number.
- For every guess, I will tell you how many bulls and cows you have.
- A bull is a digit that is in the correct position.
- A cow is a digit that is in the number, but not in the correct position.
- The game ends when you guess the number correctly.""")
    print_sep(INTRO_TEXT)

    user_guess = check_user_input()
    bulls, cows, number_of_guesses = check_bulls_and_cows(user_guess, generated_game_number, guesses)
    bulls_word, cows_word = choose_word(bulls, cows)
    
    print(f"You have {bulls} {bulls_word} and {cows} {cows_word}.")
    print_sep(INTRO_TEXT)

    while user_guess != generated_game_number:
        user_guess = check_user_input()
        bulls, cows, number_of_guesses = check_bulls_and_cows(user_guess, generated_game_number, guesses)
        bulls_word, cows_word = choose_word(bulls, cows)
        print(f"You have {bulls} {bulls_word} and {cows} {cows_word}.")
        print_sep(INTRO_TEXT)

    else:
        print(f"""
Congratulations! You've guessed the number {generated_game_number}.
You needed {number_of_guesses} guesses to get it right.""")
            
        
if __name__ == "__main__":
    main()