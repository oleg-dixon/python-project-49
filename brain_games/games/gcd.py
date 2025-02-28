import random

from brain_games import engine


def generate_even_question():
    """ Generating a question for "The greatest common divisor" game.
    """
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    question = f'{num_1} {num_2}'

    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    correct_answer = num_1

    return question, correct_answer


def gcd_game():
    """ Launching "The greatest common divisor" game.
    """
    description = 'Find the greatest common divisor of given numbers.'
    engine.run_game(description, generate_even_question)
