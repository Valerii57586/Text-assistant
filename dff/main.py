import games 

command = input('Что делать?\n')

if command == 'Давай поиграем':
    print('Вот игры в которые я умею играть: ')
    print('1. Угадай число')
    game = int(input('Выбери игру напишите её порядковый номер: '))
if game == 1:
    games.guess_number()
# CKJF
