import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    """ 
    Generates a question for the "Calculator" game.

    Returns:
        str: A string representing the arithmetic expression (e.g., "3 + 5").
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    question = f'{num_1} {operator} {num_2}'
    return question


def generate_answer(question):
    """ 
    Calculates the correct answer for the given arithmetic expression.

    Args:
        question (str): The arithmetic expression to evaluate (e.g., "3 + 5").

    Returns:
        int: The result of the arithmetic expression.
    """
    correct_answer = eval(question)
    return correct_answer
