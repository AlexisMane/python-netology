# coding=Windows_1251
import os

migrations = os.path.dirname(os.path.abspath(__file__))

def searching():
    search = input('Введите строку:')
    counter = int()
    for f in sql_list.copy():
        if f.endswith(".sql"):
            if search in f:
                print(f)
                counter += 1
            else:
                sql_list.remove(f)
        else:
            sql_list.remove(f)
    print(counter)


if __name__ == '__main__':
    sql_list = os.listdir(migrations)
    while True:
        searching()
