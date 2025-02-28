import random

from brain_games import engine


def generate_even_question():
    """ Generating a question for the "Arithmetic progression" game.
    """
    start = random.randint(1, 100)
    step = random.randint(2, 10) 
    length = random.randint(5, 10)
    question = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = question[hidden_index]
    question[hidden_index] = '..'
    return question, correct_answer


def progression_game():
    """ Launching "Arithmetic progression" game.
    """
    description = 'What number is missing in the progression?'
    engine.run_game(description, generate_even_question)
