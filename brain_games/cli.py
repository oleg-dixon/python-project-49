import prompt


def welcome_user():
    """ User greeting function
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
