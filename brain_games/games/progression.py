import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    """ 
    Generates a question for the "Arithmetic progression" game.

    Returns:
        str: A string representing the arithmetic progression 
        with one hidden element.
    """
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, len(progression) - 1)
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question


def generate_answer(question):
    """ 
    Calculates the correct answer for the "Arithmetic progression" game.

    Args:
        question (str): A string representing the arithmetic 
        progression with one hidden element.

    Returns:
        str: The hidden number in the progression.
    """
    elements = question.split()
    hidden_index = elements.index('..')
    progression = []
    
    for i, element in enumerate(elements):
        if element == '..':
            progression.append(None)
        else:
            progression.append(int(element))

    known_indices = [i for i, x in enumerate(progression) if x is not None]
    first_val, second_val = progression[known_indices[0]], progression[known_indices[1]]
    first_idx, second_idx = known_indices[0], known_indices[1]
    step = (second_val - first_val) // (second_idx - first_idx)

    if hidden_index == 0:
        correct_answer = progression[1] - step
    elif hidden_index == len(progression) - 1:
        correct_answer = progression[-2] + step
    else:
        correct_answer = progression[hidden_index - 1] + step

    return str(correct_answer)
