import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """
    Generates a question for the "Greatest Common Divisor" game.

    Returns:
        str: A string containing two random integers between 0 and 100, separated by a space.
    """
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    question = f'{num_1} {num_2}'
    return question


def generate_answer(question):
    """ 
    Calculates the greatest common divisor (GCD) of two numbers.

    Args:
        question (str): A string containing two integers separated by a space.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    num_1, num_2 = map(int, question.split())

    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    correct_answer = num_1
    
    return correct_answer
