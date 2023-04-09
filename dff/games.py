import random

def guess_number(attemp = 0):
    random_number = random.randint(1, 10)
    my_number = 0
    while random_number != my_number:
        my_number = input('Отгадай число от 1 до 10, которое я загадал ')
        if random_number == my_number:
            print('Ты угадал : )')
        else:
            print('Ты проиграл : (')
            if attemp < 9:
                print('Попробуй еще раз')
        attemp += 1
        if attemp == 9:
            print('Слишком много попыток. Число которое я загадал это ', random_number)
            break

if __name__ == '__main__':
    guess_number()