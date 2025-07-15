"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Martin Šenk
email: oshenny@icloud.com
"""

# This is the program that will simulate the game of Bulls and Cows.

import random


INTRO_TEXT = """Hi there! 
I've generated a random 4 digit number for you. 
 Let's play a bulls and cows game."""

SENTENCE_ENDING_CHARS = ["!", "?", "."]


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

separator = "-" * max(calculate_sentence_lengths(separate_sentences(INTRO_TEXT)))


def generate_game_number() -> str:
    
    """
    Generate a random 4-digit number with no repeating digits.
    """

    first_number = random.choice(range(1, 10))
    other_numbers = random.sample([number for number in range(10) if number != first_number], 3)

    print(other_numbers)

    return str(first_number) + "".join(str(other_numbers))


def check_user_input() -> str:

    while True:
        user_input = input("What is your guess? \n >>> ").strip()
        print(separator)
        
        if not user_input.isdigit():
            print("Your input should only contain digits.")
            print(separator)

        elif len(user_input) != 4:
            print("Please enter a 4-digit number.")
            print(separator)

        elif user_input[0] == "0":
            print("First digit cannot be 0. Please try again.")
            print(separator)

        elif len(set(user_input)) != 4:
            print("Eeach digit in the number must be unique. Please try again.")
            print(separator)
        else: 
            return user_input


guesses = []

def check_bulls_and_cows(guess: str, game_number: str) -> tuple:

    while True:
        if guess not in guesses:
            guesses.append(guess)

            bulls = sum(1 for position in range(4) if guess[position] == game_number[position])
            cows = sum(1 for digit in guess if digit in game_number) - bulls
            number_of_guesses = len(guesses)
            break


        else:
            print("You've already guessed that number. Try again.")
            print(separator)
            guess = check_user_input()

    return bulls, cows, number_of_guesses


def choose_word(bulls: int, cows: int) -> tuple:

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
    introduction_sentences = separate_sentences(INTRO_TEXT)
    
    for sentence in introduction_sentences:
        print(sentence)
        print(separator)
    
    generated_game_number = generate_game_number()

    print(f"""The ruels are simple:
- You will guess a 4-digit number.
- For every guess, I will tell you how many bulls and cows you have.
- A bull is a digit that is in the correct position.
- A cow is a digit that is in the number, but not in the correct position.
- The game ends when you guess the number correctly.""")
    print(separator)

    user_guess = check_user_input()
    bulls, cows, number_of_guesses = check_bulls_and_cows(user_guess, generated_game_number)
    bulls_word, cows_word = choose_word(bulls, cows)
    
    print(f"You have {bulls} {bulls_word} and {cows} {cows_word}.")
    print(separator)

    while user_guess != generated_game_number:
        user_guess = check_user_input()
        bulls, cows, number_of_guesses = check_bulls_and_cows(user_guess, generated_game_number)
        bulls_word, cows_word = choose_word(bulls, cows)
        print(f"You have {bulls} {bulls_word} and {cows} {cows_word}.")
        print(separator)

    else:
        print(f"""
Congratulations! You've guessed the number {generated_game_number}.
You needed {number_of_guesses} guesses to get it right.""")
            
        
if __name__ == "__main__":
    main()