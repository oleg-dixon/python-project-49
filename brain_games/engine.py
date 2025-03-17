import prompt


CORRECT_ANSWERS_NEED = 3


def run_game(game_module):
    """ A universal game engine.
    Accepts the game module, which should contain:
    - DESCRIPTION: description of the game
    - generate_round(): a function that returns a question
    - generate_answer(question): a function that returns the correct answer
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.DESCRIPTION)
    
    correct_answers_count = 0

    while correct_answers_count < CORRECT_ANSWERS_NEED:
        question = game_module.generate_round()
        correct_answer = game_module.generate_answer(question)
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. " 
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {user_name}!")
            break

    if correct_answers_count == CORRECT_ANSWERS_NEED:
        print(f'Congratulations, {user_name}!')
