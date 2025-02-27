import random

import prompt


def generate_number():
    """ A function for generating random numbers
    """
    number = random.randint(0, 100)
    print(f'Question: {number}')
    return number


def generate_expression():
    """ A function for generating an expression and its result
    """
    operators = ['+', '-', '*']
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    operator = random.choice(operators)
    expression = f'{num_1} {operator} {num_2}'
    result = eval(expression)
    print(f'Question: {expression}')
    return expression, result


def user_answer_string():
    """ User response string input  function
    """
    user_answer_string = prompt.string('Your answer: ')
    return user_answer_string


def user_answer_integer():
    """ User response integer input  function
    """
    user_answer_integer = prompt.integer('Your answer: ')
    return user_answer_integer


def is_even(number):
    """ The number parity check function
    """
    return number % 2 == 0