from brain_games import engine
from brain_games.cli import welcome_user
from brain_games.scripts.run_brain_games import greeting


def calc_game():
    """ The main function of the game is "Calculator".
    """
    print(greeting())
    user_name = welcome_user()
    print('What is the result of the expression?')
    correct_answers_need = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_need:
        _, generate_result = engine.generate_expression()
        answer = engine.user_answer_integer()

        if answer == generate_result:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{answer} is wrong answer;(. " 
                  f"Correct answer was {generate_result}"
                  f"\nLet's try again, {user_name}!")
            break

    if correct_answers_count == correct_answers_need:
        print(f'Congratulations, {user_name}!')
