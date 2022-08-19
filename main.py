from random import randint

if __name__ == '__main__':
    rand_num = randint(1, 100)
    print('Guess the number between 1 and 100!')
    while True:
        try:
            guessed_number = int(input('Guess the number: '))
        except ValueError:
            print('You need to enter a integer!')
            continue
        if guessed_number < rand_num:
            print('To small!')
        elif guessed_number > rand_num:
            print('To big!')
        else:
            print('You win!')
            break

