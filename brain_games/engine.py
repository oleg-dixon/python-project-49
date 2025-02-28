import prompt

from brain_games.scripts.brain_games import greeting


def run_game(game_description, generate_question_and_answer):
    """ A common game engine for all games.
        :param game_description: Description of the game (string)
        :param generate_question_and_answer: A function that 
        generates a question and a correct answer
    """
    print(greeting())
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_description)
    
    correct_answers_need = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_need:
        question, correct_answer = generate_question_and_answer()
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

    if correct_answers_count == correct_answers_need:
        print(f'Congratulations, {user_name}!')
