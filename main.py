from functions import *


tasks = {4: task_4,
         9: task_9,
         10: task_10,
         11: task_11}


def main():
    info()
    while True:
        command = input()
        if not command.isdigit():
            print(Fore.YELLOW + 'Неверный ввод')
            continue

        command = int(command)
        if command in tasks:
            print()
            tasks[command]()
        else:
            print(Fore.YELLOW + 'Такого задания нет')
        print('\n')
        info()


if __name__ == '__main__':
    main()
