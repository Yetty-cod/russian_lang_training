import sqlite3
from random import choice, randint


def info():
    print('Добро пожаловать в тренажёр! Выберите номер задания:')
    print('4 - постановка ударения')

    print('Для возвращения в меню используйте команду /exit')


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
        if answer == '/exit':
            return
        while not answer.isdigit() or int(answer) not in [1, 2]:
            print('Неверный ввод')
            answer = input()
            if answer == '/exit':
                return

        answer = int(answer) - 1
        if answer == num:
            print('Верно V')
        else:
            print('Неверно X')
        print('Правильно -', correct_word)
        print('-' * 15)
