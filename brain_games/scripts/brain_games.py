from brain_games.cli import welcome_user


def greeting():
    return 'Welcome to the Brain Games!'


def main():
    print(greeting())
    welcome_user()


if __name__ == '__main__':
    main()
