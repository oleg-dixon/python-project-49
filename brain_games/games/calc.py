import random

from brain_games import engine


def generate_question_and_answer():
    """ Generating a question for the "Calculator" game.
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    expression = f'{num_1} {operator} {num_2}'
    correct_answer = eval(expression)
    return expression, correct_answer


def calc_game():
    """ Launching the "Calculator" game.
    """
    description = 'What is the result of the expression?'
    engine.run_game(description, generate_question_and_answer)
