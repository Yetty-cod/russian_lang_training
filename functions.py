import sqlite3
from random import choice, randint
from colorama import Fore, Back, Style, init

# Инициализация colorama(необходима для Windows)
init(autoreset=True)


def info():
    print('Добро пожаловать в тренажёр! Выберите номер задания:')
    print('4 - постановка ударения')
    print('9 - корни')
    print('10 - приставки')
    print('11 - суффиксы')

    print('Для возвращения в меню используйте команду /выход')


def load_from_db(task):
    connection = sqlite3.connect('tasks.sqlite')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM task_{task}')
    data = cursor.fetchall()
    connection.close()
    return data


def task_4():
    print('Начинается тренировка по 4 заданию')
    print('Для выбора варианта ответа введите 1 или 2 соответственно\n')

    data = load_from_db(4)
    while True:
        question = choice(data)
        word = question[1]
        correct_word = word[:question[2]] + word[question[2]].upper() + word[question[2] + 1:]
        incorrect_word = word[:question[3]] + word[question[3]].upper() + word[question[3] + 1:]

        num = randint(0, 1)
        s = ['', '']
        s[num] = correct_word
        s[abs(num - 1)] = incorrect_word
        print('\t'.join(s))

        answer = input()
        if answer == '/выход':
            return
        while not answer.isdigit() or int(answer) not in [1, 2]:
            print(Fore.YELLOW + 'Неверный ввод')
            answer = input()
            if answer == '/выход':
                return

        answer = int(answer) - 1
        if answer == num:
            print(Fore.GREEN + 'Верно V')
        else:
            print(Fore.RED + 'Неверно X')
        print('Правильно -', correct_word)
        print('-' * 15)


def task_9():
    print('Начинается тренировка по 9 заданию')
    print('Для выбора варианта ответа введите букву, которая должна стоять в пропуске\n')

    data = load_from_db(9)
    while True:
        question = choice(data)
        word = question[1]
        letter = question[2]

        print(word)
        answer = input()
        if answer == '/выход':
            return
        while not answer.isalpha() or len(answer) != 1:
            print(Fore.YELLOW + 'Неверный ввод')
            answer = input()
            if answer == '/выход':
                return

        if answer == letter:
            print(Fore.GREEN + 'Верно V')
        else:
            print(Fore.RED + 'Неверно X')
        print('Правильно -', word.replace('..', letter))
        print('-' * 15)


def task_10():
    print('Начинается тренировка по 10 заданию')
    print('Для выбора варианта ответа введите букву, которая должна стоять в пропуске\n')

    data = load_from_db(10)
    while True:
        question = choice(data)
        word = question[1]
        letter = question[2]

        print(word)
        answer = input()
        if answer == '/выход':
            return
        while not answer.isalpha() or len(answer) != 1:
            print(Fore.YELLOW + 'Неверный ввод')
            answer = input()
            if answer == '/выход':
                return

        if answer == letter:
            print(Fore.GREEN + 'Верно V')
        else:
            print(Fore.RED + 'Неверно X')
        print('Правильно -', word.replace('..', letter))
        print('-' * 15)


def task_11():
    print('Начинается тренировка по 11 заданию')
    print('Для выбора варианта ответа введите букву, которая должна стоять в пропуске\n')

    data = load_from_db(11)
    while True:
        question = choice(data)
        word = question[1]
        letter = question[2]

        print(word)
        answer = input()
        if answer == '/выход':
            return
        while not answer.isalpha() or len(answer) != 1:
            print(Fore.YELLOW + 'Неверный ввод')
            answer = input()
            if answer == '/выход':
                return

        if answer == letter:
            print(Fore.GREEN + 'Верно V')
        else:
            print(Fore.RED + 'Неверно X')
        print('Правильно -', word.replace('..', letter))
        print('-' * 15)