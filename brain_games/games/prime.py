import random

from brain_games import engine


def is_prime(number):
    """A function to check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_even_question():
    """ Generating a question for "Is it a prime number?" game.
    """
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def prime_game():
    """ Launching "Is it a prime number?" game.
    """
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.run_game(description, generate_even_question)
