#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

if __name__ == '__main__':
    #список работников
    workers = []

    #организовать бесконечный цикл запроса команд 
    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            name = input("Фамилия и инициалы? ")
            post = input("Должность? ")
            year = int(input("Год поступления? "))

            worker = {
                'name': name,
                'post': post,
                'year': year,
            }

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key = lambda item: item.get('name', ''))
    
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                 '-' * 4,
                 '-' * 30,
                 '-' * 20,
                 '-' * 8
                )

            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8}'.format(
                    "№",
                    "Ф.И.О.",
                    "Должность",
                    "Год"
                )
            )

            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('post', ''),
                        worker.get('year', 0)
                    )
                )
            
            print(line)
        elif command.startswitch('select '):
            today = date.today()

            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])
            count = 0
            for worker in workers:
                if today.year - worker.get('year', today.year) >= period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, worker.get('name', ''))
                    )
            if count == 0:
                print("Работники с заданным стажем не найдены.")
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - ")