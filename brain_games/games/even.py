from brain_games import engine
from brain_games.cli import welcome_user
from brain_games.scripts.run_brain_games import greeting


def even_game():
    """ The main function of the game is "Parity check".
    """
    print(greeting())
    user_name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    correct_answers_need = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_need:
        number = engine.generate_number()
        answer = engine.user_answer_string()

        if answer not in ['yes', 'no']:
            print(f"Input incorrect! Let's try again, {user_name}!")
            break

        is_number_even = engine.is_even(number)
        correct_answer = 'yes' if is_number_even else 'no'

        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {user_name}!")
            break

    if correct_answers_count == correct_answers_need:
        print(f'Congratulations, {user_name}!')
