from functions import *


tasks = {4: task_4,
         9: task_9}


def main():
    info()
    while True:
        command = input()
        if not command.isdigit():
            print('Неверный ввод')
            continue

        command = int(command)
        if command in tasks:
            tasks[command]()
        else:
            print('Такого задания нет')
        print('\n')
        info()


if __name__ == '__main__':
    main()
