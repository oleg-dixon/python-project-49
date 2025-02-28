import random

from brain_games import engine


def generate_even_question():
    """ Generating a question for the "Parity Check" game.
    """
    number = random.randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer


def even_game():
    """ Launching the "Parity Check" game.
    """
    description = "Answer 'yes' if the number is even, otherwise answer 'no'."
    engine.run_game(description, generate_even_question) 
