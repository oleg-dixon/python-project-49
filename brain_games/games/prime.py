import random


DESCRIPTION = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
    )


def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """ 
    Generates a question for the "Is it a prime number?" game.

    Returns:
        int: A random integer between 1 and 100.
    """
    question = random.randint(1, 100)
    return question


def generate_answer(question):
    """ 
    Determines if the given number is prime.

    Args:
        question (int): The number to check for primality.

    Returns:
        str: 'yes' if the number is prime, otherwise 'no'.
    """
    return 'yes' if is_prime(question) else 'no'
