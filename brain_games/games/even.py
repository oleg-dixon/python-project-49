import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """ 
    Generates a question for the "Parity Check" game.

    Returns:
        int: A random integer between 0 and 100.
    """
    question = random.randint(0, 100)
    return question


def generate_answer(question):
    """ 
    Determines if the given number is even.

    Args:
        question (int): The number to check for parity.

    Returns:
        str: 'yes' if the number is even, otherwise 'no'.
    """
    return 'yes' if question % 2 == 0 else 'no'
