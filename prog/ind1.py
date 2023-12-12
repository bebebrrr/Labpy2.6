#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

if __name__ == '__main__':
    #список поездов
    trains = []

    #организовать бесконечный цикл запроса команд 
    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            nomer = input("Номер поезда? ")
            punkt = input("Пункт назначения? ")
            time = int(input("Время назначения? (час) "))

            train = {
                'punkt': punkt,
                'nomer': nomer,
                'time': time,
            }

            trains.append(train)

            if len(trains) > 1:
                trains.sort(key = lambda item: item.get('punkt', ''))
    
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )

            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )

            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        train.get('punkt', ''),
                        train.get('nomer', ''),
                        train.get('time', 0)
                    )
                )
            
            print(line)
        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])
            count = 0
            for train in trains:
                if train.get('time', 0) >= period:
                    count += 1
                    print(count, 
                        train.get('punkt', ''),
                        train.get('nomer', ''),
                        train.get('time')
                    )
            if count == 0:
                print("Поезда с заданным временем не найдены.")
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <стаж> - запросить поезда с временем отправления;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
           