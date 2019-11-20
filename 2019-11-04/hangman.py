import random

def ask_user():
    answer = input('Would you like to play? y or n ')
    if answer == 'y':
        return True
    else:
        return False


def load_words():
    words = []
    with open('C:\\users\\Nathaniel\\Documents\\words.txt') as f:
        for line in f.readlines():
            words.append(line.strip().lower())
    return words


def play_game(word):
    strikes = 0
    guessed = set()
    while True:
        print_board(strikes, word, guessed)
        guess = input('Guess a letter: ').lower()
        if guess in guessed:
            print('You already guessed that!')
        else:
            guessed.add(guess)
            if guess not in word:
                strikes += 1
        if strikes > 5:
            print_board(strikes, word, set(word))
            print('You lost, sorry')
            return False
        if set(word) - guessed == set():
            print('You win!')
            return True


def print_board(strikes, word, guessed):
    head = 'o' if strikes > 0 else ''
    arm_one = '\\' if strikes > 2 else ' ' if strikes > 1 else ''
    neck = '|' if strikes > 1 else ''
    arm_two = '/' if strikes > 3 else ''
    leg_one = '/' if strikes > 4 else ''
    leg_two = '\\' if strikes > 5 else ''
    board = f"""   +--+
   |  {head}
   | {arm_one}{neck}{arm_two}
   | {leg_one} {leg_two}
---+---"""
    print(board)
    print(' '.join(l if l in guessed else '_' for l in word))
    print(guessed)


def print_standings(win, loss):
    print(win, '-', loss)


def main():
    win, loss = 0, 0
    while True:
        play = ask_user()
        if play:
            words = load_words()
            word = words[random.randint(0, len(words) - 1)]
            user_win = play_game(word)
            if user_win:
                win += 1
            else:
                loss += 1
            print_standings(win, loss)
        else:
            break

if __name__ == '__main__':
    main()
