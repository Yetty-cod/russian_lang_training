import sqlite3


def main():
    connection = sqlite3.connect('tasks.sqlite')
    cursor = connection.cursor()

    # code of program will be here

    connection.close()


if __name__ == 'main':
    main()
