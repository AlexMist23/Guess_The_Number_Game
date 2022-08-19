from random import randint

if __name__ == '__main__':
    rand_num = randint(1, 100)
    while True:
        guessed_number = int(input('Guess the number: '))
        if guessed_number < rand_num:
            print('To small!')
        elif guessed_number > rand_num:
            print('To big!')
        else:
            print('You win!')
            break

